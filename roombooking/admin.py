from django.contrib import admin
from .models import Room, Booking, About, Review


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):

    list_display = ("title", "content")
    search_fields = ["title", "content"]

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ("user", "room", "check_in", "check_out")
    search_fields = ["user", "room", "check_in", "check_out"]

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "number",
        "slug",
        "features",
    )
    search_fields = ["title", "number"]
    prepopulated_fields = {"slug": ("title", "number")}
    list_filter = ("title", )

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = ("user", "room", "rating", "review","created_at")
    search_fields = ["user", "room", "rating", "created_at"]
