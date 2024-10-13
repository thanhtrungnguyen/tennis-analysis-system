import logging
import json

logger = logging.getLogger('django')

class ResponseLogger:
    def process_response(self, request, response):
        logger.info(f"Response: {response.status_code} {response.reason_phrase}")
        if hasattr(response, 'content') and response.get('Content-Type') == 'application/json':
            try:
                content = json.loads(response.content)
                logger.info(f"Response Body: {json.dumps(content, indent=2)}")
            except json.JSONDecodeError:
                logger.info("Response Body: (not JSON)")
