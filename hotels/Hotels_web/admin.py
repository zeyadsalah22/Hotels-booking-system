from django.contrib import admin
from .models import User, Hotel, Room, Booking, Feedback, Services

admin.site.register(User)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Feedback)
admin.site.register(Services)
