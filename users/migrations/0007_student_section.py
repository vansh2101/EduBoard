# Generated by Django 3.2.7 on 2021-09-20 05:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_student_adm_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='section',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]