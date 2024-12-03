from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt  # 临时关闭CSRF验证，生产环境需要正确配置
def echo_view(request):
    if request.method == 'POST':
        try:
            # 解析JSON数据
            data = json.loads(request.body)
            message = data.get('message', '')
            
            # 返回相同的消息
            return JsonResponse({
                'echo': message
            })
        except json.JSONDecodeError:
            return JsonResponse({
                'error': 'Invalid JSON'
            }, status=400)
    
    return JsonResponse({
        'error': 'Only POST method is supported'
    }, status=405)
