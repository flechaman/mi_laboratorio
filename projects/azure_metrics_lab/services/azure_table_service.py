import json
import uuid
import logging
import pytz

from datetime import datetime

from azure.data.tables import (
    TableServiceClient,
    TableEntity
)

from azure.core.exceptions import (
    ResourceExistsError
)

from config.settings import (
    AZURE_STORAGE_CONNECTION_STRING,
    AZUREWEBJOBS_STORAGE,
    AZURE_STORAGE_ACCOUNT_NAME,
    AZURE_STORAGE_ACCESS_KEY,
    AZURE_TABLE_NAME
)


class AzureTableService:

    def __init__(self):

        connection_string = (
            AZURE_STORAGE_CONNECTION_STRING
        )

        if not connection_string:

            connection_string = AZUREWEBJOBS_STORAGE

        if not connection_string:

            connection_string = (
                f"DefaultEndpointsProtocol=https;"
                f"AccountName={AZURE_STORAGE_ACCOUNT_NAME};"
                f"AccountKey={AZURE_STORAGE_ACCESS_KEY};"
                f"EndpointSuffix=core.windows.net"
            )

        self.table_service = (
            TableServiceClient
            .from_connection_string(
                connection_string
            )
        )

        self._create_table_if_needed()

    def _create_table_if_needed(self):

        try:

            self.table_service.create_table(
                table_name=AZURE_TABLE_NAME
            )

            logging.info(
                f"Tabla creada: "
                f"{AZURE_TABLE_NAME}"
            )

        except ResourceExistsError:

            logging.info(
                f"Tabla ya existe: "
                f"{AZURE_TABLE_NAME}"
            )

    def save_metrics(
        self,
        metrics_data
    ):

        madrid_tz = pytz.timezone(
            "Europe/Madrid"
        )

        partition_key = metrics_data.get(
            "automation_name",
            "unknown"
        )

        row_key = (
            f"{metrics_data.get('execution_id', str(uuid.uuid4()))}"
            f"_{int(datetime.now(madrid_tz).timestamp())}"
        )

        entity = TableEntity()

        entity["PartitionKey"] = partition_key
        entity["RowKey"] = row_key

        for key, value in metrics_data.items():

            if value in (
                None,
                "",
                [],
                {}
            ):
                continue

            safe_key = (
                key.replace("-", "")
                .replace(".", "")
            )

            if isinstance(
                value,
                (dict, list)
            ):
                entity[safe_key] = json.dumps(
                    value,
                    ensure_ascii=False
                )

            else:
                entity[safe_key] = value

        table_client = (
            self.table_service
            .get_table_client(
                table_name=AZURE_TABLE_NAME
            )
        )

        table_client.create_entity(
            entity=entity
        )

        return row_key
