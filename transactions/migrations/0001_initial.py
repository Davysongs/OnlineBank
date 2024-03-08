# Generated by Django 5.0.3 on 2024-03-08 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trans',
            fields=[
                ('name', models.CharField(max_length=120)),
                ('bank', models.CharField(max_length=50)),
                ('account_no', models.CharField(max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('date', models.DateTimeField(auto_now_add=True, help_text='time of transaction')),
                ('transaction_ID', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('info', models.CharField(max_length=120)),
                ('status', models.CharField(choices=[('Success', 'Success'), ('Failed', 'Failed'), ('Pending', 'Pending')], max_length=10)),
            ],
        ),
    ]
