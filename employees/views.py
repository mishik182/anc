from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.pagination import PageNumberPagination

from employees.models import Employee
from employees.serializers import EmployeeListSerializer, EmployeeUpdateSerializer


class DefaultPageNumberPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'


class EmployeeListAPIView(ListAPIView):
    serializer_class = EmployeeListSerializer
    queryset = Employee.objects.filter(job_title=7)


class SubordinateEmployeeListAPIView(EmployeeListAPIView):
    pagination_class = DefaultPageNumberPagination
    all_fields = Employee._meta.get_fields()
    excluded_fields = [
        '_search',
        'nd',
        'rows',
        'page',
        'sidx',
        'sord',
    ]

    def get_queryset(self):
        employee = Employee.objects.get(pk=self.kwargs.get('pk'))
        subordinate_employee = Employee.objects.filter(job_title=employee.job_title - 1)
        request = self.request.GET

        if request.get('sidx') and request.get('sord') == 'asc':
            subordinate_employee = subordinate_employee.order_by(request.get('sidx'))
        elif request.get('sidx') and request.get('sord') == 'desc':
            subordinate_employee = subordinate_employee.order_by('-' + request.get('sidx'))

        if request.get('_search') == 'true':

            for key, value in request.items():
                lookup = '%s' % key

                if key in self.excluded_fields:
                    continue

                if key == 'name' or key == 'email':
                    lookup = '%s__iregex' % key
                    subordinate_employee = subordinate_employee.filter(**{lookup: value})
                else:
                    subordinate_employee = subordinate_employee.filter(**{lookup: value})

        return subordinate_employee


class EmployeeUpdateAPIView(UpdateAPIView):
    serializer_class = EmployeeUpdateSerializer
    queryset = Employee.objects.all()
