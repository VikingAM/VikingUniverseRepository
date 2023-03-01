from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.accountIndex, name='accountIndex'),
    path('login', views.accountLogin, name='accountLogin'),
    path('logout', views.accountLogout, name="accountLogout"),
    path('create', views.accountCreate, name='accountCreate'),
    path('verification/<verification_id>', views.accountVerificationPage, name="accountVerificationPage"),
    path('verify/<verification_id>', views.accountVerfiy, name="accountVerify",),
    path('resend_verification', views.resendVerification, name="resendVerification"),
    path('email_verfication_template', views.email_verfication_template, name="email_verfication_template"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)