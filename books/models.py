from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    year = models.IntegerField()

    class Meta:
        verbose_name = "کتاب"
        verbose_name_plural = "کتاب‌ها"
    
    def __str__(self):
        return self.title
