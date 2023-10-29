# Generated by Django 4.2.5 on 2023-10-29 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0007_alter_estate_area_alter_estate_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='ФИО')),
                ('description', models.TextField(blank=True, verbose_name='О себе')),
                ('phone', models.CharField(max_length=128, verbose_name='Телефон')),
                ('photo', models.ImageField(upload_to='workers/%Y/%m/%d', verbose_name='Фото')),
            ],
        ),
    ]
