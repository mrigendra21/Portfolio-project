from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')  # Images with the same name will be renamed differently by Django. User need not to worry!
    summary = models.CharField(max_length=200)      # This sets the maximum length of character for each Job item.
