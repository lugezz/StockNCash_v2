from django.contrib.auth.models import AbstractUser
from django.db import models

from snc.settings import MEDIA_URL, STATIC_URL


class User(AbstractUser):
    image = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True, verbose_name='Imagen')

    def get_image(self):
        if self.image:
            return f'{MEDIA_URL}{self.image}'
        else:
            return f'{STATIC_URL}img/empty_user.png'

    class Meta:
        verbose_name = "Usuario"


class BaseModel(models.Model):
    user_creation = models.ForeignKey(User, on_delete=models.CASCADE,
                                      related_name='user_creation')
    date_creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    user_update = models.ForeignKey(User, on_delete=models.CASCADE,
                                    related_name='user_update')
    date_update = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True
