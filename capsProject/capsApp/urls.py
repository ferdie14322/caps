from django.urls import path
from . import views
from .views import UserProfileAPIView
from .views import UserDisputesAPIView

police_patterns = [
    # Police/Driver APIs
    path('api/signup/', views.SignupAPIView.as_view(), name='signup'),
    path('api/login/', views.LoginAPIView.as_view(), name='login'),
    path('api/logout/', views.LogoutAPIView.as_view(), name='logout'),
    path('api/dashboard/', views.DashboardAPIView.as_view(), name='dashboard'),
    path('api/addticket/', views.add_ticket, name='add_ticket'),
    path('api/tickets/search/', views.search_tickets, name='ticket-search'),
    path('api/process-payment/', views.process_payment, name='process_payment'),
    path('api/file-dispute/', views.file_dispute, name='file_dispute'),
    path('api/get_violations/', views.get_violations, name='get_violations'),
    path('api/get_drivers/', views.get_drivers, name='get_drivers'),
    path('api/get_ticketsByPoliceCounts/<int:user_id>/', views.get_ticketsByPoliceCounts, name='get_ticketsByPoliceCounts'),
    path('api/get_recent_activity/<int:user_id>/', views.get_recent_activity, name='get_recent_activity'),
    path('api/user_profile/<int:user_id>/', UserProfileAPIView.as_view(), name='user_profile'),
    path('api/active_tickets/<int:user_id>/', views.get_active_tickets, name='get_active_tickets'),       
    path('api/submit_dispute/', views.submit_dispute, name='submit_dispute'),
    path('api/disputes/<int:user_id>/', UserDisputesAPIView.as_view(), name='user-disputes'),
    ]

admin_patterns = [
    path('admin/register/', views.admin_register, name='admin_register'),
    path('', views.admin_login, name='admin_login'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin/dashboard/logout/', views.admin_logout, name='admin_logout'),
    path('admin/disputes/', views.admin_disputes, name='admin_disputes'), 
    path('admin/payments/', views.admin_payments, name='admin_payments'), 
    path('admin/tickets/', views.admin_tickets, name='admin_tickets'), 
    path('admin/violations/', views.admin_violations, name='admin_violations'),
    path('admin/search/', views.admin_search, name='admin_search'), 
    ]

violation_patterns = [
    path('add_violation/', views.add_violation, name='add_violation'),
    path('edit_violation/<int:id>/', views.edit_violation, name='edit_violation'),
    path('delete_violation/<int:id>/', views.delete_violation, name='delete_violation'),
    ]

urlpatterns = police_patterns + admin_patterns + violation_patterns
