"""
Models for tutoring
"""


import django.contrib.auth.models
from django.db import models
from django.db import IntegrityError
from django.utils.translation import ugettext as _


__all__ = [
        'Subject',
        'SEMESTER_CHOICES',
        'Course',
        'CourseListing',
        'HelpRequest',
]


SEMESTER_CHOICES = (
        ('FA', _('Fall')),
        ('SP', _('Spring')),
        ('SU', _('Summer')),
)


class Subject(models.Model):

    """
    A school subject. excample: Engineering
    """

    code = models.CharField(
            max_length=4,
            primary_key=True,
            help_text=_("Example: CSCI"),
            )

    name = models.CharField(
            max_length=255,
            unique=True,
            help_text=_("Example: Computer Science"),
            )

    objects = models.Manager()

    def __unicode__(self):
        return unicode(self.name)


class Course(models.Model):

    """
    A course itself. Like Introduction to Computer Science
    """

    title = models.CharField(
            max_length=255,
            help_text=_("Example: Introduction to Biology"),
            unique=True
            )

    objects = models.Manager()

    def __unicode__(self):
        return unicode(self.title)


class CourseListing(models.Model):

    """
    The actual course numbering, i.e. CSCI-1100
    """

    subject = models.ForeignKey(Subject)
    course = models.ForeignKey(Course)
    course_code = models.PositiveIntegerField()
    semester = models.CharField(max_length=2, choices=SEMESTER_CHOICES)
    year = models.PositiveSmallIntegerField()

    objects = models.Manager()

    def __unicode__(self):
        return u"%s-%d: %s" % (
                self.subject.code,
                self.course_code,
                self.course
                )

    class Meta:
        unique_together = (('subject', 'course_code', 'semester', 'year'))


class HelpRequest(models.Model):

    """
    A request for help by a student. can be fulfilled by a teacher
    """

    course_listing = models.ForeignKey(CourseListing)
    date_created = models.DateTimeField(auto_now_add=True)
    date_taken = models.DateTimeField(
            null=True,
            blank=True
            )
    student = models.ForeignKey(django.contrib.auth.models.User,
            related_name='help_requests')
    teacher = models.ForeignKey(django.contrib.auth.models.User,
            related_name='replied_requests',
            null=True,
            blank=True,
            )

    objects = models.Manager()

    def save(self, force_insert=False, force_update=False):
        """Disallows saving when student = teacher

        *args and **kwargs are passed directly to the super's save
        """
        if self.student == self.teacher:
            raise IntegrityError
        return super(HelpRequest, self).save(
                force_insert=force_insert,
                force_update=force_update
                )

    def __unicode__(self):
        out = _(u"%s asking for help on %s") % \
                (self.student, self.course_listing)
        if self.teacher is not None:
            out += u" (taken by %s)" % self.teacher
        return out
