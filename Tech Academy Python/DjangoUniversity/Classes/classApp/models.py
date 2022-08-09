from django.db import models


class UniversityClasses(models.Model):
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    course_number = models.IntegerField(default="", blank=True, null=False)
    instructor_name = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.FloatField(null=True, blank=True, default=None)

    object = models.Manager()

    # displays object output values as a string
    def __str__(self):
        # returns input value of title and instructor_name as a tuple to display in broswer
        # instead of the default titles
        display_course = '{0.title}: {0.instructor_name}'
        return display_course.format(self)

    # removes added 's' that Django auto adds to model name in browser display
    class Meta:
        verbose_name_plural = "University Classes"
