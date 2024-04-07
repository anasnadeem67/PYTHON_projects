# from django.urls import path 
# from . import views
# from django.conf import settings
# from django.conf.urls.static import static

# #urlConfig
# urlpatterns = [
#     path("index/", views.guess_number, name="")
# ]
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



from django.urls import path
from . import views  # Import the views module

urlpatterns = [
    path('', views.guess_number, name='guess_number'),  # Use views.guess_number instead of guess_number
    path('restart/', views.restart_game, name='restart_game'),  # Use views.restart_game instead of restart_game
    path('contact/', views.contact, name='contact'),
    path('aboutus/', views.aboutus, name='aboutus')
]
