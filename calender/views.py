from django.shortcuts import render

def index(request):
    """This is a home page for calendar site"""
    return render(request, 'sharm_main/calendar.html')