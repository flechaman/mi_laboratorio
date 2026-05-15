import json
import logging
import azure.functions as func

from services.metrics_processor import (
    MetricsProcessor
)

app = func.FunctionApp(
    http_auth_level=func.AuthLevel.ANONYMOUS
)

processor = None


def get_processor():

    global processor

    if processor is None:

        processor = MetricsProcessor()

    return processor

@app.route(
    route="process_metrics",
    methods=["POST"]
)
def process_metrics(
    req: func.HttpRequest
) -> func.HttpResponse:

    try:

        req_body = req.get_json()

        result = get_processor().process_metrics(
            req_body
        )

        status_code = (
            200
            if result["status"] == "success"
            else 500
        )

        return func.HttpResponse(
            json.dumps(
                result,
                ensure_ascii=False,
                indent=2
            ),
            status_code=status_code,
            mimetype="application/json"
        )

    except Exception as e:

        logging.error(e)

        return func.HttpResponse(
            json.dumps({
                "status": "error",
                "message": str(e)
            }),
            status_code=500,
            mimetype="application/json"
        )
