# Generated by Django 4.2.5 on 2023-10-26 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0005_alter_estateimage_options_remove_estate_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='estate',
            name='image',
            field=models.ImageField(blank=True, upload_to='agency/%Y/%m/%d', verbose_name='Изображение'),
        ),
    ]
