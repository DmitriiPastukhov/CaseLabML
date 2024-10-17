from django.db import models

class Review(models.Model):
    text = models.TextField()
    rating = models.IntegerField(default=0)  #поле для рейтинга
    sentiment = models.CharField(max_length=10, default='')  #поле для статуса комментария

    def __str__(self):
        return self.text[:50]