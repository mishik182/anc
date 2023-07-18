from django.urls import path, include
from index.views import index_view

urlpatterns = [
    path('', index_view),
    path('api/v1/employees/', include('employees.urls')),
]
