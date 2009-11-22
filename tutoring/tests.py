"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

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
