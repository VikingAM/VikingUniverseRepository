from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.accountIndex, name='accountIndex'),
    path('login', views.accountLogin, name='accountLogin'),
    path('logout', views.accountLogout, name="accountLogout"),
    path('create', views.accountCreate, name='accountCreate'),

    # verify emails
    path('verification/<verification_id>', views.accountVerificationPage, name="accountVerificationPage"),
    path('verify/<verification_id>', views.accountVerfiy, name="accountVerify",),
    path('resend_verification', views.resendVerification, name="resendVerification"),
  
    # password reset 
    path('sent_password_reset_otp', views.passwordResetOtp, name="passwordResetOtp"),
    path('change_password', views.changePassword, name="changePassword"),

    # for password management
    path('profile_new_password', views.profileNewPassword, name='profileNewPassword'),
    path('profile_new_password_getById', views.ProfileNewPasswordGetById, name='ProfileNewPasswordGetById'),
    path('profile_update_password', views.ProfileUpdatePassword, name='ProfileUpdatePassword'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)