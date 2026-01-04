from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    """Homepage - shows navigation to all sections"""
    context = {
        'user': request.user,
        'is_admin': request.user.is_superuser,
    }
    return render(request, 'home.html', context)