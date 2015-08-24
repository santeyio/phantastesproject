from django.contrib import admin

from .models import Schedule, Day

class DayInline(admin.TabularInline):
	model = Day
	extra = 1

class ScheduleAdmin(admin.ModelAdmin):
	inlines = [DayInline]


admin.site.register(Schedule, ScheduleAdmin)
