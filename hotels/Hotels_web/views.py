from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from .models import User, Hotel, Room, Booking, Feedback, Services

def index(request):
    return render(request, 'hotels/index.html', {
        "rooms": Room.objects.all()
    })

def sign_up(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "hotels/index.html", {
                "message": "Passwords must match.",
                "rooms": Room.objects.all()
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "hotels/index.html", {
                "message": "Username already taken.",
                "rooms": Room.objects.all()
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "hotels/index.html", {
                "message": "Invalid username and/or password.",
                "rooms": Room.objects.all()
            })

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def search(request):
    if request.method == "POST":
        place = request.POST.get("place")
        checkin = request.POST.get("checkin")
        checkout = request.POST.get("checkout")
        order = request.POST.get("order")
        price = request.POST.get("price")
        rating = request.POST.get("rating")
        rooms = Room.objects.all()
        if place:
            city,country = place.split(',')
            rooms = rooms.filter(hotel__city=city, hotel__country=country.strip())
        if checkin:
            rooms = rooms.filter(start_date__lte=checkin, end_date__gt=checkin)
        if checkout:
            rooms = rooms.filter(start_date__lt=checkout, end_date__gte=checkout)
        if order!='0':
            if order == '1':
                rooms = rooms.order_by('price')
            if order == '2':
                rooms = rooms.order_by('-price')
            if order == '3':
                rooms = rooms.order_by('rating')
            if order == '4':
                rooms = rooms.order_by('-rating')
        if price!='0':
            rooms = rooms.filter(price__lte= int(price)*50, price__gte= ((int(price)-1)*50)+1)
        return render(request, "hotels/index.html", {
            "rooms": rooms
        }) 

def room(request, room_id):
    room = Room.objects.get(pk=room_id)
    return render(request, "hotels/room.html", {
        "room": room
    })                   

def hotels(request):
    return render(request, "hotels/hotels.html", {
        "hotels": Hotel.objects.all()
    })