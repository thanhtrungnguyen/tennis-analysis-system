import json
import logging

logger = logging.getLogger('django')


class RequestLogger:
    def process_request(self, request):
        logger.info(f"Request: {request.method} {request.get_full_path()}")
        if request.body:
            try:
                body = json.loads(request.body)
                logger.info(f"Request Body: {json.dumps(body, indent=2)}")
            except json.JSONDecodeError:
                logger.info("Request Body: (not JSON)")
