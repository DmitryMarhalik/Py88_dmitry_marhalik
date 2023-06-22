from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255, null=True, default=None)
    phone = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.name}'


class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ForeignKey('Image', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class Image(models.Model):
    title = models.CharField(max_length=255)
    url_image = models.ImageField(upload_to='autos')

    def __str__(self):
        return f'{self.title}'


class AutoModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Auto(models.Model):
    STATUSES = (('1', 'FREE'),
                ('2', 'BOOKED'),
                ('3', 'TAKEN'))

    auto_model = models.ForeignKey('AutoModel', on_delete=models.CASCADE)
    vin_code = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=7, choices=STATUSES, default='1')
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, default=None)

    def __str__(self):
        return f'{self.STATUSES}'
