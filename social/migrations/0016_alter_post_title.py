# Generated by Django 4.0.4 on 2022-04-29 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0015_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='04/28', max_length=100),
        ),
    ]
