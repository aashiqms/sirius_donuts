from django.contrib import admin
from django.urls import path, include
from . views import HomePageView
from strawberry import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('order/', views.order, name='order')


]
