from django.db import models

#TODO: Import timezone to DateTime

from django.utils import timezone

class Comment(models.Model):
    name = models.CharField(max_length=20)
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    #FIXME: Create a Special Method
    def __str__(self):
        return '<Name: {}, ID: {}>'.format(self.name, self.id)