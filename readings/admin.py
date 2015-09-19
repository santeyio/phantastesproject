from django.contrib import admin

from .models import Book, Day

class DayInline(admin.TabularInline):
	model = Day
	extra = 1

class BookAdmin(admin.ModelAdmin):
	inlines = [DayInline]


admin.site.register(Book, BookAdmin)
