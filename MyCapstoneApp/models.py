from django.db import models


# Create your models here.
# Each class represents a table in our database.
# Each variable inside a class represents a field in our table.
# If you change the models in this file you will need to:
# Run python manage.py makemigrations to create migrations for those changes
# Run python manage.py migrate to apply those changes to the database.

class School(models.Model):
    name = models.CharField(max_length=200)
    abbr = models.CharField(max_length=5, unique=True)
    compclass = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class Athletes(models.Model):
    schoolid = models.ForeignKey(School, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname + ' ' + self.lastname


class Scoring(models.Model):
    place = models.IntegerField()
    points = models.IntegerField()

    def __str__(self):
        return self.place

class TeamScores(models.Model):
    schoolid = models.ForeignKey(School, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return self.score


class Events(models.Model):
    name = models.CharField(max_length=50)
    shortname = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class PrelimRaces(models.Model):
    athleteid = models.ForeignKey(Athletes, on_delete=models.CASCADE)
    eventid = models.ForeignKey(Events, on_delete=models.CASCADE)
    districttime = models.FloatField()
    districtplace = models.IntegerField()
    heat = models.IntegerField()

    def __str__(self):
        return self.eventid


class FinalRaces(models.Model):
    prelimid = models.ForeignKey(PrelimRaces, on_delete=models.CASCADE)
    athleteid = models.ForeignKey(Athletes, on_delete=models.CASCADE)
    prelimtime = models.FloatField()
    prelimplace = models.IntegerField()

    def __str__(self):
        return self.athleteid
