# Generated by Django 3.1.5 on 2022-03-04 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noun', models.CharField(max_length=50)),
                ('case', models.CharField(max_length=15)),
                ('number', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=6)),
            ],
        ),
    ]