from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('portal_tickets', views.ticketingPage, name="ticketingPage"),
    path('add_ticket', views.Addticket, name='Addticket'),
    path('get_ticket_details', views.getTicketDetails, name="getTicketDetails"),
    path('get_category_services', views.getCategoryServices, name='getCategoryServices'),
    path('get_category_details', views.getCategoryDetailsById, name='getCategoryDetailsById'),

    path('task_dashboard', views.taskDashboard, name="taskDashboard"),
    path('task_submit', views.taskSubmit, name="taskSubmit"),
    path('create_task', views.createTask, name="createTask"),
    path('edit_task', views.editTask, name="editTask"),
    path('add_revision', views.addRevision, name="addRevision"),
    path('task_approve', views.taskApprove, name="taskApprove"),
    path('get_ticket_filter', views.getTciketByFilter, name="getTciketByFilter"),
    path('task_details/<task_id>', views.taskDetails, name="taskDetails"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)