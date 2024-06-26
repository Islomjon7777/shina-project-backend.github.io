from django.http import JsonResponse

class PathRestrictionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_paths = {
            'http://127.0.0.1:8000': ['/baskets/', '/products/', '/users/'],
            'http://localhost:5175': ['/baskets/', '/products/', '/users/','/admin/'],
        }
        
        origin = request.headers.get('Origin')
        path = request.path_info

        if origin in allowed_paths and path not in allowed_paths[origin]:
            return JsonResponse({'error': 'Path not allowed'}, status=403)
        
        response = self.get_response(request)
        return response