from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=64, help_text='Введите название датчика')
    description = models.TextField(max_length=256, help_text='Введите описание датчика', blank=True)
    

class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='owners')
    temperature = models.DecimalField(max_digits=5, decimal_places=2, help_text='Введите значение температуры в градусах по Цельсию')
    date_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True, null=True)
    