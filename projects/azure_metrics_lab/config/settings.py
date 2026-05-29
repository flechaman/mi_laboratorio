import os


def get_env(
    *names,
    default=None
):

    for name in names:

        value = os.getenv(name)

        if value not in (
            None,
            ""
        ):
            return value

    return default


# =========================================================
# AZURE STORAGE
# =========================================================

AZURE_STORAGE_CONNECTION_STRING = get_env(
    "AZURE_STORAGE_CONNECTION_STRING"
)

AZUREWEBJOBS_STORAGE = get_env(
    "AzureWebJobsStorage"
)

AZURE_STORAGE_ACCOUNT_NAME = get_env(
    "AZURE_STORAGE_ACCOUNT_NAME"
)

AZURE_STORAGE_ACCESS_KEY = get_env(
    "AZURE_STORAGE_ACCESS_KEY"
)

AZURE_TABLE_NAME = get_env(
    "AZURE_TABLE_NAME",
    default="MetricsData"
)

# =========================================================
# POSTGRESQL
# =========================================================

PG_HOST = get_env(
    "PG_HOST",
    "PGHOST"
)

PG_DATABASE = get_env(
    "PG_DATABASE",
    "PGDATABASE"
)

PG_USER = get_env(
    "PG_USER",
    "PGUSER"
)

PG_PASSWORD = get_env(
    "PG_PASSWORD",
    "PGPASSWORD"
)

PG_PORT = get_env(
    "PG_PORT",
    "PGPORT",
    default="5432"
)

PG_SSLMODE = get_env(
    "PG_SSLMODE",
    "PGSSLMODE",
    default="prefer"
)

PG_TABLE_NAME = get_env(
    "PG_TABLE_NAME",
    default="metrics_data"
)

# =========================================================
# CONFIGURACION METRICAS
# =========================================================

MANUAL_MINUTES_PER_ITEM = float(
    os.getenv(
        "MANUAL_MINUTES_PER_ITEM",
        "15"
    )
)

HOURLY_RATE_EUROS = float(
    os.getenv(
        "HOURLY_RATE_EUROS",
        "30.0"
    )
)

AUTOMATION_COST_PER_ITEM = float(
    os.getenv(
        "AUTOMATION_COST_PER_ITEM",
        "0.1"
    )
)

AUTOMATION_FIXED_COST = float(
    os.getenv(
        "AUTOMATION_FIXED_COST",
        "0.5"
    )
)

DATA_RETENTION_DAYS = int(
    os.getenv(
        "DATA_RETENTION_DAYS",
        "90"
    )
)

# =========================================================
# VALIDACION
# =========================================================

def validate_environment():

    has_storage_connection = (
        AZURE_STORAGE_CONNECTION_STRING
        or AZUREWEBJOBS_STORAGE
    )

    required_vars = {
        "AZURE_TABLE_NAME":
            AZURE_TABLE_NAME,
        "PG_HOST":
            PG_HOST,
        "PG_DATABASE":
            PG_DATABASE,
        "PG_USER":
            PG_USER,
        "PG_PASSWORD":
            PG_PASSWORD,
        "PG_TABLE_NAME":
            PG_TABLE_NAME
    }

    if not has_storage_connection:

        required_vars.update({
            "AZURE_STORAGE_ACCOUNT_NAME":
                AZURE_STORAGE_ACCOUNT_NAME,
            "AZURE_STORAGE_ACCESS_KEY":
                AZURE_STORAGE_ACCESS_KEY
        })

    missing = [
        k for k, v in required_vars.items()
        if not v
    ]

    if missing:

        raise ValueError(
            "Variables de entorno faltantes: "
            + ", ".join(missing)
        )
