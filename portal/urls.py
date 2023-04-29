from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.portalDashboard, name='portalDashboard'),
    path('setting',views.portalSettingPage, name='portalSettingPage'),
    path('setting_password', views.SettingPasswordPage, name="SettingPasswordPage"),
    path('setting_invoice', views.SettingInvoicePage, name="SettingInvoicePage"),
    path('setting_password_management', views.SettingPasswordManagementPage, name="SettingPasswordManagementPage"),
    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)