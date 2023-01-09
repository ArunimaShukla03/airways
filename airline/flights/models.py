from django.db import models

# Create your models here.

# Each model is a python class and it is like having one model for each of the main tables. Inside a model includes all the parameters or properties that a table has.

class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"


''' 

class Flight(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

'''

# But nothing here actually has modified the database the Django is using to store information about my web application.

# Thus we create a "migration" to let django go know the changes in the database. And then we migrate them to let django take those changes and apply them to the database.

# Using the command line "python manage.py makemigrations" and now in order to apply the migration, we use "python manage.py migrate". Now we have a SQLite file.

# Now in order to write what we are already familiar with, we can write "python manage.py shell" and write them instead of writing SQL queries.

# Now running a bunch of commands, such as "Flight.objects.all()" which shows all of the saved flights after importing the model by "from flights.models import Flight". 

# But this does not give me a clean set of all the flights, thus in order to do that, we use "def __str__(self):" and then returning the values which give me a proper structured flights information. This gives the string representation of this particular model or objects in python in general.

# Now we want to change our model as we have now created a new class and we need to relate these two classes.

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

# Here we have origin as foreign keys as they are replaced by cities and their codes after relating. We also have additional arguments like "on_delete=models.CASCADE" which basically means that when we have tables which are related to each other, SQL should have a way of knowing what should happen if you ever delete something.

# For example, what happens to a flight when the thing it is referencing gets deleted (an airport gets deleted), thus it also deletes any of the corresponding flights.

# "related_name" is a way of me accessing a relationship in a reverse order that we can get a flight's origin in an airport, but the reverse question here is if I have an airport, how do we get all of the flights that have that airport as the origin.

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank = True, related_name="passengers")

# These passengers have many to many relationship with flights, that a flight could have multiple passengers and a passenger could be on multiple flights. Thus we need additional tables to keep track of this.

# "blank = True" allows the passengers to have the possibility that they have no flights.

# We have related name as "passengers" meaning if I have a passenger, I can use its attribute to access all of their flights. And if we have a flight, then we can access all of their passengers.