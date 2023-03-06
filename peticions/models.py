from django.db import models

from mainapp.models import User


# Create your models here.

class Peticions(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Name', max_length=50)
    text = models.TextField('Text')
    date = models.DateTimeField(auto_now=True)
    name_surname = models.TextField("name_surname")
    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return f"/petitions/{self.id}"

    class Meta:
        verbose_name = "Petition"
        verbose_name_plural = "Petitions"

