from django.test import TestCase
from .models import todo

# Create your tests here.
class TodoModelTest(TestCase):

	def test_is_title_non_empty(self):
		test_title = ""									# Empyt test title
		field = todo.objects.get(id=1)					# get title from the db
		self.assertNotEqual(str(field),test_title)		# Test to see those two are not equal
		
	def test_is_description_non_empty(self):
		test_description = ""
		field = todo.objects.get(id=2)
		self.assertNotEqual(str(field),test_description)
	

