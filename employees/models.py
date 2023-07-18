from django.db import models


class JobTitleChoice:
    JOB_TITLE = (
        (1, 'Касир'),
        (2, 'Медичний представник'),
        (3, 'Фармацевт-лаборант'),
        (4, 'Фармацевт-провізор'),
        (5, 'Фармацевт-консультант'),
        (6, 'Аптечний директор'),
        (7, 'Власник аптеки'),
    )


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    job_title = models.IntegerField(choices=JobTitleChoice.JOB_TITLE, default=1)
    accept_date = models.DateField()

    class Meta:
        ordering = ['-job_title']

    def __str__(self):
        return self.name
