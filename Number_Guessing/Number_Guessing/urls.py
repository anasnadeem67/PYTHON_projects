from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Main_App/', include('Main_App.urls')),  # assuming Main_App has its own urls.py
    path('', RedirectView.as_view(url='/Main_App/')),  # Redirect root URL to Main_App
]
