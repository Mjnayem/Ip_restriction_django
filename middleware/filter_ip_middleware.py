from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


class FilterIPMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def unauthorized_response(self, request):

        response = Response(
            {"detail": "This action is not authorized"},
            content_type="application/json",
            status=status.HTTP_401_UNAUTHORIZED,
        )
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = "application/json"
        response.renderer_context = {}

        # Render the response
        response._is_rendered = False
        response.render()
        return response

    def __call__(self, request):
        if not self.authorized(request):
            return self.unauthorized_response(request)
        return self.get_response(request)

    def authorized(self, request):

        allowed_ips = ['127.0.0.2', '27.147.204.53']  # Authorized ip's
        ip = request.META.get('REMOTE_ADDR')  # Get client IP
        if ip not in allowed_ips:
            return False
        else:
            return True
