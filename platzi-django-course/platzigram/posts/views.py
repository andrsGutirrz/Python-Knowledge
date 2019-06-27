"""
    post views
"""

from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

post = [
    {'title': 'Mont Blanc',
     'user': {
         'name': 'Melissa Cardenas',
         'picture': 'http://picsum.photos/60/60/?image=1027'
     },
     'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
     'photo': 'http://picsum.photos/800/600/?image=1036'
     },
    {'title': 'Via lactea',
     'user': {
         'name': 'Andres Gutierrez',
         'picture': 'http://picsum.photos/60/60/?image=1005'
     },
     'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
     'photo': 'http://picsum.photos/800/600/?image=903'
     },
    {'title': 'Nuevo Auditorio',
     'user': {
         'name': 'Freddy Vega',
         'picture': 'http://picsum.photos/60/60/?image=883'
     },
     'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
     'photo': 'http://picsum.photos/800/600/?image=999'
     },
    {'title': 'Random',
     'user': {
         'name': 'Random',
         'picture': 'http://picsum.photos/60/60/?image=1020'
     },
     'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
     'photo': 'http://picsum.photos/500/700/?image=1076'
     },
]


def list_post(request):
    """List all post"""
    return render(request, 'feed.html', {'posts': post})

