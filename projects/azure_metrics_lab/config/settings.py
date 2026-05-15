import os

# =========================================================
# AZURE STORAGE
# =========================================================

AZURE_STORAGE_USE_AZURITE = os.getenv(
    "AZURE_STORAGE_USE_AZURITE",
    "true"
).lower() == "true"

AZURE_STORAGE_ACCOUNT_NAME = os.getenv(
    "AZURE_STORAGE_ACCOUNT_NAME"
)

AZURE_STORAGE_ACCESS_KEY = os.getenv(
    "AZURE_STORAGE_ACCESS_KEY"
)

AZURE_TABLE_NAME = os.getenv(
    "AZURE_TABLE_NAME",
    "MetricsData"
)

# =========================================================
# POSTGRESQL
# =========================================================

PG_HOST = os.getenv("PG_HOST")

PG_DATABASE = os.getenv("PG_DATABASE")

PG_USER = os.getenv("PG_USER")

PG_PASSWORD = os.getenv("PG_PASSWORD")

PG_PORT = os.getenv(
    "PG_PORT",
    "5432"
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

    required_vars = {
        "AZURE_TABLE_NAME":
            AZURE_TABLE_NAME
    }

    missing = [
        k for k, v in required_vars.items()
        if not v
    ]

    if missing:

        raise ValueError(
            "Variables de entorno faltantes: "
            + ", ".join(missing)
        )
