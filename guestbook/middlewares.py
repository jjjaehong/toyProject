import logging

# logger ��������
request_logger = logging.getLogger('request_logger')

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # ��û ���� �α�
        request_logger.info(f"{request.method} {request.get_full_path()}")

        response = self.get_response(request)

        return response
