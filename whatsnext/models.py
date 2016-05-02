from __future__ import unicode_literals

from django.db import models
import datetime

STATUSES = {

  1: "Open", 

  2: "In Progress", 

  3: "Completed", 

} 
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)

    def __str__(self):              
        return self.id

    def _get_full_name(self):
        "Returns the user's full name."
        
        return '%s %s' % (self.first_name, self.last_name)
    
    full_name = property(_get_full_name)

class Task(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    task_description = models.CharField(max_length=1000)
    priority = models.IntegerField()
    # Later probably want to have a separate categories table to allow
    # for users to create their own categories.
    # But for now just have dumb integer field to keep the dream alive.
    category = models.IntegerField()
    created = models.DateTimeField(default=datetime.datetime.now)
    status = models.IntegerField(choices=STATUSES, default=1)

    def __str__(self):              
        return self.task_description

    def status_status(self):
        "Returns the task's status."   
        
        return STATUSES[self.status]     
        

class TaskJoin(models.Model):
    """A join table for many-to-many relationships between tasks"""
    
    start_task = models.ForeignKey(Task, on_delete=models.CASCADE)
    final_task = models.ForeignKey(Task, on_delete=models.CASCADE)
