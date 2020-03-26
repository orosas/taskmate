from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TaskList(models.Model):
    manage = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    task = models.CharField('Tareas Por Realizar', max_length=300)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.task + ' - Task. Status Completed: ' + str(self.done)
    
