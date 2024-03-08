# Generated by Django 5.0.3 on 2024-03-08 15:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('account_no', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('regtime', models.DateTimeField(auto_now_add=True, help_text='time of registration')),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('postcode', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('pin', models.CharField(help_text='4 digit PIN for transaction verification.', max_length=128)),
                ('nickname', models.CharField(default='User', max_length=50, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
