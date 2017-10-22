from django.db import models


class Users(models.Model):
    userName = models.CharField(max_length=20, primary_key=True)
    userId = models.IntegerField()
    def __str__(self):
        return self.userName


