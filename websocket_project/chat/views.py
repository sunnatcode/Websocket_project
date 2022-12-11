from django.shortcuts import render

# Create your views here.


def Watsapp(request):
    return render(request, 'chat/chat.html')