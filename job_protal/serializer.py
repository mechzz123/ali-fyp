
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import JobCatagories , Job , Order

class JobCatagorySerializer(ModelSerializer):

    class Meta:
        model = JobCatagories
        fields = '__all__'




class JobSerializer(ModelSerializer):

    class Meta:
        model = Job
        fields = '__all__'


class OrderSerializer(ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
