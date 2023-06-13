from django.db import models

# Create your models here.

class GetCarImage(models.Model):
    image = models.ImageField(upload_to='car_images/')
    data = models.DateField(auto_now_add=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.data.strftime('%Y-%m-%d')
    