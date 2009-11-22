from django.contrib import admin
import tutoring.models

admin.site.register(tutoring.models.Subject)
admin.site.register(tutoring.models.Course)
admin.site.register(tutoring.models.CourseListing)
