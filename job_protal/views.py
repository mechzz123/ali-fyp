
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
# Create your views here.
from django.utils import timezone
from common.models import StatusChoices
from common.baselayer.baseAuth import UserAuthentication
from common.helper import encode_token, create_resonse
from rest_framework.response import Response
from common.enums import Message
from .models import Job , JobCatagories , Order
from .serializer import (
    JobCatagorySerializer, JobSerializer , OrderSerializer  )
from user.models import UserTypeChoices



class JobCatagoriesApiViewSet(ModelViewSet):
    authentication_classes = [UserAuthentication]
    permission_classes = []
    model = JobCatagories
    serializer_class = JobCatagorySerializer

    def get_catagories(self, request):
        try:
            catagories = self.model.objects.filter()
            if catagories.exists():
                serialized_data = self.serializer_class(catagories,many=True).data
                return Response(create_resonse(False,Message.success.value,serialized_data))
            return Response(create_resonse(False,Message.record_not_found.value,[]))
        except Exception as e:
            print(e)
            return Response(create_resonse(True, Message.server_error.value, []))

    def create_catagories(self, request):
        try:
            serialized_data = self.serializer_class(data=request.data)
            if serialized_data.is_valid():
                serialized_data.save()
                return Response(create_resonse(False, Message.success.value, [serialized_data.data]))
            return Response(create_resonse(True, Message.try_with_correct_data.value, data=[]))

        except Exception as e:
            print(e)
            return Response(create_resonse(True, Message.server_error.value, data=[]))


class JobApiViewSet(ModelViewSet):
    authentication_classes = [UserAuthentication]
    permission_classes = []
    model = Job
    serializer_class = JobSerializer

    def get_jobs(self, request):
        try:
            if not request.query_params.get("catagory_id"):
                return Response(create_resonse(True,Message.success.value,[]))
            Jobs = self.model.objects.filter(catagory_id = request.query_params.get("catagory_id"))
            if Jobs.exists():
                serialized_data = self.serializer_class(Jobs,many=True).data
                return Response(create_resonse(False,Message.success.value,serialized_data))
            return Response(create_resonse(False,Message.record_not_found.value,[]))
        except Exception as e:
            print(e)
            return Response(create_resonse(True, Message.server_error.value, data=[]))

    def get_single_job(self, request):
        try:
            if not request.query_params.get("id"):
                return Response(create_resonse(True,Message.success.value,[]))
            Jobs = self.model.objects.filter(id = request.query_params.get("id"))
            if Jobs.exists():
                serialized_data = self.serializer_class(Jobs,many=False).data
                return Response(create_resonse(False,Message.success.value,[serialized_data]))
            return Response(create_resonse(False,Message.record_not_found.value,[]))
        except Exception as e:
            print(e)
            return Response(create_resonse(True, Message.server_error.value, data=[]))


    def create_jobs(self, request):
        try:
            request.data['user'] = request.user.id
            serialized_data = self.serializer_class(data=request.data)
            if serialized_data.is_valid():
                serialized_data.save()
                return Response(create_resonse(False, Message.success.value, [serialized_data.data]))
            return Response(create_resonse(True, Message.try_with_correct_data.value, data=[]))

        except Exception as e:
            print(e)
            return Response(create_resonse(True, Message.server_error.value, data=[]))


    def get_vendor_jobs(self,request):
        try:
            if request.user.user_type == UserTypeChoices.VENDOR:
                jobs = self.model.objects.filter(user_id = request.user.id)
                if jobs.exists():
                    serialized_data = self.serializer_class(jobs,many=True).data
                    return Response(create_resonse(False,Message.success.value,serialized_data))
                return Response(create_resonse(False,Message.record_not_found.value,[]))
        except Exception as e:
            print(e)
            return Response(create_resonse(True,Message.server_error.value,[]))


class OrderApiViewSet(ModelViewSet):
    authentication_classes = [UserAuthentication]
    permission_classes = []
    model = Order
    serializer_class = OrderSerializer

    def get_orders(self, request):
        try:
            if request.user.user_type == UserTypeChoices.VENDOR:
                orders = self.model.objects.filter(receiver_id = request.user.id)

            if request.user.user_type == UserTypeChoices.CLIENT:
                orders = self.model.objects.filter(sender_id = request.user.id)

            if orders.exists():
                serialized_data = self.serializer_class(orders,many=True).data
                return Response(create_resonse(False,Message.success.value,serialized_data))
            return Response(create_resonse(False,Message.record_not_found.value,[]))
        except Exception as e:
            print(e)
            return Response(create_resonse(True, Message.server_error.value, data=[]))


    def create_order(self, request):
        try:
            serialized_data = self.serializer_class(data=request.data)
            if serialized_data.is_valid():
                serialized_data.save()
                return Response(create_resonse(False, Message.success.value, [serialized_data.data]))
            return Response(create_resonse(True, Message.try_with_correct_data.value, data=[]))

        except Exception as e:
            print(e)
            return Response(create_resonse(True, Message.server_error.value, data=[]))


    def update_order(self, request):
        try:
            if not request.data.get("id"):
                return Response(create_resonse(True,Message.try_with_correct_data.value,[]))
            order = self.model.objects.filter(id = request.data.get("id"))
            if order.exists():
                serialized_data = self.serializer_class(order.last(),data=request.data)
                if serialized_data.is_valid():
                    serialized_data.save()
                    return Response(create_resonse(False, Message.success.value, [serialized_data.data]))
                return Response(create_resonse(True, Message.try_with_correct_data.value, data=[]))
            return Response(create_resonse(False,Message.record_not_found.value,[]))

        except Exception as e:
            print(e)
            return Response(create_resonse(True, Message.server_error.value, data=[]))