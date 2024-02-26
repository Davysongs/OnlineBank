# Generated by Django 5.0.1 on 2024-02-26 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('account_no', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=8)),
                ('regtime', models.DateTimeField(auto_now_add=True, help_text='time of registeration')),
            ],
        ),
    ]
