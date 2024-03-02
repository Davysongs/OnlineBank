from django.db import models
from django.contrib.auth import get_user_model 
from django.contrib.auth.hashers import make_password, check_password


# Create your models here.
class Account(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    account_no = models.CharField(max_length=10, primary_key = True)
    balance = models.DecimalField(max_digits=8, decimal_places=2)
    regtime = models.DateTimeField(auto_now_add = True, help_text = "time of registeration")
    image = models.ImageField(upload_to = 'Profile Pictures')
    first_name = models.CharField(max_length = 100, blank = False)
    last_name = models.CharField(max_length = 100, blank = False)
    email = models.EmailField()
    phone = models.CharField(blank = False, max_length = 11)
    address = models.CharField(blank = False, max_length = 200)
    city = models.CharField(blank = False, max_length = 200)
    country = models.CharField(blank = False, max_length = 200)
    postcode = models.CharField(blank = False, max_length = 200)
    state = models.CharField(blank = False, max_length=200)
    pin = models.CharField(max_length=128,help_text="4 digit PIN for transaction verification.")

    def set_pin(self, pin):
        # Hash the PIN before storing it
        self.pin = make_password(pin)

    def check_pin(self, pin):
        # Check if the provided PIN matches the hashed PIN
        return check_password(pin, self.pin)

    def save(self, *args, **kwargs):
        # Hash the PIN before saving the model instance
        if self.pin:
            self.set_pin(self.pin)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name 