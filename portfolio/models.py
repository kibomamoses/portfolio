from django.db import models


# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=196)
    email = models.EmailField()
    subject = models.CharField(max_length=196)
    message = models.TextField()

    def __str__(self):
        return self.email
