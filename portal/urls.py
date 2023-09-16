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
    path('settings_faqs', views.SettingFaqsPage, name="SettingFaqsPage"),

    path('admin', views.portalAdminDashboard, name="portalAdminDashboard"),
    
    path('admin/tickets', views.portalAdminTicketDashboard, name="portalAdminTicketDashboard"),
    path('admin/tickets_list', views.portalAdminTicketList, name="portalAdminTicketList"),
    path('admin/tickets_detailed/<ticket_id>', views.getAdminTicketDetails, name="getAdminTicketDetails"),

    path('admin/tasks', views.portalAdminTaskDashboard, name="portalAdminTaskDashboard"),
    path('admin/tasks_list', views.portalAdminTaskList, name="portalAdminTaskList"),
    path('admin/task_detailed/<task_id>', views.portalAdmintaskDetails, name="portalAdmintaskDetails"),

    path('admin/services', views.portalAdminServicesDashboard, name="portalAdminServicesDashboard"),
    path('admin/services_list', views.portalAdminServicesList, name="portalAdminServicesList"),
    path('admin/services_theme_detail/<category_theme_id>', views.portalAdminServiceThemeDetail, name="portalAdminServiceThemeDetail"),
    path('admin/services_category_detail/<category_id>', views.portalAdminServiceCategoryDetail, name="portalAdminServiceCategoryDetail"),

    
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)