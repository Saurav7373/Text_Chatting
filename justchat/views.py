from django.shortcuts import render
def index(request):
    return render(request, 'justchat/index.html', {})

def room(request, room_name):
    return render(request, 'justchat/room.html', {
        'room_name': room_name
    })