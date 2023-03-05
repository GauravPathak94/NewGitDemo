from django.urls import path
from .views import Studentdetails,StudentInfo

urlpatterns = [
    path('stu/', Studentdetails.as_view()),
    path('stu/<int:id>/', StudentInfo.as_view())
]