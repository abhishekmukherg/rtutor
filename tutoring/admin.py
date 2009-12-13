# Copyright (C) 2009 Abhishek Mukherjee <abhishek.mukher.g@gmail.com>
#
# This file is part of rtutor.
#
# rtutor is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# rtutor is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with rtutor.  If not, see <http://www.gnu.org/licenses/>.

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
