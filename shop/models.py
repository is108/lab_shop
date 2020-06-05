from django.db import models
import datetime
from django.utils import timezone

class Product(models.Model):
    short_title = models.CharField(max_length = 24)
    title = models.CharField(max_length = 300)
    short_text = models.CharField(max_length = 100)
    text = models.TextField()
    img = models.ImageField()
    price = models.IntegerField()
    pub_data = models.DateTimeField(blank = 'True', null = 'True')

    def publicate(sef):
        pub_data = timezone.now()
        self.save()

    def __str__(self):
        return self.title
