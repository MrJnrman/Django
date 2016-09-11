from django.core.urlresolvers import reverse  # reverse a url name
from django.test import TestCase
from django.utils import timezone

from .models import Course
from .models import Step

class CourseModelTests(TestCase):
    def test_course_creation(self):
        course = Course.objects.create(
            title='Python Regular Expressions',
            description='Learn to write regular expressions in Python',
        )
        now = timezone.now()
        self.assertLess(course.created_at, now)

class CourseViewsTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(
            title='Python Testing',
            description='Learn to write tests in Python'
        )
        self.course2 = Course.objects.create(
            title='Java',
            description='Java ORM'
        )
        self.step = Step.objects.create(
            title='Intoduction to DocTests',
            description='Learn to write tests in your docstrings',
            course=self.course
        )

    def test_course_list_view(self):
        resp = self.client.get(reverse('courses:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.course, resp.context['courses'])  # resp context gives a dictionary from the reverse value at line 34, the name of the dictionary is 'courses' which is from views.py, the courses dictionary returned from the course_list function
        self.assertIn(self.course2, resp.context['courses'])
        self.assertTemplateUsed(resp, 'courses/course_list.html')
        self.assertContains(resp, self.course.title)

    def test_course_detail_view(self):
        resp = self.client.get(reverse('courses:detail', kwargs={'pk': self.course.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.course, resp.context['course'])
        self.assertTemplateUsed(resp, 'courses/course_detail.html')
        self.assertContains(resp, self.course.title)

    def test_step_detail_view(self):
        resp = self.client.get(reverse('courses:step', kwargs={'course_pk': self.step.course.pk, 'step_pk': self.step.pk }))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.step, resp.context['step'])
        self.assertTemplateUsed(resp, 'courses/step_detail.html')
        self.assertContains(resp, self.step.title)

