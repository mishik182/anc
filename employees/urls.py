from django.urls import path

from employees.views import (
    EmployeeListAPIView,
    SubordinateEmployeeListAPIView,
    EmployeeUpdateAPIView
)

urlpatterns = [
    path('', EmployeeListAPIView.as_view()),
    path('<int:pk>', SubordinateEmployeeListAPIView.as_view()),
    path('update/<int:pk>', EmployeeUpdateAPIView.as_view()),
]
