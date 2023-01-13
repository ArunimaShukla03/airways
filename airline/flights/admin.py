from django.contrib import admin
from .models import Flight, Airport, Passenger

# Register your models here.
class FlightAdmin(admin.ModelAdmin):
    # this is done to let us decide how flight admin looks like
    list_display = ("id","origin", "destination", "duration")

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin) # this is to view as the flight admin settings that we just set in "FlightAdmin" class.
admin.site.register(Passenger, PassengerAdmin)
