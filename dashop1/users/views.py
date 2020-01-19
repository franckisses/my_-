from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import json
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
        
        return JsonResponse(
            {'code':200,'data':'我是来自post中的方法'}
            )

