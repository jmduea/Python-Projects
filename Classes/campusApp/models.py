from django.db import models


# Creates model of University Campus
class UniversityCampus(models.Model):
    campus_Name = models.CharField(max_length=60, default="", blank=True, null=False)
    campus_State = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_ID = models.IntegerField(default="", blank=True, null=False)

    # Creates model manager
    object = models.Manager()

    # Displays the object output values in the form of a string
    def __str__(self):
        # Returns the input value of the title and instructor name
        # field as a tuple to display in the browser instead of the default titles
        display_course = '{0.campus_Name}: {0.campus_State}'
        return display_course.format(self)

# Removes added 's' that django adds to the model name in the browser display and sets it to a specific value
    class Meta:
        verbose_name_plural = "University Campus"
