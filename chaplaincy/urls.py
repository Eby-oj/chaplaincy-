"""chaplaincy URL Configuration

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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Account import views as acctviews
from categories import views as catviews
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',acctviews.index , name ='index' ),
    path('login',acctviews.login , name ='login' ),
    path('signup',acctviews.signup , name ='signup' ),
    path('text',catviews.text , name ='text' ),
    path('searchbar', catviews.searchbar , name = 'searchbar'),
    path('prayer', catviews.prayer , name ='prayer'),
    path('knowledge',catviews.knowledge, name ='knowledge'),
    path('healing', catviews.healing, name='healing'),
    path('marriage', catviews.marriage, name='marriage'),
    path('novels', catviews.novels, name='novels'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
