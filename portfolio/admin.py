
from django.contrib import admin
from .models import Project, ContactMessage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "technologies",
        "created_at",
    )
    search_fields = ("title", "description", "technologies")
    list_filter = ("created_at",)
    readonly_fields = ("created_at",)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    search_fields = ("name", "email", "subject")
    list_filter = ("created_at",)
    readonly_fields = ("created_at",)
