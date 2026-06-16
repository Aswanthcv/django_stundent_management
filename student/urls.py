from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('deleteStudent/<int:id>/',views.delete_student,name='deleteStudent'),
    path('updateStudent/<int:id>/',views.update_student,name='updateStudent'),
]
