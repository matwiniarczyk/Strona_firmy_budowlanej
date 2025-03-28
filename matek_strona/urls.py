"""
URL configuration for mate_strona project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from website_app import views
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from matek_strona import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view, name='home'),
    path('cost_estimate/', views.cost_estimate_view, name='cost_estimate'),
    path('contact/', views.contact_view, name='contact'),
    path('form_sent/', views.form_sent_view, name='form_sent'),
    path('FAQ/', views.faq_view, name='FAQ'),
    path('projects_galery/', views.projects_galery_view, name='projects_galery'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
