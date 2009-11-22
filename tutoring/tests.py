from django.test import TestCase
from django.db import IntegrityError

import tutoring.models

class SubjectTest(TestCase):

    def setUp(self):
        tutoring.models.Subject.objects.create(
                code='CSCI',
                name='Computer Science',
                )

    def test_unique_code(self):
        self.assertRaises(IntegrityError,
            tutoring.models.Subject.objects.create,
            code='CSCI',
            name='foo',
        )

    def test_unique_name(self):
        self.assertRaises(IntegrityError,
                tutoring.models.Subject.objects.create,
                code='FOOO',
                name='Computer Science',
            )

class CourseTest(TestCase):

    def setUp(self):
        tutoring.models.Course.objects.create(
                title='Computer Science I',
                )

    def test_unique_title(self):
        self.assertRaises(IntegrityError,
            tutoring.models.Course.objects.create,
            title='Computer Science I',
        )

class CourseListingTest(TestCase):

    def setUp(self):
        self.csci = tutoring.models.Subject.objects.create(
                code='CSCI',
                name='Computer Science',
                )
        self.itec = tutoring.models.Subject.objects.create(
                code='ITEC',
                name='IT stuff',
                )
        self.cs1 = tutoring.models.Course.objects.create(
                title='Computer Science I',
                )
        self.cl = tutoring.models.CourseListing.objects.create(
                subject=self.csci,
                course=self.cs1,
                course_code=1100,
                semester='FA'
                )

    def test_non_unique_code(self):
        cs2 = tutoring.models.Course.objects.create(
                title='Computer Science 2',
                )
        self.assertRaises(IntegrityError,
                tutoring.models.CourseListing.objects.create,
                subject=self.cl.subject,
                course=cs2,
                course_code=self.cl.course_code,
                semester=self.cl.semester,
        )

    def test_allow_new_semester(self):
        tutoring.models.CourseListing.objects.create(
                subject=self.cl.subject,
                course=self.cl.course,
                course_code=self.cl.course_code,
                semester='SP',
        )

    def test_allow_new_code(self):
        tutoring.models.CourseListing.objects.create(
                subject=self.cl.subject,
                course=self.cl.course,
                course_code=1200,
                semester=self.cl.semester,
        )

    def test_allow_new_subject(self):
        tutoring.models.CourseListing.objects.create(
                subject=self.itec,
                course=self.cl.course,
                course_code=self.cl.course_code,
                semester=self.cl.semester,
        )



