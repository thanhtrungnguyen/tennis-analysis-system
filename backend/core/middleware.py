import logging

from django.utils.deprecation import MiddlewareMixin

from core.handlers import request_logger, response_logger, performance

logger = logging.getLogger('django')


class ExtensibleMiddleware(MiddlewareMixin):
    def __init__(self, get_response=None):
        self.get_response = get_response
        # List of enabled handlers (can be configured via settings)
        self.handlers = [
            request_logger.RequestLogger(),
            response_logger.ResponseLogger(),
            performance.PerformanceMonitor(),
        ]

    def process_request(self, request):
        """Process each request through all enabled handlers."""
        for handler in self.handlers:
            if hasattr(handler, 'process_request'):
                handler.process_request(request)

    def process_response(self, request, response):
        """Process each response through all enabled handlers."""
        for handler in self.handlers:
            if hasattr(handler, 'process_response'):
                handler.process_response(request, response)
        return response
