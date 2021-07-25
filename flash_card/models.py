from django.db import models

# Create your models here.

class Card(models.Model):
    front_text = models.CharField(max_length=50)
    back_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField('date published')
    private = models.BooleanField()
    user = models.PositiveSmallIntegerField()
    likes = models.PositiveIntegerField()

    def __str__(self):
        return self.front_text
