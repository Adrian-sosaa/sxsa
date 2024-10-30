from django.urls import path
from camiones_app import views
urlpatterns = [
    path("",views.listadobalones,name="listadobalones")
]