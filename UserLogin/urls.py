"""UserLogin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
from LoginPage import views
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Login.as_view(),name = 'Registration'),
    path('',include("allauth.urls")),
    path('registration/',views.update_profile,name = 'reg'),
    path('doctor/',views.TriggerFill.as_view(), name = "trigger"),
    path('patient/',views.ViewAssignments.as_view(), name = "patient"),
    # path('registration/',views.RegistrationApi.as_view(),name = 'reg'),
    # path('accounts/',include("social_django.urls",namespace='social')),
    # path('registration/',login_required(views.Registration.as_view()),name = 'Registration'),
]
