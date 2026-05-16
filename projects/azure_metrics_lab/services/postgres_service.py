import json
import logging
import psycopg2

from config.settings import (
    PG_HOST,
    PG_DATABASE,
    PG_USER,
    PG_PASSWORD,
    PG_PORT
)

class PostgreSQLService:

    def __init__(self):

        self.connection = psycopg2.connect(

            host=PG_HOST,
            database=PG_DATABASE,
            user=PG_USER,
            password=PG_PASSWORD,
            port=PG_PORT
        )

        self.connection.autocommit = False

        logging.info(
            "Conexion PostgreSQL OK"
        )

    def save_metrics(
        self,
        partition_key,
        row_key,
        metrics_data
    ):

        query = """
            INSERT INTO metrics (

                partition_key,
                row_key,
                metrics_json,
                created_at

            )
            VALUES (

                %s,
                %s,
                %s::jsonb,
                NOW()

            )
        """

        try:

            with self.connection.cursor() as cursor:

                cursor.execute(

                    query,

                    (
                        partition_key,
                        row_key,
                        json.dumps(metrics_data)
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
