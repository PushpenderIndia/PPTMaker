from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=120)
    message = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class History(models.Model):
    topic_name = models.CharField(max_length=100)
    slide_count = models.CharField(max_length=100)
    ppt_path    = models.CharField(max_length=100)
    user_email  = models.CharField(max_length=100)


