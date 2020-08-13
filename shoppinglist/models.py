
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from django.utils import timezone


class todolist(models .Model):
    author = models .ForeignKey(settings.AUTH_USER_MODEL, on_delete=models .CASCADE)
    title = models .CharField(max_length=200)
    created_date = models .DateTimeField(default=timezone.now)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
# Create your models here