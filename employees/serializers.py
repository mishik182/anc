from rest_framework import serializers


from employees.models import Employee


class EmployeeListSerializer(serializers.ModelSerializer):
    job_title = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = '__all__'

    @staticmethod
    def get_job_title(obj):
        return obj.get_job_title_display()


class EmployeeUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'
