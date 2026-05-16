import logging
import pytz

from datetime import datetime

from templates.embedded_template import (
    EMBEDDED_TEMPLATE
)

from services.azure_table_service import (
    AzureTableService
)

from services.postgres_service import (
    PostgreSQLService
)

from config.settings import (
    validate_environment
)


class MetricsProcessor:

    def __init__(self):

        validate_environment()

        self.azure_service = (
            AzureTableService()
        )

        self.postgres_service = (
            PostgreSQLService()
        )

    def process_metrics(
        self,
        input_data
    ):

        try:

            final_data = (
                self._merge_metrics(
                    input_data
                )
            )

            # =====================================================
            # AZURE TABLE
            # =====================================================

            row_key = (
                self.azure_service
                .save_metrics(
                    final_data
                )
            )

            # =====================================================
            # POSTGRESQL
            # =====================================================

            self.postgres_service.save_metrics(

                partition_key=
                    final_data.get(
                        "automation_name",
                        "unknown"
                    ),

                row_key=row_key,

                metrics_data=final_data
            )

            return {

                "status": "success",

                "row_key": row_key,

                "processed_at":
                    datetime.now(
                        pytz.timezone(
                            "Europe/Madrid"
                        )
                    ).isoformat()
            }

        except Exception as e:

            logging.error(e)

            return {
                "status": "error",
                "message": str(e)
            }

    def _merge_metrics(
        self,
        input_data
    ):

        final_data = {}

        for key, value in input_data.items():

            if value not in (
                None,
                "",
                [],
                {}
            ):

                final_data[key] = value

        for key, value in EMBEDDED_TEMPLATE.items():

            if key not in final_data:

                final_data[key] = value

        if "timestamp" not in final_data:

            madrid_tz = pytz.timezone(
                "Europe/Madrid"
            )

            final_data["timestamp"] = (
                datetime.now(
                    madrid_tz
                ).isoformat()
            )

        return final_data