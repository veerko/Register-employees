from django.urls import path

from employee_register import form
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('form/', views.employee_form, name='insert'),
    path('update/<str:pk>/', views.employee_update, name='update'),
    path('delete/<str:pk>/', views.employee_delete, name='delete'),

]
   