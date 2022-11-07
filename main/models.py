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
        ('1','Повний'),   
        ('2','Передній'), 
        ('3','Задній'),   
    ]

    FUEL_CHOICES = [
        ('0','Бензин'),   
        ('1','Електро'),  
        ('2','Дизель'),   
        ('3','Гібрид'),   
    ]
# django.db.utils.IntegrityError: FOREIGN KEY constraint failed
    BODY_CHOICES = [
        ('0','Седан'),    
        ('1','Кросовер'), 
        ('2','Мінівен'),  
        ('3','Мікровен'), 
        ('4','Хетчбек'),  
        ('5','Універсал'),
        ('6','Купе'),     
        ('7','Кабріолет'),
        ('8','Пікап'),    
        ('9','Ліфтбек'),  
        ('10','Фастбек'), 
        ('11','Лімузин'), 
        ('12','Родстер'), 
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
    body = models.CharField('Тип кузова', max_length=255, choices=BODY_CHOICES)
    def __str__(self) -> str:
        return f'{self.vin} | {self.producer} {self.model} {self.year_of_production}р.'

    class Meta:
        verbose_name = "Автомобіль"
        verbose_name_plural = "Автомобілі"


class Part(models.Model):

    name = models.CharField('Назва', max_length=255)
    articul = models.CharField('Артикул', blank=True, max_length=255)
    buy_price = models.FloatField('Закупочна ціна', blank=True)
    sell_price = models.FloatField('Роздрібна ціна', blank=True)
    belongs_to = models.ForeignKey(
            verbose_name = "Автомобіль", 
            to = Auto, 
            on_delete = models.CASCADE
        )
    


    def __str__(self) -> str:
        return f'{self.name} від {self.belongs_to.producer} {self.belongs_to.model}'
        
    class Meta:
        verbose_name = "Запчастина"
        verbose_name_plural = "Запчастини"
