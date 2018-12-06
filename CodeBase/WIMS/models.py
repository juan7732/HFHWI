from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Project(models.Model):
    ProjectID = models.AutoField(primary_key=True)
    ProjectName = models.CharField(max_length=45)
    ProjectZip = models.IntegerField()
    ProjectState = models.IntegerField()
    DateProposed = models.DateField(null=True)
    DateAccepted = models.DateField(null=True, blank=True, default=None)
    DateCompleted = models.DateField(null=True, blank=True, default=None)
    ProjectLocation = models.TextField()
    ProjectDescription = models.TextField(null=False)

    def __str__(self):
        return self.ProjectName


class ProjectMembers(models.Model):
    ProjectLead = models.BinaryField()
    ProjectID = models.ForeignKey('Project', on_delete=models.CASCADE)
    UserId = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.UserId.username


class Item(models.Model):
    ItemID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=45)
    Description = models.TextField()
    Category = models.CharField(max_length=50)
    InStock = models.IntegerField()
    ARV = models.DecimalField(decimal_places=2, max_digits=12)
    BinLocation = models.IntegerField

    def __str__(self):
        return self.Name


class ProjectMaterials(models.Model):
    QuantityNeeded = models.IntegerField()
    QuantityAcquired = models.IntegerField()
    ProjectID = models.ForeignKey('Project', on_delete=models.CASCADE)  # many to many relationship how to handle????
    ItemID = models.ForeignKey('Item', on_delete=models.CASCADE)

    def __str__(self):
        return self.ItemID.Name


class Donation(models.Model):
    Quantity = models.IntegerField()
    ItemID = models.ForeignKey('Item', on_delete=models.CASCADE)
    DonorID = models.ForeignKey(User, on_delete=models.CASCADE)
    DonationDate = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.DonorID.username + ' ' + self.ItemID.Name


