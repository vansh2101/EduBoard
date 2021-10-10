# Generated by Django 3.2.7 on 2021-09-20 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=100)),
                ('deadline', models.DateTimeField()),
                ('description', models.CharField(max_length=10000)),
                ('grade', models.IntegerField()),
                ('section', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='circular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now=True)),
                ('description', models.CharField(max_length=10000)),
                ('grade', models.IntegerField()),
            ],
        ),
    ]