from django.db import models


class Estate(models.Model):
    class NamesChoices(models.TextChoices):
        HOUSE = 'house', 'Дом'
        FLAT = 'flat', 'Квартира'
        SECTOR = 'sector', 'Участок'
        COMM = 'commercial', 'Коммерческий'
        RENT = 'rent', 'Аренда'
        GARAGE = 'garage', 'Гараж'
        ROOM = 'room', 'Комната'

    name = models.CharField(
        max_length=10,
        default=NamesChoices.HOUSE,
        choices=NamesChoices.choices,
        verbose_name='Наименование'
    )
    area = models.FloatField(verbose_name='Общая площадь')
    rooms = models.IntegerField(verbose_name='Количество комнат', default=1)
    material = models.CharField(max_length=128, verbose_name='Материал стен')
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(max_length=200, verbose_name='Слаг')
    image = models.ImageField(upload_to='agency/%Y/%m/%d', blank=True, verbose_name='Изображение')
    available = models.BooleanField(default=True, verbose_name='Доступен к продаже?')

    class Meta:
        ordering = ['area']
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'

    def __str__(self):
        return f'{self.name.capitalize()} - {self.rooms} ком., {self.area} м2'
