from django.db import models

# Create your models here.
class Trans(models.Model):
    name = models.CharField(max_length=50)
    account_no = models.CharField(max_length=10)
    amount = models.IntegerField()
    date = models.DateTimeField(auto_now_add = True, help_text = "time of transaction")
    transaction_ID = models.CharField(max_length=50)
    info = models.CharField(max_length = 120)
    def __str__(self):
        return self.name + "-" + self.account_no + "-" + str(
            self.amount) + "-" + self.date.strftime("%Y-%m-%d %H:%M:%S")