# Generated by Django 3.1 on 2022-07-27 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20220727_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='name',
            field=models.TextField(default='Nothing'),
        ),
        migrations.AddField(
            model_name='document',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]