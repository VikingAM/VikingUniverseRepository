from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('portal_tickets', views.ticketingPage, name="ticketingPage"),
    path('add_ticket', views.Addticket, name='Addticket'),
    path('get_category_services', views.getCategoryServices, name='getCategoryServices'),

    path('task_dashboard', views.taskDashboard, name="taskDashboard"),
    path('task_submit', views.taskSubmit, name="taskSubmit"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)