from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Project(models.Model):
    ProjectID = models.AutoField(primary_key=True)
    ProjectName = models.CharField(max_length=45)
    ProjectZip = models.IntegerField()
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


class Item(models.Model):
    ItemID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=45)
    Description = models.TextField()
    InStock = models.IntegerField()
    ARV = models.DecimalField(decimal_places=2, max_digits=12)
    Weight = models.DecimalField(null=True, decimal_places=2, max_digits=12)
    Image = models.TextField()  # null? look up image field stuff idk

    def __str__(self):
        return self.Name


class ProjectMaterials(models.Model):
    QuantityNeeded = models.IntegerField()
    QuantityAcquired = models.IntegerField()
    ProjectID = models.ForeignKey('Project', on_delete=models.CASCADE)  # many to many relationship how to handle????
    ItemID = models.ForeignKey('Item', on_delete=models.CASCADE)

    def __str__(self):
        return self.ItemID.Name


class Donor(models.Model):
    DonorID = models.AutoField(primary_key=True)
    DonorName = models.CharField(max_length=45)
    DonorUserName = models.CharField(max_length=45)
    DonorPassword = models.CharField(max_length=45)
    Business = models.BinaryField


class Donation(models.Model):
    Quantity = models.IntegerField()
    ARV = models.DecimalField(null=True, decimal_places=2, max_digits=12)
    ItemID = models.ForeignKey('Item', on_delete=models.CASCADE)
    DonorID = models.ForeignKey('Donor', on_delete=models.CASCADE)

    def __str__(self):
        return self.DonorID.DonorName + ' ' + self.ItemID.Name


