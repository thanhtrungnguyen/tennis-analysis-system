import logging
import time

logger = logging.getLogger('django')


class PerformanceMonitor:
    def process_request(self, request):
        """Store the start time when the request starts processing."""
        request.start_time = time.time()

    def process_response(self, request, response):
        """Calculate the duration and log it."""
        duration = time.time() - getattr(request, 'start_time', time.time())
        logger.info(f"Request took {duration:.4f} seconds.")
        return response
