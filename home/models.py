from django.db import models

# Create your models here.
class Task(models.Model):
    Tasktitle = models.CharField(max_length=70)
    Taskdesc = models.CharField(max_length=70)

    def __str__(self):
        return self.Tasktitle
