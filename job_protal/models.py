from django.db import models

# Create your models here.
from django.db import models
from common.models import LogsMixin
from django.db.models import TextChoices
from  user.models import User
import jsonfield


class OrderTextChoices(TextChoices):
    PENDING = 1
    ACCEPTED = 2
    REJECTED = 3

class JobCatagories(LogsMixin):
    title = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title


class Job(LogsMixin):
    job_name = models.CharField(max_length=1000, null=True, blank=True)
    job_description = models.CharField(max_length=1000, null=True, blank=True)
    job_fair = models.FloatField(null=True, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True , related_name = "user_jobs")
    catagory = models.ForeignKey(JobCatagories,on_delete=models.CASCADE,null=True,blank=True , related_name = "catagory_jobs")

    def __str__(self):
        return self.title



class Order(LogsMixin):
    order_status = models.CharField(max_length=1000, null=True, blank=True)
    order_location= models.CharField(max_length=1000, null=True, blank=True)
    order_contact = models.FloatField(null=True, blank=True)
    sender = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True , related_name = "sender_orders")
    receiver = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True , related_name = "receiver_orders")
    location_coordinates = jsonfield.JSONField()
    job = models.ForeignKey(Job, on_delete=models.CASCADE, null=True, blank=True, related_name="job_order")
    def __str__(self):
        return self.title