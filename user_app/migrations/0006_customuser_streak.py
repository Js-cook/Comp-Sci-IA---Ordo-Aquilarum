# Generated by Django 3.1.5 on 2022-04-06 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0005_customuser_previous_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='streak',
            field=models.IntegerField(default=0),
        ),
    ]
