from django.db import models

class Myuser(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=12)
