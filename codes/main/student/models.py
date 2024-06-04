from django.db import models
from datetime import date
class StudentProfile(models.Model):
    student_name = models.CharField(max_length=255)  # Student's full name
    matric_id = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)  # Student's institution name
    industrial_supervisor = models.CharField(max_length=255)  # Name of industrial supervisor
    industry_based_supervisor = models.CharField(max_length=255)  # Name of industry-based supervisor
    year_of_study = models.PositiveSmallIntegerField()  # Year of study (e.g., 3 for third year)
    course_of_study = models.CharField(max_length=255)  # Student's course name

    def __str__(self):
        return f"{self.student_name} ({self.course_of_study}, Year {self.year_of_study}) - {self.institution}"

class ActivityLog(models.Model):
    activity_description = models.TextField()  # Description of the activity performed
    date = models.DateField(default=date.today)  # Date the activity was performed (automatically set)

    def __str__(self):
        return f"Activity: {self.activity_description} on {self.date}"


class StudentPermit(models.Model):
    student_name = models.CharField(max_length=255)  # Student's full name
    reason_for_leave = models.TextField()  # Detailed reason for leaving
    start_date = models.DateField()  # Date permit starts (inclusive)
    end_date = models.DateField()  # Date permit ends (inclusive)

    def __str__(self):
        return f"{self.student_name} Permit: {self.reason_for_leave} ({self.start_date} - {self.end_date})"

    class Meta:
        ordering = ['start_date']  # Order permits by start date (ascending)


