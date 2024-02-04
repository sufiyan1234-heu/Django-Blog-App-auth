from django.db import models

# Create your models here.


class Contact(models.Model):

    company = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    desc = models.TextField(blank=True, max_length=150)
    date = models.DateField(auto_now_add=True)


class Contact2(models.Model):

    company = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    desc = models.TextField(blank=True, max_length=150)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email


class Contact3(models.Model):

    company = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    desc = models.TextField(blank=True, max_length=150)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email
