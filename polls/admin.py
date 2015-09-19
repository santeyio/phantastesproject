from django.contrib import admin

from .models import Poll, Book, Vote

class BookInline(admin.TabularInline):
	model = Book
	extra = 1

class PollAdmin(admin.ModelAdmin):
	inlines = [BookInline]

admin.site.register(Poll, PollAdmin)
admin.site.register(Vote)

