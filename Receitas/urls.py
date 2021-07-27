from django.urls import path
from . import views
from django.urls import path

urlpatterns = [
    		path('', views.index, name='index'),
			path('<int:receita_id>', views.receita, name='receita'),
			path('busca', views.buscar, name='buscar')
	]
