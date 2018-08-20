from django.db import models


class Apptest(models.Model):
    Title = models.CharField('TITLE', max_length=50)
    Content = models.TextField('CONTENT')

    def __str__(self):
        return self.Title

# Create your models here.
