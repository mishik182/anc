from django.core.management.base import BaseCommand, CommandError
from faker import Faker

from employees.models import Employee


class Command(BaseCommand):
    help = "Generate and save test data to the DB!"
    fake = Faker('uk_UA')

    def save_to_db(self, count, job_title):
        for i in range(1, count + 1):
            Employee.objects.create(
                name=self.fake.name(),
                email=self.fake.email(),
                accept_date=self.fake.date(),
                job_title=job_title,
            )

    def handle(self, *args, **options):
        self.save_to_db(20, 7)
        self.stdout.write(self.style.SUCCESS(str(Employee.objects.all().count()) + ' users was created!'))
        self.save_to_db(500, 6)
        self.stdout.write(self.style.SUCCESS(str(Employee.objects.all().count()) + ' users was created'))
        self.save_to_db(1000, 5)
        self.stdout.write(self.style.SUCCESS(str(Employee.objects.all().count()) + ' users was created'))
        self.save_to_db(2000, 4)
        self.stdout.write(self.style.SUCCESS(str(Employee.objects.all().count()) + ' users was created'))
        self.save_to_db(5000, 3)
        self.stdout.write(self.style.SUCCESS(str(Employee.objects.all().count()) + ' users was created'))
        self.save_to_db(10000, 2)
        self.stdout.write(self.style.SUCCESS(str(Employee.objects.all().count()) + ' users was created'))
        self.save_to_db(35000, 1)
        self.stdout.write(self.style.SUCCESS(str(Employee.objects.all().count()) + ' users was created'))

        self.stdout.write(self.style.SUCCESS('Total users - ' + str(Employee.objects.all().count())))

        self.stdout.write(self.style.SUCCESS('Successfully!'))
