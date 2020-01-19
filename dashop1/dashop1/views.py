from django.http import request
from django.http import JsonResponse

def test(request):
            
    return JsonResponse({'code':200})