from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
@login_required
def ribbon_game(request):
    return render(request, 'ribbongame/ribbon_game.html')
