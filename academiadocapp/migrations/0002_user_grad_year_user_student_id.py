# Generated by Django 4.1.5 on 2023-02-07 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academiadocapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='grad_year',
            field=models.IntegerField(blank=True, default=1900),
        ),
        migrations.AddField(
            model_name='user',
            name='student_id',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
