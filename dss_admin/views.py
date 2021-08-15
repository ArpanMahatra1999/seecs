from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.db.models import Q
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from ctevt.settings import EMAIL_HOST_USER
from ctevt.utils import generate_token

from .forms import CreateCourseClassForm
from .forms import CreateSMTMemberForm, CreateTrainerForm, CreateTraineeForm, CreateStaffForm
from .forms import CreateTrainingForm, CreateQualificationForm, CreateExperienceForm, CreateTestForm, CreateEmploymentForm
from .forms import CreateActivityForm, CreateDocumentForm, CreatePropertyForm, CreateRequirementForm
from .forms import UpdateCourseClassForm
from .forms import UpdateSMTMemberForm, UpdateTrainerForm, UpdateTraineeForm, UpdateStaffForm
from .forms import UpdateTrainingForm, UpdateQualificationForm, UpdateExperienceForm, UpdateTestForm, UpdateEmploymentForm
from .forms import UpdateActivityForm, UpdateDocumentForm, UpdatePropertyForm, UpdateRequirementForm
from .forms import UserEditForm, UserProfileEditForm, CustomPasswordChangeForm
from .forms import CustomUserForm, DSSAdminProfileForm

from dss.models import DSS
from dss_admin.models import DSSAdmin
from course_class.models import CourseClass, Test, Employment
from smt_member.models import SMTMember
from trainer.models import Trainer, Qualification, Experience
from trainee.models import Trainee
from staff.models import Staff
from training.models import Training
from activity.models import Activity
from document.models import Document
from property.models import Property
from requirement.models import Requirement
from notification.models import Notification
from ctevt.date_converter import ad_to_bs, bs_to_ad

from datetime import date


@login_required
def landing(request):

    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss

    if not request.user.is_superuser:
        course_classes = CourseClass.objects.filter(dss=required_dss)
        smtms = SMTMember.objects.filter(dss=required_dss)
        trainers = Trainer.objects.filter(dss=required_dss)
        trainees = Trainee.objects.filter(dss=required_dss)
        staffs = Staff.objects.filter(dss=required_dss)
        trainings = Training.objects.filter(dss=required_dss)
        activities = Activity.objects.filter(dss=required_dss)
        documents = Document.objects.filter(dss=required_dss)

        courses = [
            'Agriculture', 'Tourism', 'Construction'
        ]
        agriculture = CourseClass.objects.filter(Q(dss=required_dss) & Q(course__type="Agriculture")).count()
        tourism = CourseClass.objects.filter(Q(dss=required_dss) & Q(course__type="Tourism")).count()
        construction = CourseClass.objects.filter(Q(dss=required_dss) & Q(course__type="Construction")).count()
        course_classes_by_type = [agriculture, tourism, construction]

        people = [
            'SMT Members', 'Trainers', 'Trainees', 'Other Staffs'
        ]
        people_by_type = [len(smtms), len(trainers), len(trainees), len(staffs)]

        document_types = [
            'Application', 'Letter', 'Minute', 'Proposal', 'Report', 'Research Paper', 'Resume', 'Thesis', 'None'
        ]
        application = Document.objects.filter(Q(dss=required_dss) & Q(document_type="Application")).count()
        letter = Document.objects.filter(Q(dss=required_dss) & Q(document_type="Letter")).count()
        minute = Document.objects.filter(Q(dss=required_dss) & Q(document_type="Minute")).count()
        proposal = Document.objects.filter(Q(dss=required_dss) & Q(document_type="Proposal")).count()
        report = Document.objects.filter(Q(dss=required_dss) & Q(document_type="Report")).count()
        research_paper = Document.objects.filter(Q(dss=required_dss) & Q(document_type="Research Paper")).count()
        resume = Document.objects.filter(Q(dss=required_dss) & Q(document_type="Resume")).count()
        thesis = Document.objects.filter(Q(dss=required_dss) & Q(document_type="Thesis")).count()
        others = Document.objects.filter(Q(dss=required_dss) & Q(document_type="Others")).count()
        none = len(documents) - application - letter - minute - proposal - report - research_paper - resume - thesis - others
        documents_by_type = [application, letter, minute, proposal, report, research_paper, resume, thesis, others, none]

        property_types = [
            "Land", "Building", "Furniture", "Automobile", "Electronic", "Others"
        ]

        land_p = Property.objects.filter(Q(dss=required_dss) & Q(property_type="Land")).count()
        building_p = Property.objects.filter(Q(dss=required_dss) & Q(property_type="Building")).count()
        furniture_p = Property.objects.filter(Q(dss=required_dss) & Q(property_type="Furniture")).count()
        automobile_p = Property.objects.filter(Q(dss=required_dss) & Q(property_type="Automobile")).count()
        electronic_p = Property.objects.filter(Q(dss=required_dss) & Q(property_type="Electronic")).count()
        others_p = Property.objects.filter(Q(dss=required_dss) & Q(property_type="Others")).count()

        properties_by_type = [land_p, building_p, furniture_p, automobile_p, electronic_p, others_p]

        requirement_types = [
            "Land", "Building", "Furniture", "Automobile", "Electronic", "Others"
        ]

        land_r = Requirement.objects.filter(Q(dss=required_dss) & Q(requirement_type="Land")).count()
        building_r = Requirement.objects.filter(Q(dss=required_dss) & Q(requirement_type="Building")).count()
        furniture_r = Requirement.objects.filter(Q(dss=required_dss) & Q(requirement_type="Furniture")).count()
        automobile_r = Requirement.objects.filter(Q(dss=required_dss) & Q(requirement_type="Automobile")).count()
        electronic_r = Requirement.objects.filter(Q(dss=required_dss) & Q(requirement_type="Electronic")).count()
        others_r = Requirement.objects.filter(Q(dss=required_dss) & Q(requirement_type="Others")).count()

        requirements_by_type = [land_r, building_r, furniture_r, automobile_r, electronic_r, others_r]

        context = {
            'course_classes': course_classes,
            'courses': courses,
            'course_classes_by_type': course_classes_by_type,

            'people': people,
            'people_by_type': people_by_type,
            'smtms': smtms,
            'trainers': trainers,
            'trainees': trainees,
            'staffs': staffs,

            'trainings': trainings,

            'activities': activities,

            'documents': documents,
            'document_types': document_types,
            'documents_by_type': documents_by_type,

            'property_types': property_types,
            'property_by_type': properties_by_type,

            'requirement_types': requirement_types,
            'requirement_by_type': requirements_by_type
        }
        return render(request, 'dss/home.html', context)
    else:
        return redirect('home')


# DSS views.
@login_required
def create_dss_admin(request):
    if not request.user.is_superuser:
        required_dss_admin = DSSAdmin.objects.get(user=request.user)
        required_dss = required_dss_admin.dss
        if request.method == 'POST':
            form = CustomUserForm(request.POST)
            profile_form = DSSAdminProfileForm(request.POST, request.FILES)
            if form.is_valid() and profile_form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.dss = required_dss
                profile.save()
                email = form.cleaned_data.get('email')
                current_site = get_current_site(request)
                email_subject = 'Activate your account'
                message = render_to_string(
                    'registration/activate.html',
                    {
                        'user': user,
                        'domain': current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': generate_token.make_token(user)
                    }
                )
                email_message = EmailMessage(
                    email_subject,
                    message,
                    EMAIL_HOST_USER,
                    [email]
                )
                email_message.send()
                return redirect('dss:read-dss-admin')
        else:
            form = CustomUserForm()
            profile_form = DSSAdminProfileForm()
        context = {
            'form': form,
            'profile_form': profile_form
        }
        return render(request, 'dss/create/dss_admin.html', context)
    else:
        return redirect('home')


@login_required
def read_dss_admin(request):
    if not request.user.is_superuser:
        required_dss_admin = DSSAdmin.objects.get(user=request.user)
        required_dss = required_dss_admin.dss
        dss_admin_list = DSSAdmin.objects.filter(dss=required_dss)
        context = {
            'dss': required_dss,
            'dss_admins': dss_admin_list,
        }
        return render(request, 'dss/read/dss_admin.html', context)
    else:
        return redirect('home')


@login_required
def dss_admin_detail(request, pk):
    current_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = DSS.objects.get(id=current_admin.dss.id)
    required_dss_admin = DSSAdmin.objects.get(id=pk)
    required_course_classes = CourseClass.objects.filter(user=required_dss_admin.user)
    if not request.user.is_superuser and current_admin.dss == required_dss_admin.dss:
        context = {
            'dss': required_dss,
            'dss_admin': required_dss_admin,
            'course_classes': required_course_classes
        }
        return render(request, "dss/detail/dss_admin.html", context)
    else:
        return redirect('home')


# Course Class views.
@login_required
def create_course_class(request):

    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss

    if not request.user.is_superuser:
        if request.method == 'POST':
            form = CreateCourseClassForm(user=request.user, data=request.POST, files=request.FILES)
            if form.is_valid():
                course_class = form.save(commit=False)
                course_class.user = request.user
                course_class.dss = required_dss
                if (course_class.calendar == 'BS'):
                    if course_class.date_of_starting_BS:
                        course_class.date_of_starting_AD = bs_to_ad.to_ad(course_class.date_of_starting_BS)
                    else:
                        course_class.date_of_starting_BS = "1975-01-01"
                        course_class.date_of_starting_AD = "1975-01-01"
                    if course_class.date_of_ending_BS:
                        course_class.date_of_ending_AD = bs_to_ad.to_ad(course_class.date_of_ending_BS)
                    else:
                        course_class.date_of_ending_BS = "1975-01-01"
                        course_class.date_of_ending_AD = "1975-01-01"
                if (course_class.calendar == 'AD'):
                    if course_class.date_of_starting_AD:
                        course_class.date_of_starting_BS = ad_to_bs.to_bs(course_class.date_of_starting_AD)
                    else:
                        course_class.date_of_starting_AD = "1975-01-01"
                        course_class.date_of_starting_BS = "1975-01-01"
                    if course_class.date_of_ending_AD:
                        course_class.date_of_ending_BS = ad_to_bs.to_bs(course_class.date_of_ending_AD)
                    else:
                        course_class.date_of_ending_AD = "1975-01-01"
                        course_class.date_of_ending_BS = "1975-01-01"
                course_class.save()
                form.save_m2m()
                notification = Notification(
                    course_class=course_class,
                    message="was created"
                )
                notification.save()
                return redirect('dss:read-course-class')
        else:
            form = CreateCourseClassForm(user=request.user)
        context = {
            'form': form
        }
        return render(request, 'dss/create/course_class.html', context)
    else:
        return redirect('home')


@login_required
def read_course_class(request):
    if not request.user.is_superuser:
        required_admin = DSSAdmin.objects.get(user=request.user)
        required_dss = required_admin.dss
        course_class_list = CourseClass.objects.filter(dss=required_dss)
        context = {
            'course_classes': course_class_list,
        }
        return render(request, 'dss/read/course_class.html', context)
    else:
        return redirect('home')


@login_required
def update_course_class(request, pk):
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss
    required_course_class = CourseClass.objects.get(id=pk)
    if not request.user.is_superuser and required_course_class.dss == required_dss:
        if request.method == 'POST':
            form = UpdateCourseClassForm(user=request.user, data=request.POST, files=request.FILES, instance=required_course_class)
            if form.is_valid():
                course_class = form.save(commit=False)
                if (course_class.calendar == 'BS'):
                    if course_class.date_of_starting_BS:
                        course_class.date_of_starting_AD = bs_to_ad.to_ad(course_class.date_of_starting_BS)
                    else:
                        course_class.date_of_starting_BS = "1975-01-01"
                        course_class.date_of_starting_AD = "1975-01-01"
                    if course_class.date_of_ending_BS:
                        course_class.date_of_ending_AD = bs_to_ad.to_ad(course_class.date_of_ending_BS)
                    else:
                        course_class.date_of_ending_BS = "1975-01-01"
                        course_class.date_of_ending_AD = "1975-01-01"
                if (course_class.calendar == 'AD'):
                    if course_class.date_of_starting_AD:
                        course_class.date_of_starting_BS = ad_to_bs.to_bs(course_class.date_of_starting_AD)
                    else:
                        course_class.date_of_starting_AD = "1975-01-01"
                        course_class.date_of_starting_BS = "1975-01-01"
                    if course_class.date_of_ending_AD:
                        course_class.date_of_ending_BS = ad_to_bs.to_bs(course_class.date_of_ending_AD)
                    else:
                        course_class.date_of_ending_AD = "1975-01-01"
                        course_class.date_of_ending_BS = "1975-01-01"
                course_class.save()
                form.save_m2m()
                notification = Notification(
                    course_class=course_class,
                    message="was created"
                )
                notification.save()
                return redirect('dss:read-course-class')
        else:
            form = UpdateCourseClassForm(user=request.user, instance=required_course_class)
        context = {
            'form': form
        }
        return render(request, 'dss/update/course_class.html', context)
    else:
        return redirect('home')


@login_required
def delete_course_class(request, pk):
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss
    required_course_class = CourseClass.objects.get(id=pk)
    if not request.user.is_superuser and required_course_class.dss == required_dss:
        context = {}
        if request.method == "POST":
            required_course_class.delete()
            return redirect('dss:read-course-class')
        return render(request, "dss/delete/course_class.html", context)
    else:
        return redirect('home')


@login_required
def course_class_detail(request, pk):
    if not request.user.is_superuser:
        required_admin = DSSAdmin.objects.get(user=request.user)
        required_dss = required_admin.dss
        course_class = CourseClass.objects.get(id=pk)
        trainees = Trainee.objects.filter(course_class=course_class)
        tests = Test.objects.filter(course_class=course_class)
        employments = Employment.objects.filter(course_class=course_class)
        context = {
            'course_class': course_class,
            'trainees': trainees,
            'tests': tests,
            'employments': employments
        }
        if course_class.dss == required_dss:
            return render(request, "dss/detail/course_class.html", context)
        else:
            return redirect('dss:read-course-class')
    else:
        return redirect('home')


# SMT System views.
@login_required
def create_smt_member(request):
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss

    if not request.user.is_superuser:
        if request.method == 'POST':
            form = CreateSMTMemberForm(request.POST, request.FILES)
            if form.is_valid():
                smt_member = form.save(commit=False)
                smt_member.dss = required_dss
                smt_member.created_by = request.user
                if (smt_member.calendar == 'BS'):
                    if smt_member.date_of_birth_BS:
                        smt_member.date_of_birth_AD = bs_to_ad.to_ad(smt_member.date_of_birth_BS)
                    else:
                        smt_member.date_of_birth_BS = "1975-01-01"
                        smt_member.date_of_birth_AD = "1975-01-01"
                    if smt_member.date_of_joining_BS:
                        smt_member.date_of_joining_AD = bs_to_ad.to_ad(smt_member.date_of_joining_BS)
                    else:
                        smt_member.date_of_joining_BS = "1975-01-01"
                        smt_member.date_of_joining_AD = "1975-01-01"
                    if smt_member.citizenship_issued_date_BS:
                        smt_member.citizenship_issued_date_AD = bs_to_ad.to_ad(smt_member.citizenship_issued_date_BS)
                    else:
                        smt_member.citizenship_issued_date_BS = "1975-01-01"
                        smt_member.citizenship_issued_date_AD = "1975-01-01"
                if (smt_member.calendar == 'AD'):
                    if smt_member.date_of_birth_AD:
                        smt_member.date_of_birth_BS = ad_to_bs.to_bs(smt_member.date_of_birth_AD)
                    else:
                        smt_member.date_of_birth_AD = "1975-01-01"
                        smt_member.date_of_birth_BS = "1975-01-01"
                    if smt_member.date_of_joining_AD:
                        smt_member.date_of_joining_BS = ad_to_bs.to_bs(smt_member.date_of_joining_AD)
                    else:
                        smt_member.date_of_joining_AD = "1975-01-01"
                        smt_member.date_of_joining_BS = "1975-01-01"
                    if smt_member.citizenship_issued_date_AD:
                        smt_member.citizenship_issued_date_BS = ad_to_bs.to_bs(smt_member.citizenship_issued_date_AD)
                    else:
                        smt_member.citizenship_issued_date_AD = "1975-01-01"
                        smt_member.citizenship_issued_date_BS = "1975-01-01"
                smt_member.save()
                return redirect('dss:read-smtm')
        else:
            form = CreateSMTMemberForm()
        context = {
            'form': form
        }
        return render(request, 'dss/create/smtm.html', context)
    else:
        return redirect('home')


@login_required
def read_smt_member(request):
    if not request.user.is_superuser:
        required_admin = DSSAdmin.objects.get(user=request.user)
        required_dss = required_admin.dss
        smtm_list = SMTMember.objects.filter(dss=required_dss)
        context = {
            'smtms': smtm_list,
        }
        return render(request, 'dss/read/smtm.html', context)
    else:
        return redirect('home')


@login_required
def update_smt_member(request, pk):
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss
    required_smtm = SMTMember.objects.get(id=pk)
    if not request.user.is_superuser and required_smtm.dss == required_dss:
        if request.method == 'POST':
            form = UpdateSMTMemberForm(data=request.POST, files=request.FILES, instance=required_smtm)
            if form.is_valid():
                smt_member = form.save(commit=False)
                if (smt_member.calendar == 'BS'):
                    if smt_member.date_of_birth_BS:
                        smt_member.date_of_birth_AD = bs_to_ad.to_ad(smt_member.date_of_birth_BS)
                    else:
                        smt_member.date_of_birth_BS = "1975-01-01"
                        smt_member.date_of_birth_AD = "1975-01-01"
                    if smt_member.date_of_joining_BS:
                        smt_member.date_of_joining_AD = bs_to_ad.to_ad(smt_member.date_of_joining_BS)
                    else:
                        smt_member.date_of_joining_BS = "1975-01-01"
                        smt_member.date_of_joining_AD = "1975-01-01"
                    if smt_member.citizenship_issued_date_BS:
                        smt_member.citizenship_issued_date_AD = bs_to_ad.to_ad(smt_member.citizenship_issued_date_BS)
                    else:
                        smt_member.citizenship_issued_date_BS = "1975-01-01"
                        smt_member.citizenship_issued_date_AD = "1975-01-01"
                if (smt_member.calendar == 'AD'):
                    if smt_member.date_of_birth_AD:
                        smt_member.date_of_birth_BS = ad_to_bs.to_bs(smt_member.date_of_birth_AD)
                    else:
                        smt_member.date_of_birth_AD = "1975-01-01"
                        smt_member.date_of_birth_BS = "1975-01-01"
                    if smt_member.date_of_joining_AD:
                        smt_member.date_of_joining_BS = ad_to_bs.to_bs(smt_member.date_of_joining_AD)
                    else:
                        smt_member.date_of_joining_AD = "1975-01-01"
                        smt_member.date_of_joining_BS = "1975-01-01"
                    if smt_member.citizenship_issued_date_AD:
                        smt_member.citizenship_issued_date_BS = ad_to_bs.to_bs(smt_member.citizenship_issued_date_AD)
                    else:
                        smt_member.citizenship_issued_date_AD = "1975-01-01"
                        smt_member.citizenship_issued_date_BS = "1975-01-01"
                smt_member.save()
                return redirect('dss:read-smtm')
        else:
            form = UpdateSMTMemberForm(instance=required_smtm)
        context = {
            'form': form
        }
        return render(request, 'dss/update/smtm.html', context)
    else:
        return redirect('home')


@login_required
def delete_smt_member(request, pk):
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss
    required_smtm = SMTMember.objects.get(id=pk)
    if not request.user.is_superuser and required_smtm.dss == required_dss:
        context = {}
        if request.method == "POST":
            required_smtm.delete()
            return redirect('dss:read-smtm')
        return render(request, "dss/delete/smtm.html", context)
    else:
        return redirect('home')


@login_required
def smt_member_detail(request, pk):
    if not request.user.is_superuser:
        required_admin = DSSAdmin.objects.get(user=request.user)
        required_dss = required_admin.dss
        smtm = SMTMember.objects.get(id=pk)
        context = {
            'smtm': smtm
        }
        if smtm.dss == required_dss:
            return render(request, "dss/detail/smtm.html", context)
        else:
            return redirect('dss:read-smtm')
    else:
        return redirect('home')


# Trainer views.
@login_required
def create_trainer(request):
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss

    if not request.user.is_superuser:
        if request.method == 'POST':
            form = CreateTrainerForm(request.POST, request.FILES)
            if form.is_valid():
                trainer = form.save(commit=False)
                trainer.dss = required_dss
                trainer.created_by = request.user
                if (trainer.calendar == 'BS'):
                    if trainer.date_of_birth_BS:
                        trainer.date_of_birth_AD = bs_to_ad.to_ad(trainer.date_of_birth_BS)
                    else:
                        trainer.date_of_birth_BS = "1975-01-01"
                        trainer.date_of_birth_AD = "1975-01-01"
                    if trainer.date_of_joining_BS:
                        trainer.date_of_joining_AD = bs_to_ad.to_ad(trainer.date_of_joining_BS)
                    else:
                        trainer.date_of_joining_BS = "1975-01-01"
                        trainer.date_of_joining_AD = "1975-01-01"
                    if trainer.citizenship_issued_date_BS:
                        trainer.citizenship_issued_date_AD = bs_to_ad.to_ad(trainer.citizenship_issued_date_BS)
                    else:
                        trainer.citizenship_issued_date_BS = "1975-01-01"
                        trainer.citizenship_issued_date_AD = "1975-01-01"
                if (trainer.calendar == 'AD'):
                    if trainer.date_of_birth_AD:
                        trainer.date_of_birth_BS = ad_to_bs.to_bs(trainer.date_of_birth_AD)
                    else:
                        trainer.date_of_birth_AD = "1975-01-01"
                        trainer.date_of_birth_BS = "1975-01-01"
                    if trainer.date_of_joining_AD:
                        trainer.date_of_joining_BS = ad_to_bs.to_bs(trainer.date_of_joining_AD)
                    else:
                        trainer.date_of_joining_AD = "1975-01-01"
                        trainer.date_of_joining_BS = "1975-01-01"
                    if trainer.citizenship_issued_date_AD:
                        trainer.citizenship_issued_date_BS = ad_to_bs.to_bs(trainer.citizenship_issued_date_AD)
                    else:
                        trainer.citizenship_issued_date_AD = "1975-01-01"
                        trainer.citizenship_issued_date_BS = "1975-01-01"
                trainer.save()
                form.save_m2m()
                return redirect('dss:read-trainer')
        else:
            form = CreateTrainerForm()
        context = {
            'form': form
        }
        return render(request, 'dss/create/trainer.html', context)
    else:
        return redirect('home')


@login_required
def read_trainer(request):
    if not request.user.is_superuser:
        required_admin = DSSAdmin.objects.get(user=request.user)
        required_dss = required_admin.dss
        trainer_list = Trainer.objects.filter(dss=required_dss)
        context = {
            'trainers': trainer_list,
        }
        return render(request, 'dss/read/trainer.html', context)
    else:
        return redirect('home')


@login_required
def update_trainer(request, pk):
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss
    required_trainer = Trainer.objects.get(id=pk)
    if not request.user.is_superuser and required_trainer.dss == required_dss:
        if request.method == 'POST':
            form = UpdateTrainerForm(data=request.POST, files=request.FILES, instance=required_trainer)
            if form.is_valid():
                trainer = form.save(commit=False)
                if (trainer.calendar == 'BS'):
                    if trainer.date_of_birth_BS:
                        trainer.date_of_birth_AD = bs_to_ad.to_ad(trainer.date_of_birth_BS)
                    else:
                        trainer.date_of_birth_BS = "1975-01-01"
                        trainer.date_of_birth_AD = "1975-01-01"
                    if trainer.date_of_joining_BS:
                        trainer.date_of_joining_AD = bs_to_ad.to_ad(trainer.date_of_joining_BS)
                    else:
                        trainer.date_of_joining_BS = "1975-01-01"
                        trainer.date_of_joining_AD = "1975-01-01"
                    if trainer.citizenship_issued_date_BS:
                        trainer.citizenship_issued_date_AD = bs_to_ad.to_ad(trainer.citizenship_issued_date_BS)
                    else:
                        trainer.citizenship_issued_date_BS = "1975-01-01"
                        trainer.citizenship_issued_date_AD = "1975-01-01"
                if (trainer.calendar == 'AD'):
                    if trainer.date_of_birth_AD:
                        trainer.date_of_birth_BS = ad_to_bs.to_bs(trainer.date_of_birth_AD)
                    else:
                        trainer.date_of_birth_AD = "1975-01-01"
                        trainer.date_of_birth_BS = "1975-01-01"
                    if trainer.date_of_joining_AD:
                        trainer.date_of_joining_BS = ad_to_bs.to_bs(trainer.date_of_joining_AD)
                    else:
                        trainer.date_of_joining_AD = "1975-01-01"
                        trainer.date_of_joining_BS = "1975-01-01"
                    if trainer.citizenship_issued_date_AD:
                        trainer.citizenship_issued_date_BS = ad_to_bs.to_bs(trainer.citizenship_issued_date_AD)
                    else:
                        trainer.citizenship_issued_date_AD = "1975-01-01"
                        trainer.citizenship_issued_date_BS = "1975-01-01"
                trainer.save()
                form.save_m2m()
                return redirect('dss:trainer-detail', pk=required_trainer.pk)
        else:
            form = UpdateTrainerForm(instance=required_trainer)
        context = {
            'form': form
        }
        return render(request, 'dss/update/trainer.html', context)
    else:
        return redirect('home')


@login_required
def delete_trainer(request, pk):
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss
    required_trainer = Trainer.objects.get(id=pk)
    if not request.user.is_superuser and required_trainer.dss == required_dss:
        context = {}
        if request.method == "POST":
            required_trainer.delete()
            return redirect('dss:read-trainer')
        return render(request, "dss/delete/trainer.html", context)
    else:
        return redirect('home')


@login_required
def trainer_detail(request, pk):
    if not request.user.is_superuser:
        required_admin = DSSAdmin.objects.get(user=request.user)
        required_dss = required_admin.dss
        trainer = Trainer.objects.get(id=pk)

        all_qualifications = Qualification.objects.all()
        qualifications = []
        for qualification in all_qualifications:
            if qualification.trainer == trainer:
                qualifications.append(qualification)

        all_experiences = Experience.objects.all()
        experiences = []
        for experience in all_experiences:
            if experience.trainer == trainer:
                experiences.append(experience)

        context = {
            'trainer': trainer,
            'qualifications': qualifications,
            'experiences': experiences
        }
        if trainer.dss == required_dss:
            return render(request, "dss/detail/trainer.html", context)
        else:
            return redirect('dss:read-trainer')
    else:
        return redirect('home')


# Qualification views.
@login_required
def create_qualification(request, pk):
    if not request.user.is_superuser:
        required_admin = DSSAdmin.objects.get(user=request.user)
        required_dss = required_admin.dss
        required_trainer = Trainer.objects.get(id=pk)
        if request.method == 'POST' and required_trainer.dss == required_dss:
            form = CreateQualificationForm(request.POST, request.FILES)
            if form.is_valid():
                qualification = form.save(commit=False)
                qualification.trainer = required_trainer
                if (qualification.calendar == 'BS'):
                    if qualification.started_from_BS:
                        qualification.started_from_AD = bs_to_ad.to_ad(qualification.started_from_BS)
                    else:
                        qualification.started_from_BS = "1975-01-01"
                        qualification.started_from_AD = "1975-01-01"
                    if qualification.ended_on_BS:
                        qualification.ended_on_AD = bs_to_ad.to_ad(qualification.ended_on_BS)
                    else:
                        qualification.ended_on_BS = "1975-01-01"
                        qualification.ended_on_AD = "1975-01-01"
                if (qualification.calendar == 'AD'):
                    if qualification.started_from_AD:
                        qualification.started_from_BS = bs_to_ad.to_ad(qualification.started_from_AD)
                    else:
                        qualification.started_from_AD = "1975-01-01"
                        qualification.started_from_BS = "1975-01-01"
                    if qualification.ended_on_AD:
                        qualification.ended_on_BS = bs_to_ad.to_ad(qualification.ended_on_AD)
                    else:
                        qualification.ended_on_AD = "1975-01-01"
                        qualification.ended_on_BS = "1975-01-01"
                qualification.save()
                return redirect('dss:trainer-detail', pk=required_trainer.id)
        else:
            form = CreateQualificationForm()
        context = {
            'form': form
        }
        return render(request, 'dss/create/qualification.html', context)
    else:
        return redirect('home')


@login_required
def update_qualification(request, pk, pk1):
    if not request.user.is_superuser:
        required_admin = DSSAdmin.objects.get(user=request.user)
        required_dss = required_admin.dss
        required_trainer = Trainer.objects.get(id=pk)
        required_qualification = Qualification.objects.get(id=pk1)
        if request.method == 'POST' and required_trainer.dss == required_dss and required_qualification.trainer == required_trainer:
            form = UpdateQualificationForm(instance=required_qualification, data=request.POST, files=request.FILES)
            if form.is_valid():
                qualification = form.save(commit=False)
                if (qualification.calendar == 'BS'):
                    if qualification.started_from_BS:
                        qualification.started_from_AD = bs_to_ad.to_ad(qualification.started_from_BS)
                    else:
                        qualification.started_from_BS = "1975-01-01"
                        qualification.started_from_AD = "1975-01-01"
                    if qualification.ended_on_BS:
                        qualification.ended_on_AD = bs_to_ad.to_ad(qualification.ended_on_BS)
                    else:
                        qualification.ended_on_BS = "1975-01-01"
                        qualification.ended_on_AD = "1975-01-01"
                if (qualification.calendar == 'AD'):
                    if qualification.started_from_AD:
                        qualification.started_from_BS = bs_to_ad.to_ad(qualification.started_from_AD)
                    else:
                        qualification.started_from_AD = "1975-01-01"
                        qualification.started_from_BS = "1975-01-01"
                    if qualification.ended_on_AD:
                        qualification.ended_on_BS = bs_to_ad.to_ad(qualification.ended_on_AD)
                    else:
                        qualification.ended_on_AD = "1975-01-01"
                        qualification.ended_on_BS = "1975-01-01"
                qualification.save()

                return redirect('dss:trainer-detail', pk=required_trainer.id)
        else:
            form = CreateQualificationForm(instance=required_qualification)
        context = {
            'form': form
        }
        return render(request, 'dss/update/qualification.html', context)
    else:
        return redirect('home')


@login_required
def delete_qualification(request, pk, pk1):
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss
    required_trainer = Trainer.objects.get(id=pk)
    required_qualification = Qualification.objects.get(id=pk1)
    if not request.user.is_superuser and required_trainer.dss == required_dss and required_qualification.trainer == required_trainer:
        context = {
            'pk': pk
        }
        if request.method == "POST":
            required_qualification.delete()
            return redirect('dss:trainer-detail', pk=required_trainer.id)
        return render(request, "dss/delete/qualification.html", context)
    else:
        return redirect('home')


# Experience views.
@login_required
def create_experience(request, pk):
    if not request.user.is_superuser:
        required_admin = DSSAdmin.objects.get(user=request.user)
        required_dss = required_admin.dss
        required_trainer = Trainer.objects.get(id=pk)
        if request.method == 'POST' and required_trainer.dss == required_dss:
            form = CreateExperienceForm(request.POST, request.FILES)
            if form.is_valid():
                experience = form.save(commit=False)
                experience.trainer = required_trainer
                if (experience.calendar == 'BS'):
                    if experience.started_from_BS:
                        experience.started_from_AD = bs_to_ad.to_ad(experience.started_from_BS)
                    else:
                        experience.started_from_BS = "1975-01-01"
                        experience.started_from_AD = "1975-01-01"
                    if experience.ended_on_BS:
                        experience.ended_on_AD = bs_to_ad.to_ad(experience.ended_on_BS)
                    else:
                        experience.ended_on_BS = "1975-01-01"
                        experience.ended_on_AD = "1975-01-01"
                if (experience.calendar == 'AD'):
                    if experience.started_from_AD:
                        experience.started_from_BS = bs_to_ad.to_ad(experience.started_from_AD)
                    else:
                        experience.started_from_AD = "1975-01-01"
                        experience.started_from_BS = "1975-01-01"
                    if experience.ended_on_AD:
                        experience.ended_on_BS = bs_to_ad.to_ad(experience.ended_on_AD)
                    else:
                        experience.ended_on_AD = "1975-01-01"
                        experience.ended_on_BS = "1975-01-01"
                experience.save()
                return redirect('dss:trainer-detail', pk=required_trainer.id)
        else:
            form = CreateExperienceForm()
        context = {
            'form': form
        }
        return render(request, 'dss/create/experience.html', context)
    else:
        return redirect('home')


@login_required
def update_experience(request, pk, pk1):
    if not request.user.is_superuser:
        required_admin = DSSAdmin.objects.get(user=request.user)
        required_dss = required_admin.dss
        required_trainer = Trainer.objects.get(id=pk)
        required_experience = Experience.objects.get(id=pk1)
        if request.method == 'POST' and required_trainer.dss == required_dss:
            form = UpdateExperienceForm(instance=required_experience, data=request.POST, files=request.FILES)
            if form.is_valid():
                experience = form.save(commit=False)
                if (experience.calendar == 'BS'):
                    if experience.started_from_BS:
                        experience.started_from_AD = bs_to_ad.to_ad(experience.started_from_BS)
                    else:
                        experience.started_from_BS = "1975-01-01"
                        experience.started_from_AD = "1975-01-01"
                    if experience.ended_on_BS:
                        experience.ended_on_AD = bs_to_ad.to_ad(experience.ended_on_BS)
                    else:
                        experience.ended_on_BS = "1975-01-01"
                        experience.ended_on_AD = "1975-01-01"
                if (experience.calendar == 'AD'):
                    if experience.started_from_AD:
                        experience.started_from_BS = bs_to_ad.to_ad(experience.started_from_AD)
                    else:
                        experience.started_from_AD = "1975-01-01"
                        experience.started_from_BS = "1975-01-01"
                    if experience.ended_on_AD:
                        experience.ended_on_BS = bs_to_ad.to_ad(experience.ended_on_AD)
                    else:
                        experience.ended_on_AD = "1975-01-01"
                        experience.ended_on_BS = "1975-01-01"
                experience.save()
                return redirect('dss:trainer-detail', pk=required_trainer.id)
        else:
            form = CreateExperienceForm(instance=required_experience)
        context = {
            'form': form
        }
        return render(request, 'dss/update/experience.html', context)
    else:
        return redirect('home')


@login_required
def delete_experience(request, pk, pk1):
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss
    required_trainer = Trainer.objects.get(id=pk)
    required_experience = Experience.objects.get(id=pk1)
    if not request.user.is_superuser and required_trainer.dss == required_dss and required_experience.trainer == required_trainer:
        context = {
            'pk': pk
        }
        if request.method == "POST":
            required_experience.delete()
            return redirect('dss:trainer-detail', pk=required_trainer.id)
        return render(request, "dss/delete/experience.html", context)
    else:
        return redirect('home')


# Training
@login_required
def create_training(request):
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss
    if not request.user.is_superuser:
        if request.method == 'POST':
            form = CreateTrainingForm(data=request.POST, files=request.FILES)
            if form.is_valid():
                training = form.save(commit=False)
                training.dss = required_dss
                training.created_by = request.user
                if (training.calendar == 'BS'):
                    if training.planned_start_date_BS:
                        training.planned_start_date_AD = bs_to_ad.to_ad(training.planned_start_date_BS)
                    else:
                        training.planned_start_date_BS = "1975-01-01"
                        training.planned_start_date_AD = "1975-01-01"
                    if training.planned_end_date_BS:
                        training.planned_end_date_AD = bs_to_ad.to_ad(training.planned_end_date_BS)
                    else:
                        training.planned_end_date_BS = "1975-01-01"
                        training.planned_end_date_AD = "1975-01-01"
                    if training.actual_start_date_BS:
                        training.actual_start_date_AD = bs_to_ad.to_ad(training.actual_start_date_BS)
                    else:
                        training.actual_start_date_BS = "1975-01-01"
                        training.actual_start_date_AD = "1975-01-01"
                    if training.actual_end_date_BS:
                        training.actual_end_date_AD = bs_to_ad.to_ad(training.actual_end_date_BS)
                    else:
                        training.actual_end_date_BS = "1975-01-01"
                        training.actual_end_date_AD = "1975-01-01"
                if (training.calendar == 'AD'):
                    if training.planned_start_date_AD:
                        training.planned_start_date_BS = ad_to_bs.to_bs(training.planned_start_date_AD)
                    else:
                        training.planned_start_date_AD = "1975-01-01"
                        training.planned_start_date_BS = "1975-01-01"
                    if training.planned_end_date_AD:
                        training.planned_end_date_BS = ad_to_bs.to_bs(training.planned_end_date_AD)
                    else:
                        training.planned_end_date_AD = "1975-01-01"
                        training.planned_end_date_BS = "1975-01-01"
                    if training.actual_start_date_AD:
                        training.actual_start_date_BS = ad_to_bs.to_bs(training.actual_start_date_AD)
                    else:
                        training.actual_start_date_AD = "1975-01-01"
                        training.actual_start_date_BS = "1975-01-01"
                    if training.actual_end_date_AD:
                        training.actual_end_date_BS = ad_to_bs.to_bs(training.actual_end_date_AD)
                    else:
                        training.actual_end_date_AD = "1975-01-01"
                        training.actual_end_date_BS = "1975-01-01"
                training.save()
                form.save_m2m()
                return redirect('dss:read-training')
        else:
            form = CreateTrainingForm()
        context = {
            'form': form
        }
        return render(request, 'dss/create/training.html', context)
    else:
        return redirect('home')


@login_required
def read_training(request):
    if not request.user.is_superuser:
        required_admin = DSSAdmin.objects.get(user=request.user)
        required_dss = required_admin.dss
        training_list = Training.objects.filter(dss=required_dss)
        context = {
            'trainings': training_list,
        }
        return render(request, 'dss/read/training.html', context)
    else:
        return redirect('home')


def update_training(request, pk):
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss
    required_training = Training.objects.get(id=pk)
    if not request.user.is_superuser and required_training.dss == required_dss:
        if request.method == 'POST':
            form = UpdateTrainingForm(data=request.POST, files=request.FILES, instance=required_training)
            if form.is_valid():
                training = form.save(commit=False)
                if (training.calendar == 'BS'):
                    if training.planned_start_date_BS:
                        training.planned_start_date_AD = bs_to_ad.to_ad(training.planned_start_date_BS)
                    else:
                        training.planned_start_date_BS = "1975-01-01"
                        training.planned_start_date_AD = "1975-01-01"
                    if training.planned_end_date_BS:
                        training.planned_end_date_AD = bs_to_ad.to_ad(training.planned_end_date_BS)
                    else:
                        training.planned_end_date_BS = "1975-01-01"
                        training.planned_end_date_AD = "1975-01-01"
                    if training.actual_start_date_BS:
                        training.actual_start_date_AD = bs_to_ad.to_ad(training.actual_start_date_BS)
                    else:
                        training.actual_start_date_BS = "1975-01-01"
                        training.actual_start_date_AD = "1975-01-01"
                    if training.actual_end_date_BS:
                        training.actual_end_date_AD = bs_to_ad.to_ad(training.actual_end_date_BS)
                    else:
                        training.actual_end_date_BS = "1975-01-01"
                        training.actual_end_date_AD = "1975-01-01"
                if (training.calendar == 'AD'):
                    if training.planned_start_date_AD:
                        training.planned_start_date_BS = ad_to_bs.to_bs(training.planned_start_date_AD)
                    else:
                        training.planned_start_date_AD = "1975-01-01"
                        training.planned_start_date_BS = "1975-01-01"
                    if training.planned_end_date_AD:
                        training.planned_end_date_BS = ad_to_bs.to_bs(training.planned_end_date_AD)
                    else:
                        training.planned_end_date_AD = "1975-01-01"
                        training.planned_end_date_BS = "1975-01-01"
                    if training.actual_start_date_AD:
                        training.actual_start_date_BS = ad_to_bs.to_bs(training.actual_start_date_AD)
                    else:
                        training.actual_start_date_AD = "1975-01-01"
                        training.actual_start_date_BS = "1975-01-01"
                    if training.actual_end_date_AD:
                        training.actual_end_date_BS = ad_to_bs.to_bs(training.actual_end_date_AD)
                    else:
                        training.actual_end_date_AD = "1975-01-01"
                        training.actual_end_date_BS = "1975-01-01"
                training.save()
                form.save_m2m()
                return redirect('dss:read-training')
        else:
            form = UpdateTrainingForm(instance=required_training)
        context = {
            'form': form
        }
        return render(request, 'dss/create/training.html', context)
    else:
        return redirect('home')


def delete_training(request, pk):
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss
    required_training = Training.objects.get(id=pk)
    if not request.user.is_superuser and required_training.dss == required_dss:
        context = {}
        if request.method == "POST":
            required_training.delete()
            return redirect('dss:read-training')
        return render(request, "dss/delete/training.html", context)
    else:
        return redirect('home')


@login_required
def training_detail(request, pk):
    if not request.user.is_superuser:
        required_admin = DSSAdmin.objects.get(user=request.user)
        required_dss = required_admin.dss
        training = Training.objects.get(id=pk)
        context = {
            'training': training
        }
        if training.dss == required_dss:
            return render(request, "dss/detail/training.html", context)
        else:
            return redirect('dss:read-training')
    else:
        return redirect('home')


# Trainee views.
@login_required
def create_trainee(request):
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss

    if not request.user.is_superuser:
        if request.method == 'POST':
            form = CreateTraineeForm(user=request.user, data=request.POST, files=request.FILES)
            if form.is_valid():
                trainee = form.save(commit=False)
                trainee.dss = required_dss
                trainee.created_by = request.user
                if (trainee.calendar == 'BS'):
                    if trainee.date_of_birth_BS:
                        trainee.date_of_birth_AD = bs_to_ad.to_ad(trainee.date_of_birth_BS)
                    else:
                        trainee.date_of_birth_BS = "1975-01-01"
                        trainee.date_of_birth_AD = "1975-01-01"
                    if trainee.date_of_joining_BS:
                        trainee.date_of_joining_AD = bs_to_ad.to_ad(trainee.date_of_joining_BS)
                    else:
                        trainee.date_of_joining_BS = "1975-01-01"
                        trainee.date_of_joining_AD = "1975-01-01"
                    if trainee.citizenship_issued_date_BS:
                        trainee.citizenship_issued_date_AD = bs_to_ad.to_ad(trainee.citizenship_issued_date_BS)
                    else:
                        trainee.citizenship_issued_date_BS = "1975-01-01"
                        trainee.citizenship_issued_date_AD = "1975-01-01"
                if (trainee.calendar == 'AD'):
                    if trainee.date_of_birth_AD:
                        trainee.date_of_birth_BS = ad_to_bs.to_bs(trainee.date_of_birth_AD)
                    else:
                        trainee.date_of_birth_AD = "1975-01-01"
                        trainee.date_of_birth_BS = "1975-01-01"
                    if trainee.date_of_joining_AD:
                        trainee.date_of_joining_BS = ad_to_bs.to_bs(trainee.date_of_joining_AD)
                    else:
                        trainee.date_of_joining_AD = "1975-01-01"
                        trainee.date_of_joining_BS = "1975-01-01"
                    if trainee.citizenship_issued_date_AD:
                        trainee.citizenship_issued_date_BS = ad_to_bs.to_bs(trainee.citizenship_issued_date_AD)
                    else:
                        trainee.citizenship_issued_date_AD = "1975-01-01"
                        trainee.citizenship_issued_date_BS = "1975-01-01"
                trainee.save()
                return redirect('dss:read-trainee')
        else:
            form = CreateTraineeForm(user=request.user)
        context = {
            'form': form
        }
        return render(request, 'dss/create/trainee.html', context)
    else:
        return redirect('home')


@login_required
def read_trainee(request):
    if not request.user.is_superuser:
        required_admin = DSSAdmin.objects.get(user=request.user)
        required_dss = required_admin.dss
        trainee_list = Trainee.objects.filter(dss=required_dss)
        context = {
            'trainees': trainee_list,
        }
        return render(request, 'dss/read/trainee.html', context)
    else:
        return redirect('home')


@login_required
def update_trainee(request, pk):
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss
    required_trainee = Trainee.objects.get(id=pk)
    if not request.user.is_superuser and required_trainee.dss == required_dss:
        if request.method == 'POST':
            form = UpdateTraineeForm(user=request.user, data=request.POST, files=request.FILES, instance=required_trainee)
            if form.is_valid():
                trainee = form.save(commit=False)
                if (trainee.calendar == 'BS'):
                    if trainee.date_of_birth_BS:
                        trainee.date_of_birth_AD = bs_to_ad.to_ad(trainee.date_of_birth_BS)
                    else:
                        trainee.date_of_birth_BS = "1975-01-01"
                        trainee.date_of_birth_AD = "1975-01-01"
                    if trainee.date_of_joining_BS:
                        trainee.date_of_joining_AD = bs_to_ad.to_ad(trainee.date_of_joining_BS)
                    else:
                        trainee.date_of_joining_BS = "1975-01-01"
                        trainee.date_of_joining_AD = "1975-01-01"
                    if trainee.citizenship_issued_date_BS:
                        trainee.citizenship_issued_date_AD = bs_to_ad.to_ad(trainee.citizenship_issued_date_BS)
                    else:
                        trainee.citizenship_issued_date_BS = "1975-01-01"
                        trainee.citizenship_issued_date_AD = "1975-01-01"
                if (trainee.calendar == 'AD'):
                    if trainee.date_of_birth_AD:
                        trainee.date_of_birth_BS = ad_to_bs.to_bs(trainee.date_of_birth_AD)
                    else:
                        trainee.date_of_birth_AD = "1975-01-01"
                        trainee.date_of_birth_BS = "1975-01-01"
                    if trainee.date_of_joining_AD:
                        trainee.date_of_joining_BS = ad_to_bs.to_bs(trainee.date_of_joining_AD)
                    else:
                        trainee.date_of_joining_AD = "1975-01-01"
                        trainee.date_of_joining_BS = "1975-01-01"
                    if trainee.citizenship_issued_date_AD:
                        trainee.citizenship_issued_date_BS = ad_to_bs.to_bs(trainee.citizenship_issued_date_AD)
                    else:
                        trainee.citizenship_issued_date_AD = "1975-01-01"
                        trainee.citizenship_issued_date_BS = "1975-01-01"
                trainee.save()
                return redirect('dss:read-trainee')
        else:
            form = UpdateTraineeForm(user=request.user, instance=required_trainee)
        context = {
            'form': form
        }
        return render(request, 'dss/update/trainee.html', context)
    else:
        return redirect('home')


@login_required
def delete_trainee(request, pk):
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss
    required_trainee = Trainee.objects.get(id=pk)
    if not request.user.is_superuser and required_trainee.dss == required_dss:
        context = {}
        if request.method == "POST":
            required_trainee.delete()
            return redirect('dss:read-trainee')
        return render(request, "dss/delete/trainee.html", context)
    else:
        return redirect('home')


@login_required
def trainee_detail(request, pk):
    if not request.user.is_superuser:
        required_admin = DSSAdmin.objects.get(user=request.user)
        required_dss = required_admin.dss
        trainee = Trainee.objects.get(id=pk)
        context = {
            'trainee': trainee
        }
        if trainee.dss == required_dss:
            return render(request, "dss/detail/trainee.html", context)
        else:
            return redirect('dss:read-trainee')
    else:
        return redirect('home')


# Staff views.
@login_required
def create_staff(request):
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss

    if not request.user.is_superuser:
        if request.method == 'POST':
            form = CreateStaffForm(request.POST, request.FILES)
            if form.is_valid():
                staff = form.save(commit=False)
                staff.dss = required_dss
                staff.created_by = request.user
                if (staff.calendar == 'BS'):
                    if staff.date_of_birth_BS:
                        staff.date_of_birth_AD = bs_to_ad.to_ad(staff.date_of_birth_BS)
                    else:
                        staff.date_of_birth_BS = "1975-01-01"
                        staff.date_of_birth_AD = "1975-01-01"
                    if staff.date_of_joining_BS:
                        staff.date_of_joining_AD = bs_to_ad.to_ad(staff.date_of_joining_BS)
                    else:
                        staff.date_of_joining_BS = "1975-01-01"
                        staff.date_of_joining_AD = "1975-01-01"
                    if staff.citizenship_issued_date_BS:
                        staff.citizenship_issued_date_AD = bs_to_ad.to_ad(staff.citizenship_issued_date_BS)
                    else:
                        staff.citizenship_issued_date_BS = "1975-01-01"
                        staff.citizenship_issued_date_AD = "1975-01-01"
                if (staff.calendar == 'AD'):
                    if staff.date_of_birth_AD:
                        staff.date_of_birth_BS = ad_to_bs.to_bs(staff.date_of_birth_AD)
                    else:
                        staff.date_of_birth_AD = "1975-01-01"
                        staff.date_of_birth_BS = "1975-01-01"
                    if staff.date_of_joining_AD:
                        staff.date_of_joining_BS = ad_to_bs.to_bs(staff.date_of_joining_AD)
                    else:
                        staff.date_of_joining_AD = "1975-01-01"
                        staff.date_of_joining_BS = "1975-01-01"
                    if staff.citizenship_issued_date_AD:
                        staff.citizenship_issued_date_BS = ad_to_bs.to_bs(staff.citizenship_issued_date_AD)
                    else:
                        staff.citizenship_issued_date_AD = "1975-01-01"
                        staff.citizenship_issued_date_BS = "1975-01-01"
                staff.save()
                return redirect('dss:read-staff')
        else:
            form = CreateStaffForm()
        context = {
            'form': form
        }
        return render(request, 'dss/create/staff.html', context)
    else:
        return redirect('home')


@login_required
def read_staff(request):
    if not request.user.is_superuser:
        required_admin = DSSAdmin.objects.get(user=request.user)
        required_dss = required_admin.dss
        staff_list = Staff.objects.filter(dss=required_dss)
        context = {
            'staffs': staff_list,
        }
        return render(request, 'dss/read/staff.html', context)
    else:
        return redirect('home')


@login_required
def update_staff(request, pk):
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss
    required_staff = Staff.objects.get(id=pk)
    if not request.user.is_superuser and required_staff.dss == required_dss:
        if request.method == 'POST':
            form = UpdateStaffForm(data=request.POST, files=request.FILES, instance=required_staff)
            if form.is_valid():
                staff = form.save(commit=False)
                if (staff.calendar == 'BS'):
                    if staff.date_of_birth_BS:
                        staff.date_of_birth_AD = bs_to_ad.to_ad(staff.date_of_birth_BS)
                    else:
                        staff.date_of_birth_BS = "1975-01-01"
                        staff.date_of_birth_AD = "1975-01-01"
                    if staff.date_of_joining_BS:
                        staff.date_of_joining_AD = bs_to_ad.to_ad(staff.date_of_joining_BS)
                    else:
                        staff.date_of_joining_BS = "1975-01-01"
                        staff.date_of_joining_AD = "1975-01-01"
                    if staff.citizenship_issued_date_BS:
                        staff.citizenship_issued_date_AD = bs_to_ad.to_ad(staff.citizenship_issued_date_BS)
                    else:
                        staff.citizenship_issued_date_BS = "1975-01-01"
                        staff.citizenship_issued_date_AD = "1975-01-01"
                if (staff.calendar == 'AD'):
                    if staff.date_of_birth_AD:
                        staff.date_of_birth_BS = ad_to_bs.to_bs(staff.date_of_birth_AD)
                    else:
                        staff.date_of_birth_AD = "1975-01-01"
                        staff.date_of_birth_BS = "1975-01-01"
                    if staff.date_of_joining_AD:
                        staff.date_of_joining_BS = ad_to_bs.to_bs(staff.date_of_joining_AD)
                    else:
                        staff.date_of_joining_AD = "1975-01-01"
                        staff.date_of_joining_BS = "1975-01-01"
                    if staff.citizenship_issued_date_AD:
                        staff.citizenship_issued_date_BS = ad_to_bs.to_bs(staff.citizenship_issued_date_AD)
                    else:
                        staff.citizenship_issued_date_AD = "1975-01-01"
                        staff.citizenship_issued_date_BS = "1975-01-01"
                staff.save()
                return redirect('dss:read-staff')
        else:
            form = UpdateStaffForm(instance=required_staff)
        context = {
            'form': form
        }
        return render(request, 'dss/update/staff.html', context)
    else:
        return redirect('home')


@login_required
def delete_staff(request, pk):
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss
    required_staff = Staff.objects.get(id=pk)
    if not request.user.is_superuser and required_staff.dss == required_dss:
        context = {}
        if request.method == "POST":
            required_staff.delete()
            return redirect('dss:read-staff')
        return render(request, "dss/delete/staff.html", context)
    else:
        return redirect('home')


@login_required
def staff_detail(request, pk):
    if not request.user.is_superuser:
        required_admin = DSSAdmin.objects.get(user=request.user)
        required_dss = required_admin.dss
        staff = Staff.objects.get(id=pk)
        context = {
            'staff': staff
        }
        if staff.dss == required_dss:
            return render(request, "dss/detail/staff.html", context)
        else:
            return redirect('dss:read-staff')
    else:
        return redirect('home')


# Test views.
@login_required
def create_test(request, pk, pk1):

    required_course_class = CourseClass.objects.get(id=pk)
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss
    required_trainee = Trainee.objects.get(id=pk1)
    required_trainees = Trainee.objects.filter(course_class=required_course_class)

    if not request.user.is_superuser:
        if request.method == 'POST':
            form = CreateTestForm(request.POST, request.FILES)
            if form.is_valid():
                test = form.save(commit=False)
                test.course_class = required_course_class
                test.dss = required_dss
                test.trainee = required_trainee
                if (test.calendar == 'BS'):
                    if test.date_of_application_BS:
                        test.date_of_application_AD = bs_to_ad.to_ad(test.date_of_application_BS)
                    else:
                        test.date_of_application_BS = "1975-01-01"
                        test.date_of_application_AD = "1975-01-01"
                    if test.date_of_exam_BS:
                        test.date_of_exam_AD = bs_to_ad.to_ad(test.date_of_exam_AD)
                    else:
                        test.date_of_exam_BS = "1975-01-01"
                        test.date_of_exam_AD = "1975-01-01"
                    if test.date_of_result_BS:
                        test.date_of_result_AD = bs_to_ad.to_ad(test.date_of_result_BS)
                    else:
                        test.date_of_result_BS = "1975-01-01"
                        test.date_of_result_AD = "1975-01-01"
                if (test.calendar == 'AD'):
                    if test.date_of_application_AD:
                        test.date_of_application_BS = ad_to_bs.to_bs(test.date_of_application_BS)
                    else:
                        test.date_of_application_AD = "1975-01-01"
                        test.date_of_application_BS = "1975-01-01"
                    if test.date_of_exam_AD:
                        test.date_of_exam_BS = ad_to_bs.to_bs(test.date_of_exam_AD)
                    else:
                        test.date_of_exam_AD = "1975-01-01"
                        test.date_of_exam_BS = "1975-01-01"
                    if test.date_of_result_AD:
                        test.date_of_result_BS = ad_to_bs.to_bs(test.date_of_result_BS)
                    else:
                        test.date_of_result_AD = "1975-01-01"
                        test.date_of_result_BS = "1975-01-01"
                test.save()
                return redirect('dss:course-class-detail', pk=pk)
        else:
            form = CreateTestForm()
        context = {
            'form': form
        }
        if required_trainee in required_trainees:
            return render(request, 'dss/create/test.html', context)
        else:
            return redirect('dss:course-class-detail', pk=pk)
    else:
        return redirect('home')


@login_required
def update_test(request, pk, pk1, pk2):
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss
    required_course_class = CourseClass.objects.get(id=pk)
    required_trainee = Trainee.objects.get(id=pk1)
    required_test = Test.objects.get(id=pk2)
    required_trainees = Trainee.objects.filter(course_class=required_course_class)

    if not request.user.is_superuser and required_test.course_class == required_course_class and required_test.dss == required_dss:
        if request.method == 'POST':
            form = UpdateTestForm(data=request.POST, files=request.FILES, instance=required_test)
            if form.is_valid():
                test = form.save(commit=False)
                if (test.calendar == 'BS'):
                    if test.date_of_application_BS:
                        test.date_of_application_AD = bs_to_ad.to_ad(test.date_of_application_BS)
                    else:
                        test.date_of_application_BS = "1975-01-01"
                        test.date_of_application_AD = "1975-01-01"
                    if test.date_of_exam_BS:
                        test.date_of_exam_AD = bs_to_ad.to_ad(test.date_of_exam_AD)
                    else:
                        test.date_of_exam_BS = "1975-01-01"
                        test.date_of_exam_AD = "1975-01-01"
                    if test.date_of_result_BS:
                        test.date_of_result_AD = bs_to_ad.to_ad(test.date_of_result_BS)
                    else:
                        test.date_of_result_BS = "1975-01-01"
                        test.date_of_result_AD = "1975-01-01"
                if (test.calendar == 'AD'):
                    if test.date_of_application_AD:
                        test.date_of_application_BS = ad_to_bs.to_bs(test.date_of_application_BS)
                    else:
                        test.date_of_application_AD = "1975-01-01"
                        test.date_of_application_BS = "1975-01-01"
                    if test.date_of_exam_AD:
                        test.date_of_exam_BS = ad_to_bs.to_bs(test.date_of_exam_AD)
                    else:
                        test.date_of_exam_AD = "1975-01-01"
                        test.date_of_exam_BS = "1975-01-01"
                    if test.date_of_result_AD:
                        test.date_of_result_BS = ad_to_bs.to_bs(test.date_of_result_BS)
                    else:
                        test.date_of_result_AD = "1975-01-01"
                        test.date_of_result_BS = "1975-01-01"
                test.save()
                return redirect('dss:course-class-detail', pk=pk)
        else:
            form = UpdateTestForm(instance=required_test)
        context = {
            'form': form
        }
        if required_test.trainee in required_trainees:
            return render(request, 'dss/update/test.html', context)
        else:
            return redirect('dss:course-class-detail', pk=pk)
    else:
        return redirect('home')


@login_required
def delete_test(request, pk, pk1, pk2):
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss
    required_course_class = CourseClass.objects.get(id=pk)
    required_trainee = Trainee.objects.get(id=pk1)
    required_test = Test.objects.get(id=pk2)

    if not request.user.is_superuser and required_test.course_class == required_course_class and required_test.dss == required_dss:
        context = {
            'pk': pk
        }
        if request.method == "POST":
            required_test.delete()
            return redirect('dss:course-class-detail', pk=pk)
        return render(request, "dss/delete/test.html", context)
    else:
        return redirect('home')


@login_required
def test_detail(request, pk, pk1, pk2):
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss
    required_course_class = CourseClass.objects.get(id=pk)
    required_trainee = Trainee.objects.get(id=pk1)
    required_test = Test.objects.get(id=pk2)
    required_trainees = Trainee.objects.filter(course_class=required_course_class)

    if not request.user.is_superuser and required_test.course_class == required_course_class:
        test = required_test
        context = {
            'test': test
        }
        if test.dss == required_dss:
            if test.trainee in required_trainees:
                return render(request, "dss/detail/test.html", context)
            else:
                return redirect('dss:course-class-detail', pk=pk)
        else:
            return redirect('dss:course-class-detail', pk=pk)
    else:
        return redirect('home')


# Employment views.
@login_required
def create_employment(request, pk, pk1):

    required_course_class = CourseClass.objects.get(id=pk)
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss
    required_trainee = Trainee.objects.get(id=pk1)
    required_trainees = Trainee.objects.filter(course_class=required_course_class)

    if not request.user.is_superuser:
        if request.method == 'POST':
            form = CreateEmploymentForm(request.POST, request.FILES)
            if form.is_valid():
                employment = form.save(commit=False)
                employment.course_class = required_course_class
                employment.dss = required_dss
                employment.trainee = required_trainee
                if (employment.calendar == 'BS'):
                    if employment.date_of_call_BS:
                        employment.date_of_call_AD = bs_to_ad.to_ad(employment.date_of_call_BS)
                    else:
                        employment.date_of_call_BS = "1975-01-01"
                        employment.date_of_call_AD = "1975-01-01"
                    if employment.start_date_BS:
                        employment.start_date_AD = bs_to_ad.to_ad(employment.start_date_BS)
                    else:
                        employment.start_date_BS = "1975-01-01"
                        employment.start_date_AD = "1975-01-01"
                    if employment.end_date_BS:
                        employment.end_date_AD = bs_to_ad.to_ad(employment.end_date_BS)
                    else:
                        employment.end_date_BS = "1975-01-01"
                        employment.end_date_AD = "1975-01-01"
                if (employment.calendar == 'AD'):
                    if employment.date_of_call_AD:
                        employment.date_of_call_BS = ad_to_bs.to_bs(employment.date_of_call_AD)
                    else:
                        employment.date_of_call_AD = "1975-01-01"
                        employment.date_of_call_BS = "1975-01-01"
                    if employment.start_date_AD:
                        employment.start_date_BS = ad_to_bs.to_bs(employment.start_date_AD)
                    else:
                        employment.start_date_AD = "1975-01-01"
                        employment.start_date_BS = "1975-01-01"
                    if employment.end_date_AD:
                        employment.end_date_BS = ad_to_bs.to_bs(employment.end_date_AD)
                    else:
                        employment.end_date_AD = "1975-01-01"
                        employment.end_date_BS = "1975-01-01"
                employment.save()
                return redirect('dss:course-class-detail', pk=pk)
        else:
            form = CreateEmploymentForm()
        context = {
            'form': form
        }
        if required_trainee in required_trainees:
            return render(request, 'dss/create/employment.html', context)
        else:
            return redirect('dss:course-class-detail', pk=pk)
    else:
        return redirect('home')


@login_required
def update_employment(request, pk, pk1, pk2):
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss
    required_course_class = CourseClass.objects.get(id=pk)
    required_trainee = Trainee.objects.get(id=pk1)
    required_employment = Employment.objects.get(id=pk2)
    required_trainees = Trainee.objects.filter(course_class=required_course_class)

    if not request.user.is_superuser and required_employment.course_class == required_course_class and required_employment.dss == required_dss:
        if request.method == 'POST':
            form = UpdateEmploymentForm(data=request.POST, files=request.FILES, instance=required_employment)
            if form.is_valid():
                employment = form.save(commit=False)
                if (employment.calendar == 'BS'):
                    if employment.date_of_call_BS:
                        employment.date_of_call_AD = bs_to_ad.to_ad(employment.date_of_call_BS)
                    else:
                        employment.date_of_call_BS = "1975-01-01"
                        employment.date_of_call_AD = "1975-01-01"
                    if employment.start_date_BS:
                        employment.start_date_AD = bs_to_ad.to_ad(employment.start_date_BS)
                    else:
                        employment.start_date_BS = "1975-01-01"
                        employment.start_date_AD = "1975-01-01"
                    if employment.end_date_BS:
                        employment.end_date_AD = bs_to_ad.to_ad(employment.end_date_BS)
                    else:
                        employment.end_date_BS = "1975-01-01"
                        employment.end_date_AD = "1975-01-01"
                if (employment.calendar == 'AD'):
                    if employment.date_of_call_AD:
                        employment.date_of_call_BS = ad_to_bs.to_bs(employment.date_of_call_AD)
                    else:
                        employment.date_of_call_AD = "1975-01-01"
                        employment.date_of_call_BS = "1975-01-01"
                    if employment.start_date_AD:
                        employment.start_date_BS = ad_to_bs.to_bs(employment.start_date_AD)
                    else:
                        employment.start_date_AD = "1975-01-01"
                        employment.start_date_BS = "1975-01-01"
                    if employment.end_date_AD:
                        employment.end_date_BS = ad_to_bs.to_bs(employment.end_date_AD)
                    else:
                        employment.end_date_AD = "1975-01-01"
                        employment.end_date_BS = "1975-01-01"
                employment.save()
                return redirect('dss:course-class-detail', pk=pk)
        else:
            form = UpdateEmploymentForm(instance=required_employment)
        context = {
            'form': form
        }
        if required_employment.trainee in required_trainees:
            return render(request, 'dss/update/employment.html', context)
        else:
            return redirect('dss:course-class-detail', pk=pk)
    else:
        return redirect('home')


@login_required
def delete_employment(request, pk, pk1, pk2):
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss
    required_course_class = CourseClass.objects.get(id=pk)
    required_trainee = Trainee.objects.get(id=pk1)
    required_employment = Employment.objects.get(id=pk2)

    if not request.user.is_superuser and required_employment.course_class == required_course_class and required_employment.dss == required_dss:
        context = {
            'pk': pk
        }
        if request.method == "POST":
            required_employment.delete()
            return redirect('dss:course-class-detail', pk=pk)
        return render(request, "dss/delete/employment.html", context)
    else:
        return redirect('home')


@login_required
def employment_detail(request, pk, pk1, pk2):
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss
    required_course_class = CourseClass.objects.get(id=pk)
    required_trainee = Trainee.objects.get(id=pk1)
    required_employment = Employment.objects.get(id=pk2)
    required_trainees = Trainee.objects.filter(course_class=required_course_class)

    if not request.user.is_superuser and required_employment.course_class == required_course_class:
        employment = required_employment
        context = {
            'employment': employment
        }
        if employment.dss == required_dss:
            if employment.trainee in required_trainees:
                return render(request, "dss/detail/employment.html", context)
            else:
                return redirect('dss:course-class-detail', pk=pk)
        else:
            return redirect('dss:course-class-detail', pk=pk)
    else:
        return redirect('home')


# Employment Log
def employment_log(request, pk, pk1):
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss
    required_course_class = CourseClass.objects.get(id=pk)
    required_trainee = Trainee.objects.get(id=pk1)

    if not request.user.is_superuser and required_trainee.course_class == required_course_class:
        employments = Employment.objects.filter(Q(course_class=required_course_class) & Q(trainee=required_trainee))
        context = {
            'required_course_class': required_course_class,
            'required_trainee': required_trainee,
            'employments': employments
        }
        if required_trainee.dss == required_dss:
            return render(request, "dss/log/employment.html", context)
        else:
            return redirect('dss:read-course-class')
    else:
        return redirect('home')


# Activity views.
@login_required
def create_activity(request):
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss

    if not request.user.is_superuser:
        if request.method == 'POST':
            form = CreateActivityForm(request.POST, request.FILES)
            if form.is_valid():
                activity = form.save(commit=False)
                activity.dss = required_dss
                activity.created_by = request.user
                if (activity.calendar == 'BS'):
                    if activity.planned_start_date_BS:
                        activity.planned_start_date_AD = bs_to_ad.to_ad(activity.planned_start_date_BS)
                    else:
                        activity.planned_start_date_BS = "1975-01-01"
                        activity.planned_start_date_AD = "1975-01-01"
                    if activity.planned_end_date_BS:
                        activity.planned_end_date_AD = bs_to_ad.to_ad(activity.planned_end_date_BS)
                    else:
                        activity.planned_end_date_BS = "1975-01-01"
                        activity.planned_end_date_AD = "1975-01-01"
                    if activity.actual_start_date_BS:
                        activity.actual_start_date_AD = bs_to_ad.to_ad(activity.actual_start_date_BS)
                    else:
                        activity.actual_start_date_BS = "1975-01-01"
                        activity.actual_start_date_AD = "1975-01-01"
                    if activity.actual_end_date_BS:
                        activity.actual_end_date_AD = bs_to_ad.to_ad(activity.actual_end_date_BS)
                    else:
                        activity.actual_end_date_BS = "1975-01-01"
                        activity.actual_end_date_AD = "1975-01-01"
                if (activity.calendar == 'AD'):
                    if activity.planned_start_date_AD:
                        activity.planned_start_date_BS = ad_to_bs.to_bs(activity.planned_start_date_AD)
                    else:
                        activity.planned_start_date_AD = "1975-01-01"
                        activity.planned_start_date_BS = "1975-01-01"
                    if activity.planned_end_date_AD:
                        activity.planned_end_date_BS = ad_to_bs.to_bs(activity.planned_end_date_AD)
                    else:
                        activity.planned_end_date_AD = "1975-01-01"
                        activity.planned_end_date_BS = "1975-01-01"
                    if activity.actual_start_date_AD:
                        activity.actual_start_date_BS = ad_to_bs.to_bs(activity.actual_start_date_AD)
                    else:
                        activity.actual_start_date_AD = "1975-01-01"
                        activity.actual_start_date_BS = "1975-01-01"
                    if activity.actual_end_date_AD:
                        activity.actual_end_date_BS = ad_to_bs.to_bs(activity.actual_end_date_AD)
                    else:
                        activity.actual_end_date_AD = "1975-01-01"
                        activity.actual_end_date_BS = "1975-01-01"
                activity.save()
                return redirect('dss:read-activity')
        else:
            form = CreateActivityForm()
        context = {
            'form': form
        }
        return render(request, 'dss/create/activity.html', context)
    else:
        return redirect('home')


@login_required
def read_activity(request):
    if not request.user.is_superuser:
        required_admin = DSSAdmin.objects.get(user=request.user)
        required_dss = required_admin.dss
        activity_list = Activity.objects.filter(Q(dss=required_dss))
        context = {
            'activities': activity_list,
        }
        return render(request, 'dss/read/activity.html', context)
    else:
        return redirect('home')


@login_required
def update_activity(request, pk):
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss
    required_activity = Activity.objects.get(id=pk)
    if not request.user.is_superuser and required_activity.dss == required_dss:
        if request.method == 'POST':
            form = UpdateActivityForm(data=request.POST, files=request.FILES, instance=required_activity)
            if form.is_valid():
                activity = form.save(commit=False)
                if (activity.calendar == 'BS'):
                    if activity.planned_start_date_BS:
                        activity.planned_start_date_AD = bs_to_ad.to_ad(activity.planned_start_date_BS)
                    else:
                        activity.planned_start_date_BS = "1975-01-01"
                        activity.planned_start_date_AD = "1975-01-01"
                    if activity.planned_end_date_BS:
                        activity.planned_end_date_AD = bs_to_ad.to_ad(activity.planned_end_date_BS)
                    else:
                        activity.planned_end_date_BS = "1975-01-01"
                        activity.planned_end_date_AD = "1975-01-01"
                    if activity.actual_start_date_BS:
                        activity.actual_start_date_AD = bs_to_ad.to_ad(activity.actual_start_date_BS)
                    else:
                        activity.actual_start_date_BS = "1975-01-01"
                        activity.actual_start_date_AD = "1975-01-01"
                    if activity.actual_end_date_BS:
                        activity.actual_end_date_AD = bs_to_ad.to_ad(activity.actual_end_date_BS)
                    else:
                        activity.actual_end_date_BS = "1975-01-01"
                        activity.actual_end_date_AD = "1975-01-01"
                if (activity.calendar == 'AD'):
                    if activity.planned_start_date_AD:
                        activity.planned_start_date_BS = ad_to_bs.to_bs(activity.planned_start_date_AD)
                    else:
                        activity.planned_start_date_AD = "1975-01-01"
                        activity.planned_start_date_BS = "1975-01-01"
                    if activity.planned_end_date_AD:
                        activity.planned_end_date_BS = ad_to_bs.to_bs(activity.planned_end_date_AD)
                    else:
                        activity.planned_end_date_AD = "1975-01-01"
                        activity.planned_end_date_BS = "1975-01-01"
                    if activity.actual_start_date_AD:
                        activity.actual_start_date_BS = ad_to_bs.to_bs(activity.actual_start_date_AD)
                    else:
                        activity.actual_start_date_AD = "1975-01-01"
                        activity.actual_start_date_BS = "1975-01-01"
                    if activity.actual_end_date_AD:
                        activity.actual_end_date_BS = ad_to_bs.to_bs(activity.actual_end_date_AD)
                    else:
                        activity.actual_end_date_AD = "1975-01-01"
                        activity.actual_end_date_BS = "1975-01-01"
                activity.save()
                return redirect('dss:read-activity')
        else:
            form = UpdateActivityForm(instance=required_activity)
        context = {
            'form': form
        }
        return render(request, 'dss/update/activity.html', context)
    else:
        return redirect('home')


@login_required
def delete_activity(request, pk):
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss
    required_activity = Activity.objects.get(id=pk)
    if not request.user.is_superuser and required_activity.dss == required_dss:
        context = {}
        if request.method == "POST":
            required_activity.delete()
            return redirect('dss:read-activity')
        return render(request, "dss/delete/activity.html", context)
    else:
        return redirect('home')


@login_required
def activity_detail(request, pk):
    if not request.user.is_superuser:
        required_admin = DSSAdmin.objects.get(user=request.user)
        required_dss = required_admin.dss
        activity = Activity.objects.get(id=pk)
        context = {
            'activity': activity
        }
        if activity.dss == required_dss:
            return render(request, "dss/detail/activity.html", context)
        else:
            return redirect('dss:read-activity')
    else:
        return redirect('home')


# Document views.
@login_required
def create_document(request):
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss

    if not request.user.is_superuser:
        if request.method == 'POST':
            form = CreateDocumentForm(request.POST, request.FILES)
            if form.is_valid():
                document = form.save(commit=False)
                document.dss = required_dss
                document.created_by = request.user
                document.created_on_BS = date.today()
                document.last_updated_on_BS = date.today()
                document.created_on_AD = date.today()
                document.last_updated_on_AD = date.today()
                if (document.calendar == 'BS'):
                    if document.date_of_submission_BS:
                        document.date_of_submission_AD = bs_to_ad.to_ad(document.date_of_submission_BS)
                    else:
                        document.date_of_submission_BS = "1975-01-01"
                        document.date_of_submission_AD = "1975-01-01"
                    if document.created_on_BS:
                        document.created_on_AD = bs_to_ad.to_ad(document.created_on_BS)
                    else:
                        document.created_on_BS = "1975-01-01"
                        document.created_on_AD = "1975-01-01"
                    if document.last_updated_on_BS:
                        document.last_updated_on_AD = bs_to_ad.to_ad(document.last_updated_on_BS)
                    else:
                        document.last_updated_on_BS = "1975-01-01"
                        document.last_updated_on_AD = "1975-01-01"
                if (document.calendar == 'AD'):
                    if document.date_of_submission_AD:
                        document.date_of_submission_BS = ad_to_bs.to_bs(document.date_of_submission_AD)
                    else:
                        document.date_of_submission_AD = "1975-01-01"
                        document.date_of_submission_BS = "1975-01-01"
                    if document.created_on_AD:
                        document.created_on_BS = ad_to_bs.to_bs(document.created_on_AD)
                    else:
                        document.created_on_AD = "1975-01-01"
                        document.created_on_BS = "1975-01-01"
                    if document.last_updated_on_AD:
                        document.last_updated_on_BS = ad_to_bs.to_bs(document.last_updated_on_AD)
                    else:
                        document.last_updated_on_AD = "1975-01-01"
                        document.last_updated_on_BS = "1975-01-01"
                document.save()
                return redirect('dss:read-document')
        else:
            form = CreateDocumentForm()
        context = {
            'form': form
        }
        return render(request, 'dss/create/document.html', context)
    else:
        return redirect('home')


@login_required
def read_document(request):
    if not request.user.is_superuser:
        required_admin = DSSAdmin.objects.get(user=request.user)
        required_dss = required_admin.dss
        document_list = Document.objects.filter(Q(dss=required_dss))
        context = {
            'documents': document_list,
        }
        return render(request, 'dss/read/document.html', context)
    else:
        return redirect('home')


@login_required
def update_document(request, pk):
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss
    required_document = Document.objects.get(id=pk)
    if not request.user.is_superuser and required_document.dss == required_dss:
        if request.method == 'POST':
            form = UpdateDocumentForm(data=request.POST, files=request.FILES, instance=required_document)
            if form.is_valid():
                document = form.save(commit=False)
                document.last_updated_on_BS = date.today()
                document.last_updated_on_AD = date.today()
                if (document.calendar == 'BS'):
                    if document.date_of_submission_BS:
                        document.date_of_submission_AD = bs_to_ad.to_ad(document.date_of_submission_BS)
                    else:
                        document.date_of_submission_BS = "1975-01-01"
                        document.date_of_submission_AD = "1975-01-01"
                    if document.created_on_BS:
                        document.created_on_AD = bs_to_ad.to_ad(document.created_on_BS)
                    else:
                        document.created_on_BS = "1975-01-01"
                        document.created_on_AD = "1975-01-01"
                    if document.last_updated_on_BS:
                        document.last_updated_on_AD = bs_to_ad.to_ad(document.last_updated_on_BS)
                    else:
                        document.last_updated_on_BS = "1975-01-01"
                        document.last_updated_on_AD = "1975-01-01"
                if (document.calendar == 'AD'):
                    if document.date_of_submission_AD:
                        document.date_of_submission_BS = ad_to_bs.to_bs(document.date_of_submission_AD)
                    else:
                        document.date_of_submission_AD = "1975-01-01"
                        document.date_of_submission_BS = "1975-01-01"
                    if document.created_on_AD:
                        document.created_on_BS = ad_to_bs.to_bs(document.created_on_AD)
                    else:
                        document.created_on_AD = "1975-01-01"
                        document.created_on_BS = "1975-01-01"
                    if document.last_updated_on_AD:
                        document.last_updated_on_BS = ad_to_bs.to_bs(document.last_updated_on_AD)
                    else:
                        document.last_updated_on_AD = "1975-01-01"
                        document.last_updated_on_BS = "1975-01-01"
                document.save()
                return redirect('dss:read-document')
        else:
            form = UpdateDocumentForm(instance=required_document)
        context = {
            'form': form
        }
        return render(request, 'dss/update/document.html', context)
    else:
        return redirect('home')


@login_required
def delete_document(request, pk):
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss
    required_document = Document.objects.get(id=pk)
    if not request.user.is_superuser and required_document.dss == required_dss:
        context = {}
        if request.method == "POST":
            required_document.delete()
            return redirect('dss:read-document')
        return render(request, "dss/delete/document.html", context)
    else:
        return redirect('home')


@login_required
def document_detail(request, pk):
    if not request.user.is_superuser:
        required_admin = DSSAdmin.objects.get(user=request.user)
        required_dss = required_admin.dss
        document = Document.objects.get(id=pk)
        context = {
            'document': document
        }
        if document.dss == required_dss:
            return render(request, "dss/detail/document.html", context)
        else:
            return redirect('dss:read-document')
    else:
        return redirect('home')


# Property views.
@login_required
def create_property(request):
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss

    if not request.user.is_superuser:
        if request.method == 'POST':
            form = CreatePropertyForm(request.POST, request.FILES)
            if form.is_valid():
                property_variable = form.save(commit=False)
                property_variable.dss = required_dss
                property_variable.created_by = request.user
                if (property_variable.calendar == 'BS'):
                    if property_variable.date_of_purchase_BS:
                        property_variable.date_of_purchase_AD = bs_to_ad.to_ad(property_variable.date_of_purchase_BS)
                    else:
                        property_variable.date_of_purchase_BS = "1975-01-01"
                        property_variable.date_of_purchase_AD = "1975-01-01"
                if (property_variable.calendar == 'AD'):
                    if property_variable.date_of_purchase_AD:
                        property_variable.date_of_purchase_BS = ad_to_bs.to_bs(property_variable.date_of_purchase_AD)
                    else:
                        property_variable.date_of_purchase_AD = "1975-01-01"
                        property_variable.date_of_purchase_BS = "1975-01-01"
                property_variable.save()
                return redirect('dss:read-property')
        else:
            form = CreatePropertyForm()
        context = {
            'form': form
        }
        return render(request, 'dss/create/property.html', context)
    else:
        return redirect('home')


@login_required
def read_property(request):
    if not request.user.is_superuser:
        required_admin = DSSAdmin.objects.get(user=request.user)
        required_dss = required_admin.dss
        property_list = Property.objects.filter(Q(dss=required_dss))
        context = {
            'properties': property_list,
        }
        return render(request, 'dss/read/property.html', context)
    else:
        return redirect('home')


@login_required
def update_property(request, pk):
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss
    required_property = Property.objects.get(id=pk)
    if not request.user.is_superuser and required_property.dss == required_dss:
        if request.method == 'POST':
            form = UpdatePropertyForm(data=request.POST, files=request.FILES, instance=required_property)
            if form.is_valid():
                property_variable = form.save(commit=False)
                if (property_variable.calendar == 'BS'):
                    if property_variable.date_of_purchase_BS:
                        property_variable.date_of_purchase_AD = bs_to_ad.to_ad(property_variable.date_of_purchase_BS)
                    else:
                        property_variable.date_of_purchase_BS = "1975-01-01"
                        property_variable.date_of_purchase_AD = "1975-01-01"
                if (property_variable.calendar == 'AD'):
                    if property_variable.date_of_purchase_AD:
                        property_variable.date_of_purchase_BS = ad_to_bs.to_bs(property_variable.date_of_purchase_AD)
                    else:
                        property_variable.date_of_purchase_AD = "1975-01-01"
                        property_variable.date_of_purchase_BS = "1975-01-01"
                property_variable.save()
                return redirect('dss:read-property')
        else:
            form = UpdatePropertyForm(instance=required_property)
        context = {
            'form': form
        }
        return render(request, 'dss/update/property.html', context)
    else:
        return redirect('home')


@login_required
def delete_property(request, pk):
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss
    required_property = Property.objects.get(id=pk)
    if not request.user.is_superuser and required_property.dss == required_dss:
        context = {}
        if request.method == "POST":
            required_property.delete()
            return redirect('dss:read-property')
        return render(request, "dss/delete/property.html", context)
    else:
        return redirect('home')


@login_required
def property_detail(request, pk):
    if not request.user.is_superuser:
        required_admin = DSSAdmin.objects.get(user=request.user)
        required_dss = required_admin.dss
        property_variable = Property.objects.get(id=pk)
        context = {
            'property': property_variable
        }
        if property_variable.dss == required_dss:
            return render(request, "dss/detail/property.html", context)
        else:
            return redirect('dss:read-property')
    else:
        return redirect('home')


# Requirement views.
@login_required
def create_requirement(request):
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss

    if not request.user.is_superuser:
        if request.method == 'POST':
            form = CreateRequirementForm(request.POST, request.FILES)
            if form.is_valid():
                requirement_variable = form.save(commit=False)
                requirement_variable.dss = required_dss
                requirement_variable.created_by = request.user
                if (requirement_variable.calendar == 'BS'):
                    if requirement_variable.estimated_date_of_purchase_BS:
                        requirement_variable.estimated_date_of_purchase_AD = bs_to_ad.to_ad(requirement_variable.estimated_date_of_purchase_BS)
                    else:
                        requirement_variable.estimated_date_of_purchase_BS = "1975-01-01"
                        requirement_variable.estimated_date_of_purchase_AD = "1975-01-01"
                if (requirement_variable.calendar == 'AD'):
                    if requirement_variable.estimated_date_of_purchase_AD:
                        requirement_variable.estimated_date_of_purchase_BS = ad_to_bs.to_bs(requirement_variable.estimated_date_of_purchase_AD)
                    else:
                        requirement_variable.estimated_date_of_purchase_AD = "1975-01-01"
                        requirement_variable.estimated_date_of_purchase_BS = "1975-01-01"
                requirement_variable.save()
                return redirect('dss:read-requirement')
        else:
            form = CreateRequirementForm()
        context = {
            'form': form
        }
        return render(request, 'dss/create/requirement.html', context)
    else:
        return redirect('home')


@login_required
def read_requirement(request):
    if not request.user.is_superuser:
        required_admin = DSSAdmin.objects.get(user=request.user)
        required_dss = required_admin.dss
        requirement_list = Requirement.objects.filter(Q(dss=required_dss))
        context = {
            'requirements': requirement_list,
        }
        return render(request, 'dss/read/requirement.html', context)
    else:
        return redirect('home')


@login_required
def update_requirement(request, pk):
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss
    required_requirement = Requirement.objects.get(id=pk)
    if not request.user.is_superuser and required_requirement.dss == required_dss:
        if request.method == 'POST':
            form = UpdateRequirementForm(data=request.POST, files=request.FILES, instance=required_requirement)
            if form.is_valid():
                requirement_variable = form.save(commit=False)
                if (requirement_variable.calendar == 'BS'):
                    if requirement_variable.estimated_date_of_purchase_BS:
                        requirement_variable.estimated_date_of_purchase_AD = bs_to_ad.to_ad(requirement_variable.estimated_date_of_purchase_BS)
                    else:
                        requirement_variable.estimated_date_of_purchase_BS = "1975-01-01"
                        requirement_variable.estimated_date_of_purchase_AD = "1975-01-01"
                if (requirement_variable.calendar == 'AD'):
                    if requirement_variable.estimated_date_of_purchase_AD:
                        requirement_variable.estimated_date_of_purchase_BS = ad_to_bs.to_bs(requirement_variable.estimated_date_of_purchase_AD)
                    else:
                        requirement_variable.estimated_date_of_purchase_AD = "1975-01-01"
                        requirement_variable.estimated_date_of_purchase_BS = "1975-01-01"
                requirement_variable.save()
                return redirect('dss:read-requirement')
        else:
            form = UpdateRequirementForm(instance=required_requirement)
        context = {
            'form': form
        }
        return render(request, 'dss/update/requirement.html', context)
    else:
        return redirect('home')


@login_required
def delete_requirement(request, pk):
    required_admin = DSSAdmin.objects.get(user=request.user)
    required_dss = required_admin.dss
    required_requirement = Requirement.objects.get(id=pk)
    if not request.user.is_superuser and required_requirement.dss == required_dss:
        context = {}
        if request.method == "POST":
            required_requirement.delete()
            return redirect('dss:read-requirement')
        return render(request, "dss/delete/requirement.html", context)
    else:
        return redirect('home')


@login_required
def requirement_detail(request, pk):
    if not request.user.is_superuser:
        required_admin = DSSAdmin.objects.get(user=request.user)
        required_dss = required_admin.dss
        requirement_variable = Requirement.objects.get(id=pk)
        context = {
            'requirement': requirement_variable
        }
        if requirement_variable.dss == required_dss:
            return render(request, "dss/detail/requirement.html", context)
        else:
            return redirect('dss:read-requirement')
    else:
        return redirect('home')


# notifications
@login_required
def course_class_log(request):
    if not request.user.is_superuser:
        required_user = request.user
        required_dss_admin = DSSAdmin.objects.get(user=required_user)
        required_dss = required_dss_admin.dss
        course_classes = CourseClass.objects.filter(dss=required_dss)
        all_notifications = Notification.objects.filter(course_class__in=course_classes)
        context = {
            'notifications': all_notifications
        }
        return render(request, 'dss/log/course_class.html', context)
    else:
        return redirect('home')


# Profile views.
@login_required
def profile(request):
    if not request.user.is_superuser:
        required_admin = DSSAdmin.objects.get(user=request.user)
        required_dss = required_admin.dss
        required_course_classes = CourseClass.objects.filter(user=request.user)
        context = {
            'user': request.user,
            'dss': required_dss,
            'course_classes': required_course_classes
        }
        return render(request, 'dss/profile.html', context)
    else:
        return redirect('home')


@login_required
def edit_profile(request):
    if not request.user.is_superuser:
        required_admin = DSSAdmin.objects.get(user=request.user)
        required_dss = required_admin.dss
        if request.method == 'POST':
            form = UserEditForm(request.POST, request.FILES, instance=request.user)
            dss_form = UserProfileEditForm(request.POST, request.FILES, instance=required_dss)
            if form.is_valid() and dss_form.is_valid():
                form.save()
                dss = dss_form.save(commit=False)
                if (dss.calendar == 'BS'):
                    if dss.date_of_establishment_BS:
                        dss.date_of_establishment_AD = bs_to_ad.to_ad(dss.date_of_establishment_BS)
                    else:
                        dss.date_of_establishment_BS = "1975-01-01"
                        dss.date_of_establishment_AD = "1975-01-01"
                if (dss.calendar == 'AD'):
                    if dss.date_of_establishment_AD:
                        dss.date_of_establishment_BS = ad_to_bs.to_bs(dss.date_of_establishment_AD)
                    else:
                        dss.date_of_establishment_AD = "1975-01-01"
                        dss.date_of_establishment_BS = "1975-01-01"
                dss.save()
                return redirect('dss:profile')
        else:
            form = UserEditForm(instance=request.user)
            dss_form = UserProfileEditForm(instance=required_dss)
        context = {
            'form': form,
            'profile_form': dss_form
        }
        return render(request, 'dss/edit_profile.html', context)
    else:
        return redirect('home')


@login_required
def initial_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            login(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('dss:landing')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'dss/initial_password.html', {
        'form': form
    })
