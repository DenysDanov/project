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
    model = models.CharField("Модель", max_length=255)
    producer = models.ForeignKey(
        verbose_name = "Виробник", 
        to = CarProducer, 
        on_delete = models.CASCADE)
    year_of_production = models.IntegerField("Рік випуску")

    def __str__(self) -> str:
        return f'{self.producer} {self.model} {self.year_of_production}р.'

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
    amount = models.IntegerField('Кількість')
    
    def __str__(self) -> str:
        return f'{self.name} від {self.belongs_to.__str__()}'
        
    class Meta:
        verbose_name = "Запчастина"
        verbose_name_plural = "Запчастини"
