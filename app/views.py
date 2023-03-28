"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def game1(request):
    """Renders the games page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/game1.html',
        {
            'title':'Game1',
            'message':'Your Games description page.',
            'year':datetime.now().year,
        }
    )

def game2(request):
    """Renders the games page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/game2.html',
        {
            'title':'Game2',
            'message':'Your Games description page.',
            'year':datetime.now().year,
        }
    )

def game3(request):
    """Renders the games page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/game3.html',
        {
            'title':'Game3',
            'message':'Your Games description page.',
            'year':datetime.now().year,
        }
    )

def game4(request):
    """Renders the games page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/game4.html',
        {
            'title':'Game4',
            'message':'Your Games description page.',
            'year':datetime.now().year,
        }
    )