from django.urls import path

from . import views

urlpatterns = [

    path('',views.UserEndPoint.as_view())

]