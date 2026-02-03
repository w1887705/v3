from django.contrib import admin
from django.urls import path, include
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Custom logout: redirects back to login with a message
    path('accounts/logout/', core_views.logout_view, name='logout'),

    # Django's built-in auth pages (login, password reset, etc.)
    path('accounts/', include('django.contrib.auth.urls')),

    path('', include('core.urls')),
    path('ribbon/', include('ribbongame.urls')),
]
