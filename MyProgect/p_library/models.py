from django.db import models


class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"    


class Publisher(models.Model):
    name = models.TextField()
    city = models.TextField()   

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = "Издатель"
        verbose_name_plural = "Издатели"    


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    copy_count = models.PositiveSmallIntegerField(default=1)
    price = models.FloatField(default=0.00)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Книги'
        verbose_name_plural = 'Книги'


