from django.db import models


class Books(models.Model):
    books_name = models.CharField(max_length=50, unique=True)
    genre = models.ForeignKey(to='Genre', on_delete=models.CASCADE)
    description = models.TextField()
    
    def __str__(self):
        return f'{self.books_name.title()}: {self.description[:20]}'

class Genre(models.Model):
    genre_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.genre_name.title()}'
