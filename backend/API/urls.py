"""
URL configuration for TEST project.

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
from django.urls import  re_path
from django.conf.urls.static import static
from django.conf import settings

from API import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    re_path("login/user", views.login),
    re_path("signup/user", views.signup),
    re_path("health", views.test),
    re_path("test_token_health", views.test),
    re_path("login/dev", views.login_vendor),
    re_path("signup/dev", views.signup_vendor),
    re_path("describe", views.describe),
    re_path("translate", views.translate),
    re_path("asl", views.asl),
    # re_path("transcribe", views.transcribe),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)