from django.urls import path

from . import views

urlpatterns = [
	path('supervisors', views.supervisors, name='supervisors'),
	path('submit', views.submit, name='submit'),
]
