"""
    post views
"""
import datetime

# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Forms
from posts.forms import PostForm

# Models
from posts.models import Post


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


@login_required
def list_post(request):
    """List all post"""
    #post = Post.objects.all().order_by('-created')
    return render(request, 'posts/feed.html', {'posts': post})


@login_required
def create_post(request):
    """Create new post view."""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')

    else:
        form = PostForm()

    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )