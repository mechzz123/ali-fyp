from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
# Create your views here.
from django.utils import timezone
from common.models import StatusChoices
from common.baselayer.baseAuth import UserAuthentication
from common.helper import encode_token, create_resonse
from rest_framework.response import Response
from common.enums import Message
from .models import User
from .serializer import (
    UserLoginSerializer, UserSignupSerializer  )
from django.db.models import F , Prefetch


class UserAuthView(ModelViewSet):
    authentication_classes = []
    permission_classes = [AllowAny]
    model = User

    def login(self, request):
        try:
            user = self.model.objects.filter(email=request.data.get('email')).first()
            try:
                if user:
                    if not user.check_password(request.data.get("password")):
                        return Response(create_resonse(True, Message.incorrect_password.value, []))
                    data = UserLoginSerializer(user,many=False).data
                    data['token'] = encode_token(user)
                    user.login_token = data['token']
                    user.save()
                    return Response(create_resonse(False, Message.success.value, [data]))
                return Response(create_resonse(True, Message.user_not_exists.value, []))
            except Exception as e:
                print(e)
                return Response(create_resonse(True, Message.try_with_correct_data.value, []))
        except Exception as e:
            print(e)
            return Response(create_resonse(True, Message.server_error.value, []))

    def signup(self, request):
        try:
            if self.model.objects.filter(email=request.data.get("email")).exists():
                return Response(create_resonse(True, Message.email_exists.value, []))
            serialized_data = UserSignupSerializer(data=request.data)
            if serialized_data.is_valid():
                serialized_data.save()
                return Response(create_resonse(False, Message.success.value, [serialized_data.data]))
            return Response(create_resonse(True, Message.try_with_correct_data.value, data=[]))

        except Exception as e:
            print(e)
            return Response(create_resonse(True, Message.server_error.value, data=[]))


    def get_dashboard(self,request):
        try:
            return Response(create_resonse(False, Message.success.value, data=[]))

        except Exception as e:
            print(e)
            return Response(create_resonse(True, Message.server_error.value, data=[]))
