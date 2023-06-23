from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('checkout', views.paymentCheckout, name='paymentCheckout'),
    path('success', views.paymentSuccess, name="paymentSuccess"),
    path('cancel', views.paymentCancel, name="paymentCancel"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)