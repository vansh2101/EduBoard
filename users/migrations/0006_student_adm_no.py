# Generated by Django 3.2.7 on 2021-09-18 13:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_school_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='adm_no',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]