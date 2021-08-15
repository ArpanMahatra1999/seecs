from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils.encoding import force_text, force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import View

from .forms import CustomUserForm, DSSProfileForm, DSSAdminProfileForm
from .forms import CreateSMTMemberForm, UpdateSMTMemberForm
from .forms import CreateTrainerForm, UpdateTrainerForm
from .forms import CreateTraineeForm, UpdateTraineeForm
from .forms import CreateStaffForm, UpdateStaffForm
from .forms import CreateStakeholderForm, UpdateStakeholderForm
from .forms import CreateCourseForm, UpdateCourseForm
from .forms import CreateTrainingForm, UpdateTrainingForm
from .forms import CreateActivityForm, UpdateActivityForm
from .forms import CreateDocumentForm, UpdateDocumentForm
from .forms import CreatePropertyForm, UpdatePropertyForm
from .forms import CreateRequirementForm, UpdateRequirementForm
from .forms import CreateCourseClassForm, UpdateCourseClassForm
from .forms import CreateQualificationForm, UpdateQualificationForm
from .forms import CreateExperienceForm, UpdateExperienceForm
from .forms import CreateTestForm, UpdateTestForm
from .forms import CreateEmploymentForm, UpdateEmploymentForm
from .settings import EMAIL_HOST_USER
from .utils import generate_token

from dss.models import DSS
from dss_admin.models import DSSAdmin
from smt_member.models import SMTMember
from trainer.models import Trainer, Qualification, Experience
from trainee.models import Trainee
from staff.models import Staff
from stakeholder.models import Stakeholder
from course.models import Course
from training.models import Training
from activity.models import Activity
from document.models import Document
from property.models import Property
from requirement.models import Requirement
from course_class.models import CourseClass, Test, Employment
from location.models import District, Municipality
from notification.models import Notification

from ctevt.date_converter import ad_to_bs
from ctevt.date_converter import bs_to_ad

import datetime


def home(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('landing')
        else:
            return redirect('dss:landing')
    else:
        return redirect('login')


@login_required
def landing(request):
    if request.user.is_superuser:
        dsses = DSS.objects.all()

        stakeholders = Stakeholder.objects.all()

        # For bar graph of stakeholder types
        stakeholderTypes = [
            'Suppliers',
            'Owners',
            'Investors',
            'Creditors',
            'Communities',
            'Trade Unions',
            'Employees',
            'Government Agencies',
            'Customers',
            'Media',
            'None'
        ]
        suppliers = Stakeholder.objects.filter(stakeholder_type="Supplier").count()
        owners = Stakeholder.objects.filter(stakeholder_type="Owner").count()
        investors = Stakeholder.objects.filter(stakeholder_type="Investor").count()
        creditors = Stakeholder.objects.filter(stakeholder_type="Creditor").count()
        communities = Stakeholder.objects.filter(stakeholder_type="Community").count()
        trade_unions = Stakeholder.objects.filter(stakeholder_type="Trade Union").count()
        employees = Stakeholder.objects.filter(stakeholder_type="Employee").count()
        government_agencies = Stakeholder.objects.filter(stakeholder_type="Government Agency").count()
        customers = Stakeholder.objects.filter(stakeholder_type="Customer").count()
        media = Stakeholder.objects.filter(stakeholder_type="Media").count()
        stakeholder_none = Stakeholder.objects.filter(stakeholder_type="None").count()
        stakeholderTypesValues = [suppliers, owners, investors, creditors, communities, trade_unions, employees, government_agencies, customers, media, stakeholder_none]

        # For bar graph of ministries
        ministries_full_name = [
            'Ministry of Defence',
            'Ministry of Home Affairs',
            'Ministry of Foreign Affairs',
            'Ministry of Federal Affairs & General Administration',
            'Ministry of Education, Science and Technology',
            'Ministry of Energy, Water Resources and Irrigation',
            'Ministry of Agriculture and Livestock Development',
            'Ministry of Health and Population',
            'Ministry of Industry, Commerce and Supplies',
            'Ministry of Culture, Tourism and Civil Aviation',
            'Ministry of Forest and Environment',
            'Ministry of Labour, Employment and Social Security',
            'Ministry of Finance',
            'Ministry of Communication and Information Technology',
            'Ministry of Youth and Sports',
            'Ministry of Land Management, Cooperatives and Poverty Alleviation',
            'Ministry of Water Supply',
            'Ministry of Physical Infrastructure and Transportation',
            'Ministry of Urban Development',
            'Ministry of Women, Children and Senior Citizen',
            'Ministry of Law, Justice and Parliamentary Affairs',
            'None'
        ]
        ministries = [
            'MOD', 'MOHA', 'MOFA', 'MOFAGA', 'MOEST', 'MOEWRI', 'MPALD', 'MOHP', 'MOICS', 'MOCTCA', 'MOFE',
            'MOLESS', 'MOF', 'MOCIT', 'MOYS', 'MOLMCPA', 'MOWS', 'MOPIT', 'MOUD', 'MOWCSC', 'MOLJPA', 'None'
        ]
        mod = Stakeholder.objects.filter(ministry='Ministry of Defence').count()
        moha = Stakeholder.objects.filter(ministry='Ministry of Home Affairs').count()
        mofa = Stakeholder.objects.filter(ministry='Ministry of Foreign Affairs').count()
        mofaga = Stakeholder.objects.filter(ministry='Ministry of Federal Affairs & General Administration').count()
        moest = Stakeholder.objects.filter(ministry='Ministry of Education, Science and Technology').count()
        moewri = Stakeholder.objects.filter(ministry='Ministry of Energy, Water Resources and Irrigation').count()
        moald = Stakeholder.objects.filter(ministry='Ministry of Agriculture and Livestock Development').count()
        mohp = Stakeholder.objects.filter(ministry='Ministry of Health and Population').count()
        moics = Stakeholder.objects.filter(ministry='Ministry of Industry, Commerce and Supplies').count()
        moctca = Stakeholder.objects.filter(ministry='Ministry of Culture, Tourism and Civil Aviation').count()
        mofe = Stakeholder.objects.filter(ministry='Ministry of Forest and Environment').count()
        moless = Stakeholder.objects.filter(ministry='Ministry of Labour, Employment and Social Security').count()
        mof = Stakeholder.objects.filter(ministry='Ministry of Finance').count()
        mocit = Stakeholder.objects.filter(ministry='Ministry of Communication and Information Technology').count()
        moys = Stakeholder.objects.filter(ministry='Ministry of Youth and Sports').count()
        molmcpa = Stakeholder.objects.filter(ministry='Ministry of Land Management, Cooperatives and Poverty Alleviation').count()
        mows = Stakeholder.objects.filter(ministry='Ministry of Water Supply').count()
        mopit = Stakeholder.objects.filter(ministry='Ministry of Physical Infrastructure and Transportation').count()
        moud = Stakeholder.objects.filter(ministry='Ministry of Urban Development').count()
        mowcsc = Stakeholder.objects.filter(ministry='Ministry of Women, Children and Senior Citizen').count()
        moljpa = Stakeholder.objects.filter(ministry='Ministry of Law, Justice and Parliamentary Affairs').count()
        ministry_none = Stakeholder.objects.filter(ministry='None').count()
        ministriesValues = [mod, moha, mofa, mofaga, moest, moewri, moald, mohp, moics, moctca, mofe, moless, mof, mocit, moys, molmcpa, mows, mopit, moud, mowcsc, moljpa, ministry_none]

        courses = Course.objects.all()
        courseTypes = [
            'Agriculture',
            'Tourism',
            'Construction'
        ]
        agriculture = Course.objects.filter(type='Agriculture').count()
        tourism = Course.objects.filter(type='Tourism').count()
        construction = Course.objects.filter(type='Construction').count()
        courseTypesValues = [agriculture, tourism, construction]
        smtms = SMTMember.objects.all()
        trainers = Trainer.objects.all()
        trainees = Trainee.objects.all()
        staffs = Staff.objects.all()
        trainings = Training.objects.all()
        properties = Property.objects.all()
        requirements = Requirement.objects.all()
        employees_count = staffs.count() + trainers.count()

        smtms_count, trainers_count, trainees_count, staffs_count, trainings_count, properties_count, requirements_count = [], [], [], [], [], [], []
        for d in dsses:
            smtms_count.append(SMTMember.objects.filter(dss=d).count())
            trainers_count.append(Trainer.objects.filter(dss=d).count())
            trainees_count.append(Trainee.objects.filter(dss=d).count())
            staffs_count.append(Staff.objects.filter(dss=d).count())
            trainings_count.append(Training.objects.filter(dss=d).count())
            properties_count.append(Property.objects.filter(dss=d).count())
            requirements_count.append(Requirement.objects.filter(dss=d).count())

        context = {
            'dsses': dsses,

            'stakeholders': stakeholders,
            'stakeholderTypes': stakeholderTypes,
            'stakeholderTypesValues': stakeholderTypesValues,
            'ministries': ministries,
            'ministriesValues': ministriesValues,

            'courses': courses,
            'courseTypes': courseTypes,
            'courseTypesValues': courseTypesValues,

            'smtms': smtms,
            'trainers': trainers,
            'trainees': trainees,
            'staffs': staffs,
            'trainings': trainings,
            'properties': properties,
            'requirements': requirements,
            'employees_count': employees_count,
            'smtms_count': smtms_count,
            'trainers_count': trainers_count,
            'trainees_count': trainees_count,
            'staffs_count': staffs_count,
            'trainings_count': trainings_count,
            'properties_count': properties_count,
            'requirements_count': requirements_count
        }
        return render(request, 'admin/home.html', context)
    else:
        return redirect('dss:landing')


# DSS views.
@login_required
def create_dss(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = DSSProfileForm(request.POST, request.FILES)
            if form.is_valid():
                dss = form.save(commit=False)
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
                        dss.date_of_establishment_BS = "1975-01-01"
                        dss.date_of_establishment_AD = "1975-01-01"
                dss.save()
                return redirect('read-dss')
        else:
            form = DSSProfileForm()
        context = {
            'form': form
        }
        return render(request, 'admin/create/dss.html', context)
    else:
        return redirect('home')


@login_required
def read_dss(request):
    if request.user.is_superuser:
        dss_list = DSS.objects.all()
        context = {
            'dsses': dss_list,
        }
        return render(request, 'admin/read/dss.html', context)
    else:
        return redirect('home')


@login_required
def dss_detail(request, pk):
    if request.user.is_superuser:
        dss = DSS.objects.get(id=pk)
        smtms = SMTMember.objects.filter(dss=dss)
        trainers = Trainer.objects.filter(dss=dss)
        trainees = Trainee.objects.filter(dss=dss)
        staffs = Staff.objects.filter(dss=dss)
        course_classes = CourseClass.objects.filter(dss=dss)
        activities = Activity.objects.filter(dss=dss)
        documents = Document.objects.filter(dss=dss)
        properties = Property.objects.filter(dss=dss)
        requirements = Requirement.objects.filter(dss=dss)

        context = {
            'dss': dss,
            'smtms': smtms,
            'trainers': trainers,
            'trainees': trainees,
            'staffs': staffs,
            'course_classes': course_classes,
            'activities': activities,
            'documents': documents,
            'properties': properties,
            'requirements': requirements
        }
        return render(request, "admin/detail/dss.html", context)
    else:
        return redirect('home')


# DSS views.
@login_required
def create_dss_admin(request, pk):
    if request.user.is_superuser:
        required_dss = DSS.objects.get(id=pk)
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
                return redirect('read-dss-admin', pk=required_dss.id)
        else:
            form = CustomUserForm()
            profile_form = DSSAdminProfileForm()
        context = {
            'form': form,
            'profile_form': profile_form
        }
        return render(request, 'admin/create/dss_admin.html', context)
    else:
        return redirect('home')


@login_required
def read_dss_admin(request, pk):
    if request.user.is_superuser:
        required_dss = DSS.objects.get(id=pk)
        dss_admin_list = DSSAdmin.objects.filter(dss=required_dss)
        context = {
            'dss': required_dss,
            'dss_admins': dss_admin_list,
        }
        return render(request, 'admin/read/dss_admin.html', context)
    else:
        return redirect('home')


@login_required
def dss_admin_detail(request, pk, pk2):
    required_dss = DSS.objects.get(id=pk)
    required_dss_admin = DSSAdmin.objects.get(id=pk2)
    required_course_classes = CourseClass.objects.filter(user=required_dss_admin.user)
    if request.user.is_superuser and required_dss == required_dss_admin.dss:
        context = {
            'dss': required_dss,
            'dss_admin': required_dss_admin,
            'course_classes': required_course_classes
        }
        return render(request, "admin/detail/dss_admin.html", context)
    else:
        return redirect('home')


# SMT Member views.
@login_required
def create_smt_member(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = CreateSMTMemberForm(request.POST, request.FILES)
            if form.is_valid():
                smt_member = form.save(commit=False)
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
                return redirect('read-smtm')
        else:
            form = CreateSMTMemberForm()
        context = {
            'form': form
        }
        return render(request, "admin/create/smtm.html", context)
    else:
        return redirect('home')


@login_required
def read_smt_member(request):
    if request.user.is_superuser:
        dss_list = DSS.objects.all()
        smtm_list = SMTMember.objects.all()
        context = {
            'dss_list': dss_list,
            'smtms': smtm_list,
        }
        return render(request, 'admin/read/smtm.html', context)
    else:
        return redirect('home')


@login_required
def update_smt_member(request, pk):
    if request.user.is_superuser:
        obj = get_object_or_404(SMTMember, id=pk)
        if request.method == 'POST':
            form = UpdateSMTMemberForm(instance=obj, data=request.POST, files=request.FILES)
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
                return redirect('smtm-detail', pk=pk)
        else:
            form = UpdateSMTMemberForm(instance=obj)
        context = {
            'form': form
        }
        return render(request, 'admin/update/smtm.html', context)
    else:
        return redirect('home')


@login_required
def delete_smt_member(request, pk):
    if request.user.is_superuser:
        context = {}
        obj = get_object_or_404(SMTMember, id=pk)
        if request.method == "POST":
            obj.delete()
            return redirect('read-smtm')
        return render(request, "admin/delete/smtm.html", context)
    else:
        return redirect('home')


@login_required
def smt_member_detail(request, pk):
    if request.user.is_superuser:
        smtm = SMTMember.objects.get(id=pk)
        context = {
            'smtm': smtm
        }
        return render(request, "admin/detail/smtm.html", context)
    else:
        return redirect('home')


# Trainer views.
@login_required
def create_trainer(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = CreateTrainerForm(request.POST, request.FILES)
            if form.is_valid():
                trainer = form.save(commit=False)
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
                return redirect('read-trainer')
        else:
            form = CreateTrainerForm()
        context = {
            'form': form
        }
        return render(request, "admin/create/trainer.html", context)
    else:
        return redirect('home')


@login_required
def read_trainer(request):
    if request.user.is_superuser:
        dss_list = DSS.objects.all()
        trainer_list = Trainer.objects.all()
        context = {
            'dss_list': dss_list,
            'trainers': trainer_list,
        }
        return render(request, 'admin/read/trainer.html', context)
    else:
        return redirect('home')


@login_required
def update_trainer(request, pk):
    if request.user.is_superuser:
        obj = get_object_or_404(Trainer, id=pk)
        if request.method == 'POST':
            form = UpdateTrainerForm(instance=obj, data=request.POST, files=request.FILES)
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
                return redirect('trainer-detail', pk=pk)
        else:
            form = UpdateTrainerForm(instance=obj)
        context = {
            'form': form
        }
        return render(request, 'admin/update/trainer.html', context)
    else:
        return redirect('home')


@login_required
def delete_trainer(request, pk):
    if request.user.is_superuser:
        context = {}
        obj = get_object_or_404(Trainer, id=pk)
        if request.method == "POST":
            obj.delete()
            return redirect('read-trainer')
        return render(request, "admin/delete/trainer.html", context)
    else:
        return redirect('home')


@login_required
def trainer_detail(request, pk):
    if request.user.is_superuser:
        trainer = Trainer.objects.get(id=pk)
        context = {
            'trainer': trainer
        }
        return render(request, "admin/detail/trainer.html", context)
    else:
        return redirect('home')


# Trainee views.
@login_required
def create_trainee(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = CreateTraineeForm(request.POST, request.FILES)
            if form.is_valid():
                trainee = form.save(commit=False)
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
                return redirect('read-trainee')
        else:
            form = CreateTraineeForm()
        context = {
            'form': form
        }
        return render(request, "admin/create/trainee.html", context)
    else:
        return redirect('home')


@login_required
def read_trainee(request):
    if request.user.is_superuser:
        dss_list = DSS.objects.all()
        trainee_list = Trainee.objects.all()
        context = {
            'dss_list': dss_list,
            'trainees': trainee_list,
        }
        return render(request, 'admin/read/trainee.html', context)
    else:
        return redirect('home')


@login_required
def update_trainee(request, pk):
    if request.user.is_superuser:
        obj = get_object_or_404(Trainee, id=pk)
        if request.method == 'POST':
            form = UpdateTraineeForm(instance=obj, data=request.POST, files=request.FILES)
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
                return redirect('trainee-detail', pk=pk)
        else:
            form = UpdateTraineeForm(instance=obj)
        context = {
            'form': form
        }
        return render(request, 'admin/update/trainee.html', context)
    else:
        return redirect('home')


@login_required
def delete_trainee(request, pk):
    if request.user.is_superuser:
        context = {}
        obj = get_object_or_404(Trainee, id=pk)
        if request.method == "POST":
            obj.delete()
            return redirect('read-trainee')
        return render(request, "admin/delete/trainee.html", context)
    else:
        return redirect('home')


@login_required
def trainee_detail(request, pk):
    if request.user.is_superuser:
        trainee = Trainee.objects.get(id=pk)
        context = {
            'trainee': trainee
        }
        return render(request, "admin/detail/trainee.html", context)
    else:
        return redirect('home')


# Staff views.
@login_required
def create_staff(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = CreateStaffForm(request.POST, request.FILES)
            if form.is_valid():
                staff = form.save(commit=False)
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
                return redirect('read-staff')
        else:
            form = CreateStaffForm()
        context = {
            'form': form
        }
        return render(request, "admin/create/staff.html", context)
    else:
        return redirect('home')


@login_required
def read_staff(request):
    if request.user.is_superuser:
        dss_list = DSS.objects.all()
        staff_list = Staff.objects.all()
        context = {
            'dss_list': dss_list,
            'staffs': staff_list,
        }
        return render(request, 'admin/read/staff.html', context)
    else:
        return redirect('home')


@login_required
def update_staff(request, pk):
    if request.user.is_superuser:
        obj = get_object_or_404(Staff, id=pk)
        if request.method == 'POST':
            form = UpdateStaffForm(instance=obj, data=request.POST, files=request.FILES)
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
                return redirect('staff-detail', pk=pk)
        else:
            form = UpdateStaffForm(instance=obj)
        context = {
            'form': form
        }
        return render(request, 'admin/update/staff.html', context)
    else:
        return redirect('home')


@login_required
def delete_staff(request, pk):
    if request.user.is_superuser:
        context = {}
        obj = get_object_or_404(Staff, id=pk)
        if request.method == "POST":
            obj.delete()
            return redirect('read-staff')
        return render(request, "admin/delete/staff.html", context)
    else:
        return redirect('home')


@login_required
def staff_detail(request, pk):
    if request.user.is_superuser:
        staff = Staff.objects.get(id=pk)
        context = {
            'staff': staff
        }
        return render(request, "admin/detail/staff.html", context)
    else:
        return redirect('home')


# Activity views.
@login_required
def create_activity(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = CreateActivityForm(request.POST, request.FILES)
            if form.is_valid():
                activity = form.save(commit=False)
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
                return redirect('read-activity')
        else:
            form = CreateActivityForm()
        context = {'form': form}
        return render(request, 'admin/create/activity.html', context)
    else:
        return redirect('home')


@login_required
def read_activity(request):
    if request.user.is_superuser:
        dss_list = DSS.objects.all()
        activity_list = Activity.objects.all()
        context = {
            'dss_list': dss_list,
            'activities': activity_list
        }
        return render(request, 'admin/read/activity.html', context)
    else:
        return redirect('home')


@login_required
def update_activity(request, pk):
    if request.user.is_superuser:
        obj = get_object_or_404(Activity, id=pk)
        if request.method == 'POST':
            form = UpdateActivityForm(request.POST, instance=obj)
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
                return redirect('activity-detail', pk=pk)
        else:
            form = UpdateActivityForm(instance=obj)
        context = {
            'form': form
        }
        return render(request, 'admin/update/activity.html', context)
    else:
        return redirect('home')


@login_required
def delete_activity(request, pk):
    if request.user.is_superuser:
        context = {}
        obj = get_object_or_404(Activity, id=pk)
        if request.method == "POST":
            obj.delete()
            return redirect('read-activity')
        return render(request, "admin/delete/activity.html", context)
    else:
        return redirect('home')


@login_required
def activity_detail(request, pk):
    if request.user.is_superuser:
        activity = Activity.objects.get(id=pk)
        context = {
            'activity': activity
        }
        return render(request, "admin/detail/activity.html", context)
    else:
        return redirect('home')


# Document views.
@login_required
def create_document(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = CreateDocumentForm(request.POST, request.FILES)
            if form.is_valid():
                document = form.save(commit=False)
                document.created_by = request.user
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
                        document.date_of_submission_BS = ad_to_bs.to_bs(document.date_of_submission_BS)
                    else:
                        document.date_of_submission_AD = "1975-01-01"
                        document.date_of_submission_BS = "1975-01-01"
                    if document.created_on_AD:
                        document.created_on_BS = ad_to_bs.to_bs(document.created_on_BS)
                    else:
                        document.created_on_AD = "1975-01-01"
                        document.created_on_BS = "1975-01-01"
                    if document.last_updated_on_AD:
                        document.last_updated_on_BS = ad_to_bs.to_bs(document.last_updated_on_BS)
                    else:
                        document.last_updated_on_AD = "1975-01-01"
                        document.last_updated_on_BS = "1975-01-01"
                document.save()
                return redirect('read-document')
        else:
            form = CreateDocumentForm()
        context = {'form': form}
        return render(request, 'admin/create/document.html', context)
    else:
        return redirect('home')


@login_required
def read_document(request):
    if request.user.is_superuser:
        dss_list = DSS.objects.all()
        document_list = Document.objects.all()
        context = {
            'dss_list': dss_list,
            'documents': document_list
        }
        return render(request, 'admin/read/document.html', context)
    else:
        return redirect('home')


@login_required
def update_document(request, pk):
    if request.user.is_superuser:
        obj = get_object_or_404(Document, id=pk)
        if request.method == 'POST':
            form = UpdateDocumentForm(request.POST, instance=obj)
            if form.is_valid():
                document = form.save(commit=False)
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
                        document.date_of_submission_BS = ad_to_bs.to_bs(document.date_of_submission_BS)
                    else:
                        document.date_of_submission_AD = "1975-01-01"
                        document.date_of_submission_BS = "1975-01-01"
                    if document.created_on_AD:
                        document.created_on_BS = ad_to_bs.to_bs(document.created_on_BS)
                    else:
                        document.created_on_AD = "1975-01-01"
                        document.created_on_BS = "1975-01-01"
                    if document.last_updated_on_AD:
                        document.last_updated_on_BS = ad_to_bs.to_bs(document.last_updated_on_BS)
                    else:
                        document.last_updated_on_AD = "1975-01-01"
                        document.last_updated_on_BS = "1975-01-01"
                document.save()
                return redirect('document-detail', pk=pk)
        else:
            form = UpdateDocumentForm(instance=obj)
        context = {
            'form': form
        }
        return render(request, 'admin/update/document.html', context)
    else:
        return redirect('home')


@login_required
def delete_document(request, pk):
    if request.user.is_superuser:
        context = {}
        obj = get_object_or_404(Document, id=pk)
        if request.method == "POST":
            obj.delete()
            return redirect('read-document')
        return render(request, "admin/delete/document.html", context)
    else:
        return redirect('home')


@login_required
def document_detail(request, pk):
    if request.user.is_superuser:
        document = Document.objects.get(id=pk)
        context = {
            'document': document
        }
        return render(request, "admin/detail/document.html", context)
    else:
        return redirect('home')


# Property views.
@login_required
def create_property(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = CreatePropertyForm(request.POST, request.FILES)
            if form.is_valid():
                property_variable = form.save(commit=False)
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
                return redirect('read-property')
        else:
            form = CreatePropertyForm()
        context = {'form': form}
        return render(request, 'admin/create/property.html', context)
    else:
        return redirect('home')


@login_required
def read_property(request):
    if request.user.is_superuser:
        dss_list = DSS.objects.all()
        property_list = Property.objects.all()
        context = {
            'dss_list': dss_list,
            'properties': property_list
        }
        return render(request, 'admin/read/property.html', context)
    else:
        return redirect('home')


@login_required
def update_property(request, pk):
    if request.user.is_superuser:
        obj = get_object_or_404(Property, id=pk)
        if request.method == 'POST':
            form = UpdatePropertyForm(request.POST, instance=obj)
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
                return redirect('property-detail', pk=pk)
        else:
            form = UpdatePropertyForm(instance=obj)
        context = {
            'form': form
        }
        return render(request, 'admin/update/property.html', context)
    else:
        return redirect('home')


@login_required
def delete_property(request, pk):
    if request.user.is_superuser:
        context = {}
        obj = get_object_or_404(Property, id=pk)
        if request.method == "POST":
            obj.delete()
            return redirect('read-property')
        return render(request, "admin/delete/property.html", context)
    else:
        return redirect('home')


@login_required
def property_detail(request, pk):
    if request.user.is_superuser:
        property_x = Property.objects.get(id=pk)
        context = {
            'property': property_x
        }
        return render(request, "admin/detail/property.html", context)
    else:
        return redirect('home')


# Requirement views.
@login_required
def create_requirement(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = CreateRequirementForm(request.POST, request.FILES)
            if form.is_valid():
                requirement_variable = form.save(commit=False)
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
                return redirect('read-requirement')
        else:
            form = CreateRequirementForm()
        context = {'form': form}
        return render(request, 'admin/create/requirement.html', context)
    else:
        return redirect('home')


@login_required
def read_requirement(request):
    if request.user.is_superuser:
        dss_list = DSS.objects.all()
        requirement_list = Requirement.objects.all()
        context = {
            'dss_list': dss_list,
            'requirements': requirement_list
        }
        return render(request, 'admin/read/requirement.html', context)
    else:
        return redirect('home')


@login_required
def update_requirement(request, pk):
    if request.user.is_superuser:
        obj = get_object_or_404(Requirement, id=pk)
        if request.method == 'POST':
            form = UpdateRequirementForm(request.POST, instance=obj)
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
                return redirect('requirement-detail', pk=pk)
        else:
            form = UpdateRequirementForm(instance=obj)
        context = {
            'form': form
        }
        return render(request, 'admin/update/requirement.html', context)
    else:
        return redirect('home')


@login_required
def delete_requirement(request, pk):
    if request.user.is_superuser:
        context = {}
        obj = get_object_or_404(Requirement, id=pk)
        if request.method == "POST":
            obj.delete()
            return redirect('read-requirement')
        return render(request, "admin/delete/requirement.html", context)
    else:
        return redirect('home')


@login_required
def requirement_detail(request, pk):
    if request.user.is_superuser:
        requirement = Requirement.objects.get(id=pk)
        context = {
            'requirement': requirement
        }
        return render(request, "admin/detail/requirement.html", context)
    else:
        return redirect('home')


# Stakeholder views.
@login_required
def create_stakeholder(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = CreateStakeholderForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('read-stakeholder')
        else:
            form = CreateStakeholderForm()
        context = {'form': form}
        return render(request, 'admin/create/stakeholder.html', context)
    else:
        return redirect('home')


@login_required
def read_stakeholder(request):
    if request.user.is_superuser:
        stakeholder_list = Stakeholder.objects.all()
        context = {
            'stakeholders': stakeholder_list
        }
        return render(request, 'admin/read/stakeholder.html', context)
    else:
        return redirect('home')


@login_required
def update_stakeholder(request, pk):
    if request.user.is_superuser:
        obj = get_object_or_404(Stakeholder, id=pk)
        if request.method == 'POST':
            form = UpdateStakeholderForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return redirect('stakeholder-detail', pk=pk)
        else:
            form = UpdateStakeholderForm(instance=obj)
        context = {
            'form': form
        }
        return render(request, 'admin/update/stakeholder.html', context)
    else:
        return redirect('home')


@login_required
def delete_stakeholder(request, pk):
    if request.user.is_superuser:
        context = {}
        obj = get_object_or_404(Stakeholder, id=pk)
        if request.method == "POST":
            obj.delete()
            return redirect('read-stakeholder')
        return render(request, "admin/delete/stakeholder.html", context)
    else:
        return redirect('home')


@login_required
def stakeholder_detail(request, pk):
    if request.user.is_superuser:
        stakeholder = Stakeholder.objects.get(id=pk)
        context = {
            'stakeholder': stakeholder
        }
        return render(request, "admin/detail/stakeholder.html", context)
    else:
        return redirect('home')


# Course views.
@login_required
def create_course(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = CreateCourseForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('read-course')
        else:
            form = CreateCourseForm()
        context = {'form': form}
        return render(request, 'admin/create/course.html', context)
    else:
        return redirect('home')


@login_required
def read_course(request):
    if request.user.is_superuser:
        course_list = Course.objects.all()
        context = {
            'courses': course_list
        }
        return render(request, 'admin/read/course.html', context)
    else:
        return redirect('home')


@login_required
def update_course(request, pk):
    if request.user.is_superuser:
        obj = get_object_or_404(Course, id=pk)
        if request.method == 'POST':
            form = UpdateCourseForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return redirect('course-detail', pk=pk)
        else:
            form = UpdateCourseForm(instance=obj)
        context = {
            'form': form
        }
        return render(request, 'admin/update/course.html', context)
    else:
        return redirect('home')


@login_required
def delete_course(request, pk):
    if request.user.is_superuser:
        context = {}
        obj = get_object_or_404(Course, id=pk)
        if request.method == "POST":
            obj.delete()
            return redirect('read-course')
        return render(request, "admin/delete/course.html", context)
    else:
        return redirect('home')


@login_required
def course_detail(request, pk):
    if request.user.is_superuser:
        course = Course.objects.get(id=pk)
        context = {
            'course': course
        }
        return render(request, "admin/detail/course.html", context)
    else:
        return redirect('home')


# Training views.
@login_required
def create_training(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = CreateTrainingForm(request.POST, request.FILES)
            if form.is_valid():
                training = form.save(commit=False)
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
                return redirect('read-training')
        else:
            form = CreateTrainingForm()
        context = {'form': form}
        return render(request, 'admin/create/training.html', context)
    else:
        return redirect('home')


@login_required
def read_training(request):
    if request.user.is_superuser:
        dss_list = DSS.objects.all()
        training_list = Training.objects.all()
        context = {
            'dss_list': dss_list,
            'trainings': training_list
        }
        return render(request, 'admin/read/training.html', context)
    else:
        return redirect('home')


@login_required
def update_training(request, pk):
    if request.user.is_superuser:
        obj = get_object_or_404(Training, id=pk)
        if request.method == 'POST':
            form = UpdateTrainingForm(request.POST, instance=obj)
            if form.is_valid():
                training = form.save(commit=False)
                if (training.calendar == 'BS'):
                    if training.planned_start_date_BS:
                        training.planned_start_date_AD = bs_to_ad.to_ad(training.planned_start_date_BS)
                    else:
                        training.planned_start_date_AD = "1975-01-01"
                        training.planned_start_date_BS = "1975-01-01"
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
                return redirect('training-detail', pk=pk)
        else:
            form = UpdateTrainingForm(instance=obj)
        context = {
            'form': form
        }
        return render(request, 'admin/update/training.html', context)
    else:
        return redirect('home')


@login_required
def delete_training(request, pk):
    if request.user.is_superuser:
        context = {}
        obj = get_object_or_404(Training, id=pk)
        if request.method == "POST":
            obj.delete()
            return redirect('read-training')
        return render(request, "admin/delete/training.html", context)
    else:
        return redirect('home')


@login_required
def training_detail(request, pk):
    if request.user.is_superuser:
        training = Training.objects.get(id=pk)
        context = {
            'training': training
        }
        return render(request, "admin/detail/training.html", context)
    else:
        return redirect('home')


# Course Class views.
@login_required
def create_course_class(request, pk):
    required_course = Course.objects.get(id=pk)
    if request.user.is_superuser:
        if request.method == 'POST':
            form = CreateCourseClassForm(request.POST, request.FILES)
            if form.is_valid():
                course_class = form.save(commit=False)
                course_class.course = required_course
                course_class.user = request.user
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
                notification = Notification(
                    course_class=course_class,
                    message="was created"
                )
                notification.save()
                return redirect('read-course-class', pk=pk)
        else:
            form = CreateCourseClassForm()
        context = {'form': form}
        return render(request, 'admin/create/course_class.html', context)
    else:
        return redirect('home')


@login_required
def read_course_class(request, pk):
    required_course = Course.objects.get(id=pk)
    if request.user.is_superuser:
        course_class_list = CourseClass.objects.filter(course=required_course)
        context = {
            'course': required_course,
            'course_classes': course_class_list
        }
        return render(request, 'admin/read/course_class.html', context)
    else:
        return redirect('home')


@login_required
def update_course_class(request, pk, pk1):
    if request.user.is_superuser:
        obj = get_object_or_404(CourseClass, id=pk1)
        if request.method == 'POST':
            form = UpdateCourseClassForm(request.POST, instance=obj)
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
                notification = Notification(
                    course_class=obj,
                    message="was updated"
                )
                notification.save()
                return redirect('course-class-detail', pk=pk, pk1=pk1)
        else:
            form = UpdateCourseClassForm(instance=obj)
        context = {
            'form': form
        }
        return render(request, 'admin/update/course_class.html', context)
    else:
        return redirect('home')


@login_required
def delete_course_class(request, pk, pk1):
    required_course_class = CourseClass.objects.get(id=pk1)
    if request.user.is_superuser:
        context = {
            'course_class': required_course_class
        }
        obj = get_object_or_404(CourseClass, id=pk1)
        if request.method == "POST":
            obj.delete()
            return redirect('read-course-class', pk=pk)
        return render(request, "admin/delete/course_class.html", context)
    else:
        return redirect('home')


@login_required
def course_class_detail(request, pk, pk1):
    if request.user.is_superuser:
        course_class = CourseClass.objects.get(id=pk1)
        trainees = Trainee.objects.filter(course_class=course_class)
        tests = Test.objects.filter(course_class=course_class)
        employments = Employment.objects.filter(course_class=course_class)
        context = {
            'course_class': course_class,
            'trainees': trainees,
            'tests': tests,
            'employments': employments
        }
        return render(request, "admin/detail/course_class.html", context)
    else:
        return redirect('home')


# Qualification and Experience views.
@login_required
def create_qualification(request, pk):
    required_trainer = Trainer.objects.get(id=pk)
    if request.user.is_superuser:
        if request.method == 'POST':
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
                        qualification.started_from_BS = ad_to_bs.to_bs(qualification.started_from_AD)
                        print("Started from")
                        print(qualification.started_from_BS)
                    else:
                        qualification.started_from_AD = "1975-01-01"
                        qualification.started_from_BS = "1975-01-01"
                    if qualification.ended_on_AD:
                        qualification.ended_on_BS = ad_to_bs.to_bs(qualification.ended_on_AD)
                        print("Ended on")
                        print(qualification.ended_on_BS)
                    else:
                        qualification.ended_on_AD = "1975-01-01"
                        qualification.ended_on_BS = "1975-01-01"
                qualification.save()
                return redirect('read-qualification', pk=pk)
        else:
            form = CreateQualificationForm()
        context = {'form': form}
        return render(request, 'admin/create/qualification.html', context)
    else:
        return redirect('home')


@login_required
def create_experience(request, pk):
    required_trainer = Trainer.objects.get(id=pk)
    if request.user.is_superuser:
        if request.method == 'POST':
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
                        experience.started_from_BS = ad_to_bs.to_bs(experience.started_from_AD)
                    else:
                        experience.started_from_AD = "1975-01-01"
                        experience.started_from_BS = "1975-01-01"
                    if experience.ended_on_AD:
                        experience.ended_on_BS = ad_to_bs.to_bs(experience.ended_on_AD)
                    else:
                        experience.ended_on_AD = "1975-01-01"
                        experience.ended_on_BS = "1975-01-01"
                experience.save()
                return redirect('read-experience', pk=pk)
        else:
            form = CreateExperienceForm()
        context = {'form': form}
        return render(request, 'admin/create/experience.html', context)
    else:
        return redirect('home')


@login_required
def read_qualification(request, pk):
    required_trainer = Trainer.objects.get(id=pk)
    if request.user.is_superuser:
        qualification_list = Qualification.objects.filter(trainer=required_trainer)
        context = {
            'trainer': required_trainer,
            'qualifications': qualification_list
        }
        return render(request, 'admin/read/qualification.html', context)
    else:
        return redirect('home')


@login_required
def read_experience(request, pk):
    required_trainer = Trainer.objects.get(id=pk)
    if request.user.is_superuser:
        experience_list = Experience.objects.filter(trainer=required_trainer)
        context = {
            'trainer': required_trainer,
            'experiences': experience_list
        }
        return render(request, 'admin/read/experience.html', context)
    else:
        return redirect('home')


@login_required
def update_qualification(request, pk, pk1):
    if request.user.is_superuser:
        obj = get_object_or_404(Qualification, id=pk1)
        if request.method == 'POST':
            form = UpdateQualificationForm(request.POST, instance=obj)
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
                        qualification.started_from_BS = ad_to_bs.to_bs(qualification.started_from_AD)
                    else:
                        qualification.started_from_AD = "1975-01-01"
                        qualification.started_from_BS = "1975-01-01"
                    if qualification.ended_on_AD:
                        qualification.ended_on_BS = ad_to_bs.to_bs(qualification.ended_on_AD)
                    else:
                        qualification.ended_on_AD = "1975-01-01"
                        qualification.ended_on_BS = "1975-01-01"
                qualification.save()
                return redirect('qualification-detail', pk=pk, pk1=pk1)
        else:
            form = UpdateQualificationForm(instance=obj)
        context = {
            'form': form
        }
        return render(request, 'admin/update/qualification.html', context)
    else:
        return redirect('home')


@login_required
def update_experience(request, pk, pk1):
    if request.user.is_superuser:
        obj = get_object_or_404(Experience, id=pk1)
        if request.method == 'POST':
            form = UpdateExperienceForm(request.POST, instance=obj)
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
                return redirect('experience-detail', pk=pk, pk1=pk1)
        else:
            form = UpdateExperienceForm(instance=obj)
        context = {
            'form': form
        }
        return render(request, 'admin/update/experience.html', context)
    else:
        return redirect('home')


@login_required
def delete_qualification(request, pk, pk1):
    required_qualification = Qualification.objects.get(id=pk1)
    if request.user.is_superuser:
        context = {
            'qualification': required_qualification
        }
        obj = get_object_or_404(Qualification, id=pk1)
        if request.method == "POST":
            obj.delete()
            return redirect('read-qualification', pk=pk)
        return render(request, "admin/delete/qualification.html", context)
    else:
        return redirect('home')


@login_required
def delete_experience(request, pk, pk1):
    required_experience = Experience.objects.get(id=pk1)
    if request.user.is_superuser:
        context = {
            'experience': required_experience
        }
        obj = get_object_or_404(Experience, id=pk1)
        if request.method == "POST":
            obj.delete()
            return redirect('read-experience', pk=pk)
        return render(request, "admin/delete/experience.html", context)
    else:
        return redirect('home')


@login_required
def qualification_detail(request, pk, pk1):
    if request.user.is_superuser:
        qualification = Qualification.objects.get(id=pk1)
        context = {
            'qualification': qualification
        }
        return render(request, "admin/detail/qualification.html", context)
    else:
        return redirect('home')


@login_required
def experience_detail(request, pk, pk1):
    if request.user.is_superuser:
        experience = Experience.objects.get(id=pk1)
        context = {
            'experience': experience
        }
        return render(request, "admin/detail/experience.html", context)
    else:
        return redirect('home')


# Test views.
@login_required
def create_test(request, pk, pk1):

    required_course_class = CourseClass.objects.get(id=pk)
    required_dss = required_course_class.dss
    required_trainee = Trainee.objects.get(id=pk1)
    required_trainees = Trainee.objects.filter(course_class=required_course_class)

    if request.user.is_superuser:
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
                        test.date_of_application_BS = ad_to_bs.to_bs(test.date_of_application_AD)
                    else:
                        test.date_of_application_AD = "1975-01-01"
                        test.date_of_application_BS = "1975-01-01"
                    if test.date_of_exam_AD:
                        test.date_of_exam_BS = ad_to_bs.to_bs(test.date_of_exam_AD)
                    else:
                        test.date_of_exam_AD = "1975-01-01"
                        test.date_of_exam_BS = "1975-01-01"
                    if test.date_of_result_AD:
                        test.date_of_result_BS = ad_to_bs.to_bs(test.date_of_result_AD)
                    else:
                        test.date_of_result_AD = "1975-01-01"
                        test.date_of_result_BS = "1975-01-01"
                test.save()
                return redirect('course-class-detail', pk=pk)
        else:
            form = CreateTestForm()
        context = {
            'form': form
        }
        if required_trainee in required_trainees:
            return render(request, 'admin/create/test.html', context)
        else:
            return redirect('course-class-detail', pk=pk)
    else:
        return redirect('home')


@login_required
def update_test(request, pk, pk1, pk2):

    required_course_class = CourseClass.objects.get(id=pk)
    required_dss = required_course_class.dss
    required_trainee = Trainee.objects.get(id=pk1)
    required_test = Test.objects.get(id=pk2)
    required_trainees = Trainee.objects.filter(course_class=required_course_class)

    if request.user.is_superuser and required_test.course_class == required_course_class and required_test.dss == required_dss:
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
                        test.date_of_exam_AD = bs_to_ad.to_ad(test.date_of_exam_BS)
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
                        test.date_of_application_BS = ad_to_bs.to_bs(test.date_of_application_AD)
                    else:
                        test.date_of_application_AD = "1975-01-01"
                        test.date_of_application_BS = "1975-01-01"
                    if test.date_of_exam_AD:
                        test.date_of_exam_BS = ad_to_bs.to_bs(test.date_of_exam_AD)
                    else:
                        test.date_of_exam_AD = "1975-01-01"
                        test.date_of_exam_BS = "1975-01-01"
                    if test.date_of_result_AD:
                        test.date_of_result_BS = ad_to_bs.to_bs(test.date_of_result_AD)
                    else:
                        test.date_of_result_AD = "1975-01-01"
                        test.date_of_result_BS = "1975-01-01"
                test.save()
                return redirect('course-class-detail', pk=pk)
        else:
            form = UpdateTestForm(instance=required_test)
        context = {
            'form': form
        }
        if required_test.trainee in required_trainees:
            return render(request, 'admin/update/test.html', context)
        else:
            return redirect('course-class-detail', pk=pk)
    else:
        return redirect('home')


@login_required
def delete_test(request, pk, pk1, pk2):

    required_course_class = CourseClass.objects.get(id=pk)
    required_dss = required_course_class.dss
    required_trainee = Trainee.objects.get(id=pk1)
    required_test = Test.objects.get(id=pk2)

    if request.user.is_superuser and required_test.course_class == required_course_class and required_test.dss == required_dss:
        context = {
            'pk': pk
        }
        if request.method == "POST":
            required_test.delete()
            return redirect('course-class-detail', pk=pk)
        return render(request, "admin/delete/test.html", context)
    else:
        return redirect('home')


@login_required
def test_detail(request, pk, pk1, pk2):

    required_course_class = CourseClass.objects.get(id=pk)
    required_dss = required_course_class.dss
    required_trainee = Trainee.objects.get(id=pk1)
    required_test = Test.objects.get(id=pk2)
    required_trainees = Trainee.objects.filter(course_class=required_course_class)

    if request.user.is_superuser and required_test.course_class == required_course_class:
        test = required_test
        context = {
            'test': test
        }
        if test.dss == required_dss:
            if test.trainee in required_trainees:
                return render(request, "admin/detail/test.html", context)
            else:
                return redirect('course-class-detail', pk=pk)
        else:
            return redirect('course-class-detail', pk=pk)
    else:
        return redirect('home')


# Employment views.
@login_required
def create_employment(request, pk, pk1):

    required_course_class = CourseClass.objects.get(id=pk)
    required_dss = required_course_class.dss
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
                return redirect('course-class-detail', pk=pk)
        else:
            form = CreateEmploymentForm()
        context = {
            'form': form
        }
        if required_trainee in required_trainees:
            return render(request, 'admin/create/employment.html', context)
        else:
            return redirect('course-class-detail', pk=pk)
    else:
        return redirect('home')


@login_required
def update_employment(request, pk, pk1, pk2):

    required_course_class = CourseClass.objects.get(id=pk)
    required_dss = required_course_class.dss
    required_trainee = Trainee.objects.get(id=pk1)
    required_employment = Employment.objects.get(id=pk2)
    required_trainees = Trainee.objects.filter(course_class=required_course_class)

    if request.user.is_superuser and required_employment.course_class == required_course_class and required_employment.dss == required_dss:
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
                return redirect('course-class-detail', pk=pk)
        else:
            form = UpdateEmploymentForm(instance=required_employment)
        context = {
            'form': form
        }
        if required_employment.trainee in required_trainees:
            return render(request, 'admin/update/employment.html', context)
        else:
            return redirect('course-class-detail', pk=pk)
    else:
        return redirect('home')


@login_required
def delete_employment(request, pk, pk1, pk2):

    required_course_class = CourseClass.objects.get(id=pk)
    required_dss = required_course_class.dss
    required_trainee = Trainee.objects.get(id=pk1)
    required_employment = Employment.objects.get(id=pk2)

    if request.user.is_superuser and required_employment.course_class == required_course_class and required_employment.dss == required_dss:
        context = {
            'pk': pk
        }
        if request.method == "POST":
            required_employment.delete()
            return redirect('course-class-detail', pk=pk)
        return render(request, "admin/delete/employment.html", context)
    else:
        return redirect('home')


@login_required
def employment_detail(request, pk, pk1, pk2):

    required_course_class = CourseClass.objects.get(id=pk)
    required_dss = required_course_class.dss
    required_trainee = Trainee.objects.get(id=pk1)
    required_employment = Employment.objects.get(id=pk2)
    required_trainees = Trainee.objects.filter(course_class=required_course_class)

    if request.user.is_superuser and required_employment.course_class == required_course_class:
        employment = required_employment
        context = {
            'employment': employment
        }
        if employment.dss == required_dss:
            if employment.trainee in required_trainees:
                return render(request, "admin/detail/employment.html", context)
            else:
                return redirect('course-class-detail', pk=pk)
        else:
            return redirect('course-class-detail', pk=pk)
    else:
        return redirect('home')


# notifications
@login_required
def course_class_log(request):
    if request.user.is_superuser:
        all_notifications = Notification.objects.all()
        context = {
            'notifications': all_notifications
        }
        return render(request, 'admin/log/course_class.html', context)
    else:
        return redirect('home')


# Employment Log
@login_required
def employment_log(request, pk, pk1):
    required_course_class = CourseClass.objects.get(id=pk)
    required_dss = required_course_class.dss
    required_trainee = Trainee.objects.get(id=pk1)

    if request.user.is_superuser and required_trainee.course_class == required_course_class:
        employments = Employment.objects.filter(Q(course_class=required_course_class) & Q(trainee=required_trainee))
        context = {
            'required_course_class': required_course_class,
            'required_trainee': required_trainee,
            'employments': employments
        }
        if required_trainee.dss == required_dss:
            return render(request, "admin/log/employment.html", context)
        else:
            return redirect('admin:read-course-class')
    else:
        return redirect('home')


# Activate Account View
class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except Exception as identifier:
            user = None
        if user is not None and generate_token.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user)
            messages.add_message(request, messages.INFO, 'Account activated successfully.')
            return redirect('dss:initial-password')
        return render(request, 'registration/activate_failed.html', status=401)


# Ajax implementation
def load_districts(request):
    province_id = request.GET.get('province')
    districts = District.objects.filter(province_id=province_id).order_by('name')
    return render(request, 'dropdown/district_dropdown_list_options.html', {'districts': districts})


def load_municipalities(request):
    district_id = request.GET.get('district')
    municipalities = Municipality.objects.filter(district_id=district_id).order_by('name')
    return render(request, 'dropdown/municipality_dropdown_list_options.html', {'municipalities': municipalities})


def load_office_districts(request):
    province_id = request.GET.get('office_province')
    districts = District.objects.filter(province_id=province_id).order_by('name')
    return render(request, 'dropdown/district_dropdown_list_options.html', {'districts': districts})


def load_office_municipalities(request):
    district_id = request.GET.get('office_district')
    municipalities = Municipality.objects.filter(district_id=district_id).order_by('name')
    return render(request, 'dropdown/municipality_dropdown_list_options.html', {'municipalities': municipalities})


def load_permanent_districts(request):
    province_id = request.GET.get('permanent_province')
    districts = District.objects.filter(province_id=province_id).order_by('name')
    return render(request, 'dropdown/district_dropdown_list_options.html', {'districts': districts})


def load_permanent_municipalities(request):
    district_id = request.GET.get('permanent_district')
    municipalities = Municipality.objects.filter(district_id=district_id).order_by('name')
    return render(request, 'dropdown/municipality_dropdown_list_options.html', {'municipalities': municipalities})


def load_temporary_districts(request):
    province_id = request.GET.get('temporary_province')
    districts = District.objects.filter(province_id=province_id).order_by('name')
    return render(request, 'dropdown/district_dropdown_list_options.html', {'districts': districts})


def load_temporary_municipalities(request):
    district_id = request.GET.get('temporary_district')
    municipalities = Municipality.objects.filter(district_id=district_id).order_by('name')
    return render(request, 'dropdown/municipality_dropdown_list_options.html', {'municipalities': municipalities})
