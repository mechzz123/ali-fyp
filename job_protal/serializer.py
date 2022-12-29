
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

    def to_representation(self, instance):
        data = {
            "id" : instance.id,
            "order_status" : instance.order_status,
            "order_location" : instance.order_location,
            "order_contact" : instance.order_contact,
            "job_name" : instance.job.job_name,
            "job_fair" : instance.job_fair,
            "job_id" : instance.job.id
        }

        return data