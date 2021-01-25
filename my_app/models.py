from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a Book Genre(topic it relates) (Eg: Sports, Entertainment etc.,)')

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)

    isbn = models.CharField('ISBN', max_length=13, unique=True, default='0000000000000',
        help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null = True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief about the book')

    genre = models.ManyToManyField(Genre, help_text='Select a genre')

    def __str__(self):
        return self.title

class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
