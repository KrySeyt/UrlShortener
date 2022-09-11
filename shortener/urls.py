from django.urls import path

from . import views


urlpatterns = [
    path('main', views.main_page, name='main-page'),
    path('add-url', views.add_url, name='add-url'),
    path('<str:short_url_key>', views.redirect_to_origin, name='redirect-to-origin'),
]
