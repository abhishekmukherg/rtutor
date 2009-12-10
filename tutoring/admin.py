"""
Admin settings
"""

from django.contrib import admin
import tutoring.models


__all__ = ['CourseAdmin']


class CourseListingInline(admin.TabularInline):

    """Settings for inlining course listings"""

    model = tutoring.models.CourseListing


class CourseAdmin(admin.ModelAdmin):

    """Settings for displaying Course's in admin"""

    inlines = [
        CourseListingInline,
    ]


admin.site.register(tutoring.models.Subject)
admin.site.register(tutoring.models.Course, CourseAdmin)
admin.site.register(tutoring.models.HelpRequest)
