from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=125)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    title = models.CharField(max_length=125)

    def __str__(self):
        return self.title
    
class Book(models.Model):
    title = models.CharField(max_length=125)
    author = models.ForeignKey(Author , on_delete=models.CASCADE , related_name='books')
    category = models.ManyToManyField(Category , related_name='books')
    publication_date = models.IntegerField()

    def __str__(self):
        return self.title