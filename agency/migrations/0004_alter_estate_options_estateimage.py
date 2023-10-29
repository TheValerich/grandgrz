# Generated by Django 4.2.5 on 2023-10-24 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0003_estate_best_offer_alter_estate_material'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estate',
            options={'ordering': ['-available'], 'verbose_name': 'Объект', 'verbose_name_plural': 'Объекты'},
        ),
        migrations.CreateModel(
            name='EstateImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='estates/%Y/%m/%d', verbose_name='Изображение')),
                ('estate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='agency.estate', verbose_name='Объект')),
            ],
        ),
    ]
