from django.db import models
from django.urls import reverse


class Estate(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='estates', verbose_name='Категория')
    name = models.CharField(max_length=64, verbose_name='Название', default='')
    area = models.FloatField(verbose_name='Общая площадь', blank=True)
    rooms = models.IntegerField(verbose_name='Количество комнат', default=1, blank=True)
    material = models.CharField(max_length=128, verbose_name='Материал стен', blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    image = models.ImageField(upload_to='agency/%Y/%m/%d', blank=True, verbose_name='Изображение')
    available = models.BooleanField(default=True, verbose_name='Доступен к продаже?')
    best_offer = models.BooleanField(default=False, verbose_name='Лучшее предложение')

    class Meta:
        ordering = ['-available']
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'

    def __str__(self):
        return f'{self.name.capitalize()} - {self.rooms} ком., {self.area} м2'


class Category(models.Model):
    name = models.CharField(max_length=64, verbose_name='Наименование')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class EstateImage(models.Model):
    estate = models.ForeignKey('Estate', on_delete=models.CASCADE, related_name='images', verbose_name='Объект')
    image = models.ImageField(upload_to='estates/%Y/%m/%d', verbose_name='Изображение')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Workers(models.Model):
    name = models.CharField(max_length=128, verbose_name='ФИО')
    description = models.TextField(verbose_name='О себе', blank=True)
    phone = models.CharField(max_length=128, verbose_name='Телефон', blank=True)
    photo = models.ImageField(upload_to='workers/%Y/%m/%d', verbose_name='Фото', blank=True)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.name


class Requisites(models.Model):
    bank = models.CharField(max_length=256, verbose_name='Банк получателя')
    bick = models.CharField(max_length=128, verbose_name='БИК')
    account = models.CharField(max_length=128, verbose_name='Р/счёт')
    corr_account = models.CharField(max_length=128, verbose_name='Корр. счет')

    class Meta:
        verbose_name = 'Реквизиты'
        verbose_name_plural = 'Реквизиты'

    def __str__(self):
        return self.bank
