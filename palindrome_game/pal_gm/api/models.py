import random
import this
from django.db import models

# Create your models here.

# Creating User Model


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25,null=True)
    password = models.CharField( max_length=12,null=True)
    phone_no = models.CharField( max_length=10, null=True)



# Creating Game Model
class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    game_string=models.CharField(max_length=6, default="",blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def set_string(self,strh):
        self.game_string +=strh