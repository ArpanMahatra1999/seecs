from activity.models import Activity
from course_class.models import CourseClass
from document.models import Document
from staff.models import Staff
from miscellaneous.models import Employment, Test
from trainer.models import Trainer
from trainee.models import Trainee
import django_filters


class ActivityFilter(django_filters.FilterSet):
    class Meta:
        model = Activity
        fields = ['title', 'target_sessions', 'target_trainees_per_session', 'actual_sessions', 'actual_trainees_per_session', 'target_deadline', 'actual_date_of_completion']


class CourseClassFilter(django_filters.FilterSet):
    class Meta:
        model = CourseClass
        fields = ['course', 'date_of_starting', 'date_of_ending', 'average_hours_per_day', 'days_per_week', 'shift']


class DocumentFilter(django_filters.FilterSet):
    class Meta:
        model = Document
        fields = ['title', 'tags', 'document_type', 'date_of_submission', 'created_on', 'last_updated_on']


class StaffFilter(django_filters.FilterSet):
    class Meta:
        model = Staff
        fields = ['first_name', 'middle_name', 'last_name', 'phone_number', 'email', 'permanent_address', 'temporary_address', 'date_of_birth', 'date_of_joining', 'post']


class EmploymentFilter(django_filters.FilterSet):
    class Meta:
        model = Employment
        fields = ['date_of_call', 'job_status', 'is_job_course_related', 'course_class', 'trainee']


class TestFilter(django_filters.FilterSet):
    class Meta:
        model = Test
        fields = ['date_of_application', 'date_of_exam', 'date_of_result', 'result_status', 'remark', 'course_class', 'trainee']


class TrainerFilter(django_filters.FilterSet):
    class Meta:
        model = Trainer
        fields = ['first_name', 'middle_name', 'last_name', 'phone_number', 'email', 'permanent_address', 'temporary_address', 'date_of_birth', 'date_of_joining', 'post']


class TraineeFilter(django_filters.FilterSet):
    class Meta:
        model = Trainee
        fields = ['first_name', 'middle_name', 'last_name', 'phone_number', 'email', 'permanent_address', 'temporary_address', 'date_of_birth', 'date_of_joining']
