from django.db import models 

class CarProducer(models.Model):
    name = models.CharField("Назва", max_length=255)

    def __str__(self) -> str:
        return self.name
    
    def __repr__(self) -> str:
        return f'CarProducer(name={self.name})'

    class Meta:
        verbose_name = "Виробник"
        verbose_name_plural = "Виробники"


class Auto(models.Model):
    
    WHEEL_DRIVE_CHOICES = [
        ('Повний', '1'),
        ('Передній', '2'),
        ('Задній', '3'),
    ]
    FUEL_CHOICES = [
        ('Бензин', 0),
        ('Електро', 1),
        ('Дизель', 2),
    ]
    BODY_CHOICES = [
        ('Седан', 0),
        ('Кросовер', 1),
        ('Мінівен', 2),
        ('Мікровен', 3),
        ('Хетчбек', 4),
        ('Універсал', 5),
        ('Купе', 6),
        ('Кабріолет', 7),
        ('Пікап', 8),
        ('Ліфтбек', 9),
        ('Фастбек', 10),
        ('Лімузин', 11),
        ('Родстер', 12),
    ]
    vin = models.CharField('VIN код', max_length=64, primary_key=True)
    model = models.CharField("Модель", max_length=255)
    producer = models.ForeignKey(
        verbose_name = "Виробник", 
        to = CarProducer, 
        on_delete = models.CASCADE)
    year_of_production = models.IntegerField("Рік випуску")
    engine_volume = models.FloatField('Об\'єм двигуна')
    wheel_drive = models.CharField('Привід', max_length=255, choices=WHEEL_DRIVE_CHOICES)
    fuel = models.CharField('Тип палива', max_length=255, choices=FUEL_CHOICES)

    def __str__(self) -> str:
        return f'{self.vin} | {self.producer} {self.model} {self.year_of_production}р.'

    class Meta:
        verbose_name = "Автомобіль"
        verbose_name_plural = "Автомобілі"


class Part(models.Model):

    name = models.CharField('Назва', max_length=255)
    belongs_to = models.ForeignKey(
            verbose_name = "Автомобіль", 
            to = Auto, 
            on_delete = models.DO_NOTHING
        )
    amount = models.IntegerField('Кількість', blank=True)
    
    def __str__(self) -> str:
        return f'{self.name} від {self.belongs_to.__str__()}'
        
    class Meta:
        verbose_name = "Запчастина"
        verbose_name_plural = "Запчастини"
