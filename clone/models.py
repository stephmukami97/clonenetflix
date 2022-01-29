from django.db import models

# Create your models here.
class Movies(models.Model):
    name=models.CharField( max_length=50)
    description=models.CharField(max_length=300)
    coverimage=models.ImageField(upload_to="img",blank=False)
    movie=models.FileField(upload_to='movie',blank=True)

    def __str__(self) :
        return self.name
