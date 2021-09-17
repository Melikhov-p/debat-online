from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('', HomeDebat.as_view(), name='main'),
    path('offer_theme/', offer_theme, name='offer_theme'),
    path('startdebat/', StartDebat.as_view(), name='startdebat'),
    path('theme/<int:theme_id>/', DebatByTheme.as_view(), name='theme'),
    path('debat/<int:debat_id>', DebatPage.as_view(), name='debat_page'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('all_themes/', all_themes, name='all_themes'),
    path('delete_debat/<int:debat_id>', delete_debat, name='delete_debat'),
    path('add_opponent/<int:debat_id>', add_opponent, name='add_opponent'),
]