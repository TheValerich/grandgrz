# Generated by Django 4.2.5 on 2023-10-29 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0010_alter_workers_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='estate',
            name='slug',
        ),
    ]
