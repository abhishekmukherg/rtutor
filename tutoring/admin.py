from django.contrib import admin
import tutoring.models

class CourseListingInline(admin.TabularInline):
    model = tutoring.models.CourseListing

class CourseAdmin(admin.ModelAdmin):
    inlines = [
        CourseListingInline,
    ]

class CourseListingAdmin(admin.ModelAdmin):
    pass

admin.site.register(tutoring.models.Subject)
admin.site.register(tutoring.models.Course, CourseAdmin)
admin.site.register(tutoring.models.HelpRequest)
