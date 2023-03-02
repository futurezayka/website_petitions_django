from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name = "home"),
    # path('second/', , name = "second_link"),
    # path('third/', views.about_us, name = "third_link"),
    path('about/', views.about_us, name = "about"),
]