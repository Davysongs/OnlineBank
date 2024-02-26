from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=50)
    account_no = models.CharField(max_length=10, primary_key = True)
    balance = models.DecimalField(max_digits=8, decimal_places=2)
    regtime = models.DateTimeField(auto_now_add = True, help_text = "time of registeration")
    def __str__(self):
        return self.name 