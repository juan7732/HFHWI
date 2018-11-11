from django.db import models

# Create your models here.


class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    Phone = models.CharField(max_length=45)
    ZipCode = models.IntegerField()
    DateJoined = models.DateTimeField()

    def __str__(self):
        return self.FirstName + ' ' + self.LastName
