# Generated by Django 3.0.2 on 2020-01-27 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('third', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurand',
            name='image',
            field=models.CharField(default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='restaurand',
            name='password',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
    ]
