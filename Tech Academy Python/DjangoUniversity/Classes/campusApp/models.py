from django.db import models


# creates UniversityCampus model
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_ID = models.IntegerField(default="", blank=True, null=False)

    # creates model manager
    object = models.Manager()

    def __str__(self):
        return self.campus_name

    #sets the plural name to "University Campus"
    class Meta:
        verbose_name_plural = "University Campus"
