# Generated by Django 5.1.2 on 2024-11-03 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='published_date',
        ),
        migrations.AddField(
            model_name='book',
            name='publication_year',
            field=models.IntegerField(default=200),
            preserve_default=False,
        ),
    ]
