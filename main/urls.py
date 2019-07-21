from django.urls import path
from main import views

urlpatterns = [
    path('',views.index,name='index'),
    path('students',views.student),
    path('addstudent',views.addstudent),
]
