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
    path('get_ticket_comments', views.getTicketComments, name="getTicketComments"),
    path('get_ticket_list', views.getTicketList, name="getTicketList"),


    path("update_ticket_title", views.updateTicketTitle, name="updateTicketTitle"),
    path("update_ticket_status", views.updateTicketStatus, name="updateTicketStatus"),
    path("update_ticket_percentage", views.UpdateTicketPercentage, name="UpdateTicketPercentage"),
    path("update_ticket_description", views.UpdateTicketDescription, name="UpdateTicketDescription"),
    path("add_ticket_responder", views.AddTicketResponder, name="AddTicketResponder"),


    path("get_task_comments", views.getTaskComments, name="getTaskComments"),

    
    path('task_dashboard', views.taskDashboard, name="taskDashboard"),
    path('task_submit', views.taskSubmit, name="taskSubmit"),
    path('create_task', views.createTask, name="createTask"),
    path("add_task_responder", views.AddTaskResponder, name="AddTaskResponder"),
    
    path('add_revision', views.addRevision, name="addRevision"),
    path('task_approve', views.taskApprove, name="taskApprove"),
    path('get_ticket_filter', views.getTciketByFilter, name="getTciketByFilter"),
    
    path('task_details/<task_id>', views.taskDetails, name="taskDetails"),
    path('edit_task/<task_id>', views.editTask, name="editTask"),
    path('remove_task_attachment', views.removeTaskAttachment, name="removeTaskAttachment"),
    path('post_task_comment/<task_id>', views.postTaskComment, name="postTaskComment"),

    path('update_task_status', views.UpdateTaskStatus, name="UpdateTaskStatus"),
    path('update_task_percentage', views.updateTaskPercentage, name='updateTaskPercentage'),

    path("update_category_theme", views.UpdateCategoryTheme, name="UpdateCategoryTheme"),
    path('update_category_assistance', views.UpdateCategoryAssistance, name="UpdateCategoryAssistance"),
    path('update_category_features', views.UpdateCategoryFeatures, name="UpdateCategoryFeatures"),

    path("update_category", views.UpdateCategory, name="UpdateCategory"),
    path("update_sub_category", views.UpdateSubCategory, name="UpdateSubCategory"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)