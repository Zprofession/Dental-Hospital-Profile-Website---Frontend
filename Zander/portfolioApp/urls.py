from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Admin Panel Title
admin.site.site_header="Boston Dental"
admin.site.site_title="Boston Dental Admin "

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    
    #cdeditor
    path('ckeditor',include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
