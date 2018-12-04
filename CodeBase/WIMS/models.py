from django.db import models

# Create your models here.


class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    Phone = models.CharField(max_length=45)
    ZipCode = models.IntegerField()
    DateJoined = models.DateField()

    def __str__(self):
        return self.FirstName + ' ' + self.LastName


class Admin(models.Model):
    UserID = models.ForeignKey('User', on_delete=models.CASCADE)
    ImpersonationID = models.IntegerField(null=True)


class Authentication(models.Model):
    UserId = models.ForeignKey('User', on_delete=models.CASCADE)
    UserName = models.CharField(primary_key=True, max_length=45)
    Password = models.TextField()
    LastLogin = models.DateTimeField()
    Instances = models.IntegerField()


class Project(models.Model):
    ProjectID = models.AutoField(primary_key=True)
    ProjectName = models.CharField(max_length=45)
    ProjectZip = models.IntegerField()
    DateProposed = models.DateField(null=True)
    DateAccepted = models.DateField(null=True)
    DateCompleted = models.DateField(null=True)
    ProjectLocation = models.TextField()
    ProjectDescription = models.TextField(null=True)


class ProjectMembers(models.Model):
    ProjectLead = models.BinaryField()
    ProjectID = models.ForeignKey('Project', on_delete=models.CASCADE)
    UserId = models.ForeignKey('User', on_delete=models.CASCADE)


class Item(models.Model):
    ItemID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=45)
    Description = models.TextField()
    InStock = models.IntegerField()
    ARV = models.DecimalField(decimal_places=2, max_digits=12)
    Weight = models.DecimalField(null=True, decimal_places=2, max_digits=12)
    Image = models.TextField()  # null? look up image field stuff idk


class ProjectMaterials(models.Model):
    QuantityNeeded = models.IntegerField()
    QuantityAcquired = models.IntegerField()
    ProjectID = models.ForeignKey('Project', on_delete=models.CASCADE)  # many to many relationship how to handle????
    ItemID = models.ForeignKey('Item', on_delete=models.CASCADE)


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


