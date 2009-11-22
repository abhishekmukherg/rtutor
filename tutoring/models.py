from django.contrib import admin
from django.db import models

SEMESTER_CHOICES = (
        ('FA', 'Fall'),
        ('SP', 'Spring'),
        ('SU', 'Summer'),
)

class Subject(models.Model):
    code = models.CharField(
            max_length=4,
            primary_key=True,
            help_text="Example: CSCI",
            )
    name = models.CharField(
            max_length=255,
            unique=True,
            help_text="Example: Computer Science",
            )

    def __unicode__(self):
        return unicode(self.name)

class Course(models.Model):
    title = models.CharField(
            max_length=255,
            help_text="Example: Introduction to Biology",
            unique=True
            )

    def __unicode__(self):
        return unicode(self.title)

class CourseListing(models.Model):
    '''The actual course numbering, i.e. CSCI-1100'''
    subject = models.ForeignKey(Subject)
    course = models.ForeignKey(Course)
    course_code = models.PositiveIntegerField()
    semester = models.CharField(max_length=2, choices=SEMESTER_CHOICES)

    def __unicode__(self):
        return u"%s-%d: %s" % (
                self.subject.code,
                self.course_code,
                self.course
                )

    class Meta:
        unique_together = (('subject', 'course_code', 'semester'))

