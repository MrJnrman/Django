from django.contrib import admin


from .models import Course
from .models import Step

# Register your models here.

# can be stacked or tabular
class StepInline(admin.TabularInline):
    model = Step

# allows us to alter steps associated to a specific course, on that course itself
class CourseAdmin(admin.ModelAdmin):
    inlines = [StepInline,]

admin.site.register(Course, CourseAdmin)

