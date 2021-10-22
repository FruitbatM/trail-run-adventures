from django.test import TestCase
from .models import Instructor


class TestModel(TestCase):

    def test_done_default_to_false(self):
        instructor = Instructor.objects.create(name="Test instructor",
                                               title="Test",
                                               about_content_1="Test content 1",
                                               about_content_2="Test content 2")
        self.assertFalse(instructor.image)

    def test_instructor_string_method_returns_name(self):
        instructor = Instructor.objects.create(name="Test Instructor")
        self.assertEqual(str(instructor), "Test Instructor")
