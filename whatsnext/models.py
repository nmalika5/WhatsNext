from __future__ import unicode_literals

from django.db import models

class Task(models.Model):
    task_id = models.IntegerField(max_length=1000, primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    task_description = models.CharField(max_length=1000)
    created = models.DateField()
    status = models.IntegerField()

    def __str__(self):              
        return self.task_description

    def status_status(self):
        "Returns the task's status."        
        import datetime        
        if self.status == 0:
            return "Open"
        elif self.status == 1:
            return "In Progress"
        elif self.status == 2:
            return "Completed"



class User(models.Model):
    user_id = models.IntegerField(max_length=1000, primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)

    def __str__(self):              
        return self.user_id

    def _get_full_name(self):
        "Returns the user's full name."
        
        return '%s %s' % (self.first_name, self.last_name)
    
    full_name = property(_get_full_name)


class TaskJoin(models.Mode):
    """A join table for many-to-many relationships between tasks"""
    
    start_task = models.ForeignKey(Task, on_delete=models.CASCADE)
    final_task = models.ForeignKey(Task, on_delete=models.CASCADE)
