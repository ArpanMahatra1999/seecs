from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from dss.models import DSS
from dss_admin.models import DSSAdmin
from smt_member.models import SMTMember
from trainer.models import Trainer, Qualification, Experience
from trainee.models import Trainee
from staff.models import Staff
from course.models import Course
from activity.models import Activity
from document.models import Document
from property.models import Property
from requirement.models import Requirement
from stakeholder.models import Stakeholder
from course_class.models import CourseClass, Test, Employment
from training.models import Training

from bootstrap_datepicker_plus import DatePickerInput


# Custom Input
class DateInput(forms.DateInput):
    input_type = 'date'


# Profile forms.
class CustomUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
        )

    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].disabled = True
        self.fields['password1'].initial = "7$)sm=ev@8eBP4P~+y`~=~j=Z]gyM.Gjy.B5%g:Qf,LQqyBzx6#A#$Q.((![NbnGx}eH_7+EhL)%aRb$e{4sPGX$+%Wb-C97MM<.WAg5brwF^B*E^*2=Wu+(C#={Xr="
        self.fields['password1'].widget = forms.HiddenInput()
        self.fields['password2'].disabled = True
        self.fields['password2'].initial = "7$)sm=ev@8eBP4P~+y`~=~j=Z]gyM.Gjy.B5%g:Qf,LQqyBzx6#A#$Q.((![NbnGx}eH_7+EhL)%aRb$e{4sPGX$+%Wb-C97MM<.WAg5brwF^B*E^*2=Wu+(C#={Xr="
        self.fields['password2'].widget = forms.HiddenInput()

    def save(self, commit=True):
        user = super(CustomUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.save()
        return user


class DSSProfileForm(forms.ModelForm):

    class Meta:
        model = DSS
        fields = [
            'title', 'calendar', 'date_of_establishment_BS', 'date_of_establishment_AD', 'description', 'photo', 'phone_number',
            'province', 'district', 'municipality', 'ward_number', 'street_name', 'tole_name'
        ]
        widgets = {
            'date_of_establishment_AD': DateInput()
        }


class DSSAdminProfileForm(forms.ModelForm):

    class Meta:
        model = DSSAdmin
        fields = ()


# SMT Member forms.
class CreateSMTMemberForm(forms.ModelForm):
    class Meta:
        model = SMTMember
        exclude = ['created_by']
        widgets = {
            'date_of_birth_AD': DateInput(),
            'date_of_joining_AD': DateInput(),
            'citizenship_issued_date_AD': DateInput()
        }


class UpdateSMTMemberForm(forms.ModelForm):
    class Meta:
        model = SMTMember
        exclude = ['created_by']
        widgets = {
            'date_of_birth_AD': DateInput(),
            'date_of_joining_AD': DateInput(),
            'citizenship_issued_date_AD': DateInput()
        }


# Trainer forms.
class CreateTrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        exclude = ['created_by']
        widgets = {
            'date_of_birth_AD': DateInput(),
            'date_of_joining_AD': DateInput(),
            'citizenship_issued_date_AD': DateInput()
        }


class UpdateTrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        exclude = ['created_by']
        widgets = {
            'date_of_birth_AD': DateInput(),
            'date_of_joining_AD': DateInput(),
            'citizenship_issued_date_AD': DateInput()
        }


# Qualification forms.
class CreateQualificationForm(forms.ModelForm):
    class Meta:
        model = Qualification
        exclude = ['trainer']
        widgets = {
            'started_from_AD': DateInput(),
            'ended_on_AD': DateInput()
        }


class UpdateQualificationForm(forms.ModelForm):
    class Meta:
        model = Qualification
        exclude = ['trainer']
        widgets = {
            'started_from_AD': DateInput(),
            'ended_on_AD': DateInput()
        }


# Experience forms.
class CreateExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        exclude = ['trainer']
        widgets = {
            'started_from_AD': DateInput(),
            'ended_on_AD': DateInput()
        }


class UpdateExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        exclude = ['trainer']
        widgets = {
            'started_from_AD': DateInput(),
            'ended_on_AD': DateInput()
        }


# Trainee forms.
class CreateTraineeForm(forms.ModelForm):
    class Meta:
        model = Trainee
        exclude = ['created_by']
        widgets = {
            'date_of_birth_AD': DateInput(),
            'date_of_joining_AD': DateInput(),
            'citizenship_issued_date_AD': DateInput()
        }


class UpdateTraineeForm(forms.ModelForm):
    class Meta:
        model = Trainee
        exclude = ['created_by']
        widgets = {
            'date_of_birth_AD': DateInput(),
            'date_of_joining_AD': DateInput(),
            'citizenship_issued_date_AD': DateInput()
        }


# Staff forms.
class CreateStaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        exclude = ['created_by']
        widgets = {
            'date_of_birth_AD': DateInput(),
            'date_of_joining_AD': DateInput(),
            'citizenship_issued_date_AD': DateInput()
        }


class UpdateStaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        exclude = ['created_by']
        widgets = {
            'date_of_birth_AD': DateInput(),
            'date_of_joining_AD': DateInput(),
            'citizenship_issued_date_AD': DateInput()
        }


# Activity forms.
class CreateActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        exclude = ['created_by']
        widgets = {
            'planned_start_date_AD': DateInput(),
            'planned_end_date_AD': DateInput(),
            'actual_start_date_AD': DateInput(),
            'actual_end_date_AD': DateInput()
        }


class UpdateActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        exclude = ['created_by']
        widgets = {
            'planned_start_date_AD': DateInput(),
            'planned_end_date_AD': DateInput(),
            'actual_start_date_AD': DateInput(),
            'actual_end_date_AD': DateInput()
        }


# Document forms.
class CreateDocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        exclude = ['created_by']
        widgets = {
            'date_of_submission_AD': DateInput(),
            'created_on_AD': DateInput(),
            'last_updated_on_AD': DateInput()
        }


class UpdateDocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        exclude = ['created_by']
        widgets = {
            'date_of_submission_AD': DateInput(),
            'created_on_AD': DateInput(),
            'last_updated_on_AD': DateInput()
        }


# Property forms.
class CreatePropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        exclude = ['created_by']
        widgets = {
            'date_of_purchase_AD': DateInput()
        }


class UpdatePropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        exclude = ['created_by']
        widgets = {
            'date_of_purchase_AD': DateInput()
        }


# Requirement forms.
class CreateRequirementForm(forms.ModelForm):
    class Meta:
        model = Requirement
        exclude = ['created_by']
        widgets = {
            'estimated_date_of_purchase_AD': DateInput()
        }

    def __init__(self, user, *args, **kwargs):
        super(CreateRequirementForm, self).__init__(*args, **kwargs)
        required_dss_admin = DSSAdmin.objects.get(user=user)
        required_dss = required_dss_admin.dss
        self.fields['activity'].queryset = Activity.objects.filter(dss=required_dss)


class UpdateRequirementForm(forms.ModelForm):
    class Meta:
        model = Requirement
        exclude = ['created_by']
        widgets = {
            'estimated_date_of_purchase_AD': DateInput()
        }

    def __init__(self, user, *args, **kwargs):
        super(UpdateRequirementForm, self).__init__(*args, **kwargs)
        required_dss_admin = DSSAdmin.objects.get(user=user)
        required_dss = required_dss_admin.dss
        self.fields['activity'].queryset = Activity.objects.filter(dss=required_dss)


# Stakeholder forms.
class CreateStakeholderForm(forms.ModelForm):
    class Meta:
        model = Stakeholder
        fields = '__all__'


class UpdateStakeholderForm(forms.ModelForm):
    class Meta:
        model = Stakeholder
        fields = '__all__'


# Course forms.
class CreateCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class UpdateCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


# Training forms.
class CreateTrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        exclude = ['created_by']
        widgets = {
            'planned_start_date_AD': DateInput(),
            'planned_end_date_AD': DateInput(),
            'actual_start_date_AD': DateInput(),
            'actual_end_date_AD': DateInput()
        }


class UpdateTrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        exclude = ['created_by']
        widgets = {
            'planned_start_date_AD': DateInput(),
            'planned_end_date_AD': DateInput(),
            'actual_start_date_AD': DateInput(),
            'actual_end_date_AD': DateInput()
        }


# Other Miscellaneous forms.
# Course Class forms for course.
class CreateCourseClassForm(forms.ModelForm):
    class Meta:
        model = CourseClass
        exclude = ['user', 'trainers', 'course']
        widgets = {
            'date_of_starting_AD': DateInput(),
            'date_of_ending_AD': DateInput()
        }


class UpdateCourseClassForm(forms.ModelForm):
    class Meta:
        model = CourseClass
        exclude = ['user', 'trainers', 'course', 'dss']
        widgets = {
            'date_of_starting_AD': DateInput(),
            'date_of_ending_AD': DateInput()
        }


# Test forms for class and trainee.
class CreateTestForm(forms.ModelForm):
    class Meta:
        model = Test
        exclude = ['course_class', 'trainee', 'dss']
        widgets = {
            'date_of_application_AD': DateInput(),
            'date_of_exam_AD': DateInput(),
            'date_of_result_AD': DateInput()
        }


class UpdateTestForm(forms.ModelForm):
    class Meta:
        model = Test
        exclude = ['course_class', 'trainee', 'dss']
        widgets = {
            'date_of_application_AD': DateInput(),
            'date_of_exam_AD': DateInput(),
            'date_of_result_AD': DateInput()
        }


# Employment forms for class and trainee.
class CreateEmploymentForm(forms.ModelForm):
    class Meta:
        model = Employment
        exclude = ['course_class', 'trainee', 'dss']
        widgets = {
            'date_of_call_AD': DateInput(),
            'start_date_AD': DateInput(),
            'end_date_AD': DateInput()
        }

    def __init__(self, *args, **kwargs):
        super(CreateEmploymentForm, self).__init__(*args, **kwargs)
        self.fields['employer'].queryset = Stakeholder.objects.filter(stakeholder_type="Employer")


class UpdateEmploymentForm(forms.ModelForm):
    class Meta:
        model = Employment
        exclude = ['course_class', 'trainee', 'dss']
        widgets = {
            'date_of_call_AD': DateInput(),
            'start_date_AD': DateInput(),
            'end_date_AD': DateInput()
        }

    def __init__(self, *args, **kwargs):
        super(UpdateEmploymentForm, self).__init__(*args, **kwargs)
        self.fields['employer'].queryset = Stakeholder.objects.filter(stakeholder_type="Employer")

