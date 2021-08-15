from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from .views import landing

from .views import create_dss_admin, create_course_class
from .views import create_smt_member, create_trainer, create_trainee, create_staff
from .views import create_qualification, create_experience, create_test, create_employment, create_training
from .views import create_activity, create_document, create_property, create_requirement

from .views import read_dss_admin, read_course_class
from .views import read_smt_member, read_trainer, read_trainee, read_staff, read_training
from .views import read_activity, read_document, read_property, read_requirement

from .views import update_course_class
from .views import update_smt_member, update_trainer, update_trainee, update_staff
from .views import update_qualification, update_experience, update_test, update_employment, update_training
from .views import update_activity, update_document, update_property, update_requirement

from .views import delete_course_class
from .views import delete_smt_member, delete_trainer, delete_trainee, delete_staff
from .views import delete_qualification, delete_experience, delete_test, delete_employment, delete_training
from .views import delete_activity, delete_document, delete_property, delete_requirement

from .views import profile, edit_profile, initial_password

from .views import dss_admin_detail, course_class_detail
from .views import smt_member_detail, trainer_detail, trainee_detail, staff_detail
from .views import test_detail, employment_detail, training_detail
from .views import activity_detail, document_detail, property_detail, requirement_detail

from .views import course_class_log

from .views import employment_log

from ctevt.settings import MEDIA_URL, MEDIA_ROOT

app_name = 'dss'

urlpatterns = [

    # for dss
    path('home/', landing, name='landing'),

    # dss admin
    path('create/dss/admin', create_dss_admin, name='create-dss-admin'),
    path('read/dss/admin', read_dss_admin, name='read-dss-admin'),
    path('detail/dss/admin/<int:pk>', dss_admin_detail, name='dss-admin-detail'),

    # course class
    path('create/course_class', create_course_class, name='create-course-class'),
    path('read/course_class', read_course_class, name='read-course-class'),
    path('update/course_class/<int:pk>', update_course_class, name='update-course-class'),
    path('delete/course_class/<int:pk>', delete_course_class, name='delete-course-class'),
    path('detail/course_class/<int:pk>', course_class_detail, name='course-class-detail'),

    # smtm
    path('create/smtm', create_smt_member, name='create-smtm'),
    path('read/smtm', read_smt_member, name='read-smtm'),
    path('update/smtm/<int:pk>', update_smt_member, name='update-smtm'),
    path('delete/smtm/<int:pk>', delete_smt_member, name='delete-smtm'),
    path('detail/smtm/<int:pk>', smt_member_detail, name='smtm-detail'),

    # trainer
    path('create/trainer', create_trainer, name='create-trainer'),
    path('read/trainer', read_trainer, name='read-trainer'),
    path('update/trainer/<int:pk>', update_trainer, name='update-trainer'),
    path('delete/trainer/<int:pk>', delete_trainer, name='delete-trainer'),
    path('detail/trainer/<int:pk>', trainer_detail, name='trainer-detail'),

    # trainer's qualification
    path('create/qualification/<int:pk>', create_qualification, name='create-qualification'),
    path('update/qualification/<int:pk>/<int:pk1>', update_qualification, name='update-qualification'),
    path('delete/qualification/<int:pk>/<int:pk1>', delete_qualification, name='delete-qualification'),

    # trainer's experience
    path('create/experience/<int:pk>', create_experience, name='create-experience'),
    path('update/experience/<int:pk>/<int:pk1>', update_experience, name='update-experience'),
    path('delete/experience/<int:pk>/<int:pk1>', delete_experience, name='delete-experience'),

    # trainee
    path('create/trainee', create_trainee, name='create-trainee'),
    path('read/trainee', read_trainee, name='read-trainee'),
    path('update/trainee/<int:pk>', update_trainee, name='update-trainee'),
    path('delete/trainee/<int:pk>', delete_trainee, name='delete-trainee'),
    path('detail/trainee/<int:pk>', trainee_detail, name='trainee-detail'),

    # staff
    path('create/staff', create_staff, name='create-staff'),
    path('read/staff', read_staff, name='read-staff'),
    path('update/staff/<int:pk>', update_staff, name='update-staff'),
    path('delete/staff/<int:pk>', delete_staff, name='delete-staff'),
    path('detail/staff/<int:pk>', staff_detail, name='staff-detail'),

    # test
    path('create/test/<int:pk>/<int:pk1>', create_test, name='create-test'),
    path('update/test/<int:pk>/<int:pk1>/<int:pk2>', update_test, name='update-test'),
    path('delete/test/<int:pk>/<int:pk1>/<int:pk2>', delete_test, name='delete-test'),
    path('detail/test/<int:pk>/<int:pk1>/<int:pk2>', test_detail, name='test-detail'),

    # employment
    path('create/employment/<int:pk>/<int:pk1>', create_employment, name='create-employment'),
    path('update/employment/<int:pk>/<int:pk1>/<int:pk2>', update_employment, name='update-employment'),
    path('delete/employment/<int:pk>/<int:pk1>/<int:pk2>', delete_employment, name='delete-employment'),
    path('detail/employment/<int:pk>/<int:pk1>/<int:pk2>', employment_detail, name='employment-detail'),

    # course class logs
    # path('log/course_class/', course_class_log, name='course-class-log'),

    # employment log
    path('log/detail/<int:pk>/<int:pk1>', employment_log, name='employment-log-detail'),

    # training
    path('create/training', create_training, name='create-training'),
    path('read/training', read_training, name='read-training'),
    path('update/training/<int:pk>', update_training, name='update-training'),
    path('delete/training/<int:pk>', delete_training, name='delete-training'),
    path('detail/training/<int:pk>', training_detail, name='training-detail'),

    # activity
    path('create/activity', create_activity, name='create-activity'),
    path('read/activity', read_activity, name='read-activity'),
    path('update/activity/<int:pk>', update_activity, name='update-activity'),
    path('delete/activity/<int:pk>', delete_activity, name='delete-activity'),
    path('detail/activity/<int:pk>', activity_detail, name='activity-detail'),

    # document
    path('create/document', create_document, name='create-document'),
    path('read/document', read_document, name='read-document'),
    path('update/document/<int:pk>', update_document, name='update-document'),
    path('delete/document/<int:pk>', delete_document, name='delete-document'),
    path('detail/document/<int:pk>', document_detail, name='document-detail'),

    # property
    path('create/property', create_property, name='create-property'),
    path('read/property', read_property, name='read-property'),
    path('update/property/<int:pk>', update_property, name='update-property'),
    path('delete/property/<int:pk>', delete_property, name='delete-property'),
    path('detail/property/<int:pk>', property_detail, name='property-detail'),

    # requirement
    path('create/requirement', create_requirement, name='create-requirement'),
    path('read/requirement', read_requirement, name='read-requirement'),
    path('update/requirement/<int:pk>', update_requirement, name='update-requirement'),
    path('delete/requirement/<int:pk>', delete_requirement, name='delete-requirement'),
    path('detail/requirement/<int:pk>', requirement_detail, name='requirement-detail'),

    # profile
    path('profile', profile, name='profile'),
    path('profile/edit', edit_profile, name='edit-profile'),
    path('initial_password', initial_password, name='initial-password'),

] + static(MEDIA_URL, document_root=MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
