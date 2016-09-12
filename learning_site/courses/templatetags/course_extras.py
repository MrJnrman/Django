from django import template
from django.utils.safestring import mark_safe

import markdown2

from ..models import Course

register = template.Library()

# simpletag returns it data as a string
@register.simple_tag
def newest_course():
    '''gets the most recent course that was added to the library'''
    return Course.objects.latest('created_at')

# returns data as template
@register.inclusion_tag('courses/course_nav.html')
def nav_courses_list():
    '''returns dictionary of courses to display as navigation pane'''
    courses = Course.objects.all()
    return {'courses': courses}

@register.filter('time_estimate')
def time_estimate(word_count):
    '''estimates the number of minutes it will take to complete a step based on the passed-in wordcount'''
    minutes = round(word_count/5)
    return minutes

@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    '''converts markdown text to html'''
    html_body = markdown2.markdown(markdown_text)
    return mark_safe(html_body)