from django.db import models

class Projects(models.Model):
    project_name = models.CharField(max_length=128)
    customer = models.CharField(max_length=128)
    label = models.CharField(max_length=128)
    project_type = models.CharField(max_length = 128)

    def __st__(self):
        return self.project_name
