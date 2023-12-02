from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return f"{self.pk} - {self.first_name} {self.middle_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=250, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    year_publication = models.PositiveSmallIntegerField()
    isbn = models.CharField(max_length=17)

    def __str__(self):
        return f"{self.isbn} {self.title}"
