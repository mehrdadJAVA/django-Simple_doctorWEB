from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from doctor.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('doctor/home',Home_View),
    path('doctor/visit',Visit_View),
    path('doctor/visit_OK',Visit_View),
    path('doctor/doctorDetail',Doctor_Del_View),
    path('doctor/search',Doctor_SRECH_View),
    path('doctor/about',About),

        
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #not both
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
