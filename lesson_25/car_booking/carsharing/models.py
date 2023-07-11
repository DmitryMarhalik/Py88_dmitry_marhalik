from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255, null=True, default=None)
    phone = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.name}: {self.phone}'


class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ForeignKey('Image', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class Image(models.Model):
    title = models.CharField(max_length=255)
    url_image = models.ImageField(upload_to='logo_auto')

    def __str__(self):
        return f'{self.title}'


class AutoModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.brand} {self.name}'


class Auto(models.Model):
    free = 'free'
    booked = 'booked'
    taken = 'taken'
    STATUSES = ((free, 'FREE'),
                (booked, 'BOOKED'),
                (taken, 'TAKEN'))

    auto_model = models.ForeignKey('AutoModel', on_delete=models.CASCADE)
    vin_code = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=7, choices=STATUSES, default=free)
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True, default=None)

    def __str__(self):
        return f'{self.auto_model} {self.vin_code}'
