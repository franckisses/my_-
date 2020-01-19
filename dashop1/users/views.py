from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
from .models import UserProfile
# Create your views here.

class UserView(View):

    def get(self,request):
        return JsonResponse(
            {'code':200,'data':'我是来自get中的方法'}
            )

    def post(self,requset):
        json_body = requset.body
        json_dict = json.loads(json_body)
        # TODO 检查每一个数据(username password email phone)
        try:
            UserProfile.objects.create(username=username,

            )
        # 检查数据
        # 保存用户
        # 返回格式
        正常响应：
            {   'code':200,
                'data':
                {
                    'username':xxx,
                    'token':'xxxx',
                    'count':1
                    }
            }
        # 异常响应：
            {
                'code':10111,
                'error':'没有传递邮箱'
            }
        return JsonResponse(
            {'code':200,'data':'我是来自post中的方法'}
            )

