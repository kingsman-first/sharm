from django.shortcuts import render

def index(request):
    """This is a home page for calendar site"""
    return render(request, 'sharm_main/calendar.html')

def services(request):
    """This is a page for services"""
    return render(request, 'sharm_main/services.html')
