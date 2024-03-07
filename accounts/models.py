from django.db import models
from django.contrib.auth import get_user_model # Create your models here.
class Account(models.Model):
    user = models.OneToOneField(get_user_model(), null = True, on_delete = models.CASCADE)
    account_no = models.CharField(max_length=10, primary_key = True)
    balance = models.DecimalField(max_digits=8, decimal_places=2)
    regtime = models.DateTimeField(auto_now_add = True, help_text = "time of registeration")
    image = models.ImageField(upload_to = 'Profile Pictures')
    phone = models.CharField(blank = False, max_length = 15)
    address = models.CharField(blank = False, max_length = 200)
    city = models.CharField(blank = False, max_length = 200)
    country = models.CharField(blank = False, max_length = 200)
    postcode = models.CharField(blank = False, max_length = 200)
    state = models.CharField(blank = False, max_length=200)
    pin = models.CharField(max_length=128,help_text="4 digit PIN for transaction verification.")        
    def __str__(self):
        return self.account_no