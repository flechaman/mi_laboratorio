import logging
import psycopg2

from psycopg2 import sql
from psycopg2.extras import Json

from config.settings import (
    PG_HOST,
    PG_DATABASE,
    PG_USER,
    PG_PASSWORD,
    PG_PORT,
    PG_SSLMODE,
    PG_TABLE_NAME
)

class PostgreSQLService:

    def __init__(self):

        self.connection = psycopg2.connect(

            host=PG_HOST,
            database=PG_DATABASE,
            user=PG_USER,
            password=PG_PASSWORD,
            port=PG_PORT,
            sslmode=PG_SSLMODE
        )

        self.connection.autocommit = False

        logging.info(
            "Conexion PostgreSQL OK"
        )

        self._create_table_if_needed()

    def _create_table_if_needed(self):

        query = sql.SQL("""
            CREATE TABLE IF NOT EXISTS {table_name} (
                id BIGSERIAL PRIMARY KEY,
                partition_key VARCHAR(255),
                row_key VARCHAR(255),
                execution_id VARCHAR(255),
                automation_name VARCHAR(255),
                timestamp_spain TIMESTAMP,
                data JSONB,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """).format(
            table_name=sql.Identifier(PG_TABLE_NAME)
        )

        try:

            with self.connection.cursor() as cursor:

                cursor.execute(query)

            self.connection.commit()

            logging.info(
                f"Tabla PostgreSQL OK: {PG_TABLE_NAME}"
            )

        except Exception as e:

            self.connection.rollback()

            logging.error(e)

            raise

    def save_metrics(
        self,
        partition_key,
        row_key,
        metrics_data
    ):

        query = sql.SQL("""
            INSERT INTO {table_name} (
                partition_key,
                row_key,
                execution_id,
                automation_name,
                timestamp_spain,
                data
            )
            VALUES (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
            )
        """).format(
            table_name=sql.Identifier(PG_TABLE_NAME)
        )

        try:

            with self.connection.cursor() as cursor:

                cursor.execute(

                    query,

                    (
                        partition_key,
                        row_key,
                        metrics_data.get("execution_id"),
                        metrics_data.get(
                            "automation_name",
                            "unknown"
                        ),
                        metrics_data.get("timestamp"),
                        Json(metrics_data)
                    )
                )

            self.connection.commit()

            logging.info(

                f"PostgreSQL OK: "
                f"{partition_key} / {row_key}"

            )

        except Exception as e:

            self.connection.rollback()

            logging.error(e)

            raise
