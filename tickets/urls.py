from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('portal_tickets', views.ticketingPage, name="ticketingPage"),
    path('add_ticket', views.Addticket, name='Addticket'),

    path('task_dashboard', views.taskDashboard, name="taskDashboard"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)