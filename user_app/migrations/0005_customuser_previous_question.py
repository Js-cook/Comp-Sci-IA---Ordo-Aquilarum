# Generated by Django 3.1.5 on 2022-03-18 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0004_auto_20220318_1448'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='previous_question',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_app.question'),
        ),
    ]
