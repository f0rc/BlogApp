# Generated by Django 3.2.6 on 2021-08-13 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0007_auto_20210723_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='2021-08-12', max_length=100),
        ),
    ]
