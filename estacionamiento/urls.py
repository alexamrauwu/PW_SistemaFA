from django.urls import path
from . import views
#from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('mostrarAu', views.mostrarAu, name='mostrarAu'),
    #path('mostrar', views.mostrar, name='mostrar' ),
    path('re_autos', views.re_autos, name='re_autos' ),
    path('re_persona', views.re_persona, name='re_persona' ),
    path('registro', views.registro, name='registro' ),

] 