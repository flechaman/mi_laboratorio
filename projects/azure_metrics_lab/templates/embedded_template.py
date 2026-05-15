from config.settings import (
    MANUAL_MINUTES_PER_ITEM,
    HOURLY_RATE_EUROS,
    AUTOMATION_COST_PER_ITEM,
    AUTOMATION_FIXED_COST,
    DATA_RETENTION_DAYS
)

EMBEDDED_TEMPLATE = {

    "version": "2.0",

    "description": "Universal metrics",

    "template_version": "2.0",

    "schema_version": "v2.0",

    "_metadata": {

        "version": "2.0",

        "compatibility": [
            "python",
            "logic_apps",
            "bash",
            "powershell",
            "java",
            "dotnet"
        ],

        "embedded_mode": True
    },

    "_config": {

        "manual_minutes_per_item":
            MANUAL_MINUTES_PER_ITEM,

        "hourly_rate_euros":
            HOURLY_RATE_EUROS,

        "automation_cost_per_item":
            AUTOMATION_COST_PER_ITEM,

        "automation_fixed_cost":
            AUTOMATION_FIXED_COST,

        "data_retention_days":
            DATA_RETENTION_DAYS
    }
}
