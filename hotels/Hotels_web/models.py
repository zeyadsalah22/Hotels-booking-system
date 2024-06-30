from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
import uuid

class User(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='hotels_users')
    user_permissions = models.ManyToManyField(Permission, related_name='hotels_users')
    def __str__(self):
        return f"Username: {self.username}"
    
class Hotel(models.Model):
    name = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField(upload_to='hotels\images')
    HMID =  models.CharField(max_length=36, default=uuid.uuid4)
    def __str__(self):
        return f"{self.name} in {self.city}, {self.country}"

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms')
    image = models.ImageField(upload_to='hotels\images')
    description = models.TextField(default="No description")
    room_type = models.CharField(max_length=64)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.room_type} in {self.hotel.name} for {self.price} per night"
    
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    check_in = models.DateField()
    check_out = models.DateField()
    def __str__(self):
        return f"{self.user.username} booked {self.room.room_type} in {self.room.hotel.name} from {self.check_in} to {self.check_out}"
    
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedbacks')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='feedbacks')
    review = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    def __str__(self):
        return f"{self.user.username} feedback on {self.hotel.name}"
    
class Services(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='services')
    service_name = models.CharField(max_length=64)
    service_price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.service_name} in {self.hotel.name} for {self.service_price}"