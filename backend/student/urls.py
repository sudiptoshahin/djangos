from django.urls import path, include
from student import views

app_name = 'student'

urlpatterns = [
    path('list/', views.student_list, name='student_list'),
]