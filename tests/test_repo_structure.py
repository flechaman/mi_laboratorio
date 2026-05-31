from pathlib import Path
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[1]


class RepoStructureTests(unittest.TestCase):
    def test_required_top_level_files_exist(self):
        required = [
            "README.md",
            ".gitignore",
            ".env.example",
            "Makefile",
            ".pre-commit-config.yaml",
            "docs/labs.md",
            "docs/runbooks/lab-operativa-diaria.md",
            "scripts/check-lab.sh",
        ]

        missing = [path for path in required if not (ROOT / path).exists()]

        self.assertEqual([], missing)

    def test_functional_labs_have_readme(self):
        required = [
            "infra/airflow/README.md",
            "infra/oracle/README.md",
            "projects/azure_metrics_lab/README.md",
            "projects/mock-api/README.md",
            "projects/api-lab/README.md",
            "projects/storage-lab/README.md",
        ]

        missing = [path for path in required if not (ROOT / path).is_file()]

        self.assertEqual([], missing)

    def test_env_examples_exist_for_services_that_need_them(self):
        required = [
            ".env.example",
            "infra/airflow/.env.example",
            "infra/oracle/.env.example",
            "projects/azure_metrics_lab/local.settings.azure.example.json",
        ]

        missing = [path for path in required if not (ROOT / path).is_file()]

        self.assertEqual([], missing)

    def test_generated_files_are_not_tracked(self):
        self.assertTrue((ROOT / ".git").exists())

        result = subprocess.run(
            ["git", "ls-files"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )

        forbidden_fragments = [
            "__pycache__/",
            "logs/",
            "volumes/",
            "grafana.db",
        ]
        forbidden_suffixes = [
            ".pyc",
            ".zip",
        ]

        offenders = []
        for path in result.stdout.splitlines():
            if any(fragment in path for fragment in forbidden_fragments):
                offenders.append(path)
            if any(path.endswith(suffix) for suffix in forbidden_suffixes):
                offenders.append(path)

        self.assertEqual([], offenders)


if __name__ == "__main__":
    unittest.main()
