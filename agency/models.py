from django.db import models


class Estate(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='estates')

    area = models.FloatField(verbose_name='Общая площадь')
    rooms = models.IntegerField(verbose_name='Количество комнат', default=1)
    material = models.CharField(max_length=128, verbose_name='Материал стен')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(max_length=200, verbose_name='Слаг')
    image = models.ImageField(upload_to='agency/%Y/%m/%d', blank=True, verbose_name='Изображение')
    available = models.BooleanField(default=True, verbose_name='Доступен к продаже?')

    class Meta:
        ordering = ['available']
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'

    def __str__(self):
        return f'{Category.name.capitalize()} - {self.rooms} ком., {self.area} м2'


class Category(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
