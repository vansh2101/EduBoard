# Generated by Django 3.2.7 on 2021-09-21 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_classes_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='circular',
            name='circular_for',
            field=models.CharField(choices=[('student', 'student'), ('teacher', 'teacher')], default='student', max_length=7),
            preserve_default=False,
        ),
    ]