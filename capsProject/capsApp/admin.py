from django.contrib import admin
from .models import *

class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'license_no', 'plate_number', 'user_id', 'violation_details', 'fine_amount', 'issued_by', 'status', 'created_at', 'due_date']

# Register the Ticket model with the custom admin configuration
admin.site.register(Ticket, TicketAdmin)

# Register other models without any custom configuration
admin.site.register(User)
admin.site.register(Payment)
admin.site.register(Dispute)
admin.site.register(Violation)

