from django.db import models
from django.contrib.auth.models import User

class UserInfo(User):
    fullname=models.CharField(max_length=100,default="Not Mentioned")
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    money=models.CharField(max_length=20,default='0')

    class Meta:
        db_table='UserInfo'