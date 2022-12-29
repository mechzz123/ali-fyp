"""FMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import JobCatagoriesApiViewSet , JobApiViewSet  , OrderApiViewSet

urlpatterns = [
    path("",JobApiViewSet.as_view({
        "get" : "get_jobs",
        "post" : "create_jobs"
    })),

    path("get-single-job", JobApiViewSet.as_view({
        "get": "get_single_job",
    })),

    path("catagories", JobCatagoriesApiViewSet.as_view({
        "get": "get_catagories",
        "post": "create_catagories"
    })),

    path("order", OrderApiViewSet.as_view({
        "get": "get_orders",
        "post": "create_order",
        "patch" : "update_order"
    })),
    path("vendor-jobs",JobApiViewSet.as_view({
        "get":"get_vendor_jobs"
    }))

]
