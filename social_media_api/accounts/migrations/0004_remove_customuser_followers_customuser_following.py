# Generated by Django 5.1.2 on 2024-12-15 17:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_followers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='followers',
        ),
        migrations.AddField(
            model_name='customuser',
            name='following',
            field=models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]
