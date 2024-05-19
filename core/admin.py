from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('date_time', 'customer_name', 'service_type')
    list_filter = ('date_time', 'service_type')
    search_fields = ('customer_name',)
