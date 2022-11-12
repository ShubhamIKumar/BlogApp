from django.db import models

class Info(models.Model):  
    fname  = models.CharField(max_length=100)  
    username    = models.CharField(max_length=100)
    email = models.CharField(max_length=100)  
    contact = models.CharField(max_length=15)
    pass1 = models.CharField(max_length=50)
    pass2 = models.CharField(max_length=50) 

#     USERNAME_FIELD = 'username'
#     PASSWORD_FIELD ='pass1'

#     # def __str__(self):
#     #     return self.username