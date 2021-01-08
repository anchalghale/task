import time
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from threading import Thread

def upload_account(task_obj):
    '''DO some function'''
    def task():
        time.sleep(1) # Delay to ensure task obj is created before updating task object
        for i in range(11):
            update_task_object(task_obj,i*10, '')
            time.sleep(1)

        task_obj.active=False
        task_obj.completed=True
        task_obj.save()
    Thread(target=task).start()


def update_task_object(task_obj, i, errors):
    task_obj.percentage_completed = i
    task_obj.errors += errors
    task_obj.save()

class Task(models.Model):
    '''Models for task'''
    active = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    percentage_completed = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    errors = models.TextField(default='', blank=True)
    created = models.DateTimeField(auto_now_add=True)
 
    def save(self, *args, **kwargs):
        if self.pk is None:
            self.active=True
            upload_account(self)
        super(Task, self).save(*args, **kwargs)