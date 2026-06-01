from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from .models import Chat

def index(request):
    if request.method == 'POST':
        room = request.POST['room']
        
        # Check if the room already exists
        get_room = Chat.objects.filter(room_name=room).first()
        
        if get_room:
            # Check the number of users currently allowed/in the room
            number = get_room.allowed_users
            
            if int(number) < 2:
                # Update user count or update logic here if needed
                return redirect(f'/video/{room}/join/')
            else:
                # Room is full
                return render(request, 'index.html', {'error': 'Room is full'})
        else:
            # Create a new room if it does not exist
            create = Chat.objects.create(room_name=room, allowed_users=1)
            if create:
                return redirect(f'/video/{room}/created/')
                
    return render(request, 'index.html')

def video(request,room,created):
    return render(request,'video.html',{
        'created':created,
        'room':room
    })