from django.db import models
from django.conf import settings
from django.db import models



class shoppinglist (models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)





    def __str__(self):
        return self.title
# Create your models here.
