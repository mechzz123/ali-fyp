
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



class GetOrderSerializer(ModelSerializer):
    job_name = serializers.SerializerMethodField("job_name")
    job_fair = serializers.SerializerMethodField("job_fair")

    def job_name(self,obj):
        try:
            return obj.job.job_name

        except:
            return None

    def job_fair(self,obj):
        try:
            return obj.job.job_fair

        except:
            return None

    class Meta:
        model = Order
        fields = ['order_status','order_location','order_contact','sender','receiver','location_coordinates','job','job_name','job_fair']