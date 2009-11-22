from django.contrib.auth.models import User
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
                year=2009,
                semester='FA'
                )

    def test_unique(self):
        self.assertRaises(IntegrityError,
                tutoring.models.CourseListing.objects.create,
                subject=self.cl.subject,
                course=self.cl.course,
                course_code=self.cl.course_code,
                year=self.cl.year,
                semester=self.cl.semester,
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
                year=self.cl.year,
                semester=self.cl.semester,
        )

    def test_allow_new_semester(self):
        tutoring.models.CourseListing.objects.create(
                subject=self.cl.subject,
                course=self.cl.course,
                course_code=self.cl.course_code,
                year=self.cl.year,
                semester='SP',
        )

    def test_allow_new_code(self):
        tutoring.models.CourseListing.objects.create(
                subject=self.cl.subject,
                course=self.cl.course,
                year=self.cl.year,
                course_code=1200,
                semester=self.cl.semester,
        )

    def test_allow_new_subject(self):
        tutoring.models.CourseListing.objects.create(
                subject=self.itec,
                course=self.cl.course,
                course_code=self.cl.course_code,
                year=self.cl.year,
                semester=self.cl.semester,
        )

    def test_allow_new_year(self):
        tutoring.models.CourseListing.objects.create(
                subject=self.cl.subject,
                course=self.cl.course,
                course_code=self.cl.course_code,
                year=2010,
                semester=self.cl.semester,
        )

class HelpRequestTest(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user('john', 'john@doe.com', 'foo')
        self.user2 = User.objects.create_user('jane', 'jane@doe.com', 'foo')
        csci = tutoring.models.Subject.objects.create(
                code='CSCI',
                name='Computer Science',
                )
        cs1 = tutoring.models.Course.objects.create(
                title='Computer Science I',
                )
        self.cl = tutoring.models.CourseListing.objects.create(
                subject=csci,
                course=cs1,
                course_code=1100,
                year=2009,
                semester='FA'
                )
        self.hr = tutoring.models.HelpRequest.objects.create(
                    course_listing=self.cl,
                    student=self.user1
                    )

    def test_create_hr(self):
        tutoring.models.HelpRequest.objects.create(
                    course_listing=self.cl,
                    student=self.user2
                    )

    def test_cannot_teach_self(self):
        self.hr.teacher = self.user1
        self.assertRaises(IntegrityError, self.hr.save)

    def test_creation_date_status(self):
        self.assertNotEqual(self.hr.date_created, None)
        self.assertEqual(self.hr.date_taken, None)


