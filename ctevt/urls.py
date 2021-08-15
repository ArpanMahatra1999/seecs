from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from .views import home, landing
from .views import create_dss, read_dss, dss_detail
from .views import create_dss_admin, read_dss_admin, dss_admin_detail
from .views import create_smt_member, read_smt_member, update_smt_member, delete_smt_member, smt_member_detail
from .views import create_trainer, read_trainer, update_trainer, delete_trainer, trainer_detail
from .views import create_trainee, read_trainee, update_trainee, delete_trainee, trainee_detail
from .views import create_staff, read_staff, update_staff, delete_staff, staff_detail
from .views import create_stakeholder, read_stakeholder, update_stakeholder, delete_stakeholder, stakeholder_detail
from .views import create_course, read_course, update_course, delete_course, course_detail
from .views import create_training, read_training, update_training, delete_training, training_detail
from .views import create_activity, read_activity, update_activity, delete_activity, activity_detail
from .views import create_document, read_document, update_document, delete_document, document_detail
from .views import create_property, read_property, update_property, delete_property, property_detail
from .views import create_requirement, read_requirement, update_requirement, delete_requirement, requirement_detail
from .views import create_course_class, read_course_class, update_course_class, delete_course_class, course_class_detail
from .views import create_qualification, read_qualification, update_qualification, delete_qualification, qualification_detail
from .views import create_experience, read_experience, update_experience, delete_experience, experience_detail
from .views import create_test, update_test, delete_test, test_detail
from .views import create_employment, update_employment, delete_employment, employment_detail
from .views import course_class_log
from .views import employment_log
from .views import ActivateAccountView
from .views import load_districts, load_municipalities
from .views import load_office_districts, load_office_municipalities
from .views import load_permanent_districts, load_permanent_municipalities
from .views import load_temporary_districts, load_temporary_municipalities

from .settings import MEDIA_URL, MEDIA_ROOT


urlpatterns = [
    path('django/admin/', admin.site.urls),
    path('', home, name='home'),

    # for admin
    path('admin/home/', landing, name='landing'),

    # dss
    path('admin/create/dss/', create_dss, name='create-dss'),
    path('admin/read/dss/', read_dss, name='read-dss'),
    path('admin/detail/dss/<int:pk>', dss_detail, name='dss-detail'),

    # dss admin
    path('admin/create/dss/admin/<int:pk>', create_dss_admin, name='create-dss-admin'),
    path('admin/read/dss/admin/<int:pk>', read_dss_admin, name='read-dss-admin'),
    path('admin/detail/dss/admin/<int:pk>/<int:pk2>', dss_admin_detail, name='dss-admin-detail'),

    # smt member
    path('admin/create/smtm/', create_smt_member, name='create-smtm'),
    path('admin/read/smtm/', read_smt_member, name='read-smtm'),
    path('admin/update/smtm/<int:pk>', update_smt_member, name='update-smtm'),
    path('admin/delete/smtm/<int:pk>', delete_smt_member, name='delete-smtm'),
    path('admin/detail/smtm/<int:pk>', smt_member_detail, name='smtm-detail'),

    # trainer
    path('admin/create/trainer/', create_trainer, name='create-trainer'),
    path('admin/read/trainer/', read_trainer, name='read-trainer'),
    path('admin/update/trainer/<int:pk>', update_trainer, name='update-trainer'),
    path('admin/delete/trainer/<int:pk>', delete_trainer, name='delete-trainer'),
    path('admin/detail/trainer/<int:pk>', trainer_detail, name='trainer-detail'),

    # trainee
    path('admin/create/trainee/', create_trainee, name='create-trainee'),
    path('admin/read/trainee/', read_trainee, name='read-trainee'),
    path('admin/update/trainee/<int:pk>', update_trainee, name='update-trainee'),
    path('admin/delete/trainee/<int:pk>', delete_trainee, name='delete-trainee'),
    path('admin/detail/trainee/<int:pk>', trainee_detail, name='trainee-detail'),

    # staff
    path('admin/create/staff/', create_staff, name='create-staff'),
    path('admin/read/staff/', read_staff, name='read-staff'),
    path('admin/update/staff/<int:pk>', update_staff, name='update-staff'),
    path('admin/delete/staff/<int:pk>', delete_staff, name='delete-staff'),
    path('admin/detail/staff/<int:pk>', staff_detail, name='staff-detail'),

    # stakeholder
    path('admin/create/stakeholder/', create_stakeholder, name='create-stakeholder'),
    path('admin/read/stakeholder/', read_stakeholder, name='read-stakeholder'),
    path('admin/update/stakeholder/<int:pk>', update_stakeholder, name='update-stakeholder'),
    path('admin/delete/stakeholder/<int:pk>', delete_stakeholder, name='delete-stakeholder'),
    path('admin/detail/stakeholder/<int:pk>', stakeholder_detail, name='stakeholder-detail'),

    # course
    path('admin/create/course/', create_course, name='create-course'),
    path('admin/read/course/', read_course, name='read-course'),
    path('admin/update/course/<int:pk>', update_course, name='update-course'),
    path('admin/delete/course/<int:pk>', delete_course, name='delete-course'),
    path('admin/detail/course/<int:pk>', course_detail, name='course-detail'),

    # training
    path('admin/create/training/', create_training, name='create-training'),
    path('admin/read/training/', read_training, name='read-training'),
    path('admin/update/training/<int:pk>', update_training, name='update-training'),
    path('admin/delete/training/<int:pk>', delete_training, name='delete-training'),
    path('admin/detail/training/<int:pk>', training_detail, name='training-detail'),

    # activity
    path('admin/create/activity/', create_activity, name='create-activity'),
    path('admin/read/activity', read_activity, name='read-activity'),
    path('admin/update/activity/<int:pk>', update_activity, name='update-activity'),
    path('admin/delete/activity/<int:pk>', delete_activity, name='delete-activity'),
    path('admin/detail/activity/<int:pk>', activity_detail, name='activity-detail'),

    # document
    path('admin/create/document/', create_document, name='create-document'),
    path('admin/read/document/', read_document, name='read-document'),
    path('admin/update/document/<int:pk>', update_document, name='update-document'),
    path('admin/delete/document/<int:pk>', delete_document, name='delete-document'),
    path('admin/detail/document/<int:pk>', document_detail, name='document-detail'),

    # property
    path('admin/create/property/', create_property, name='create-property'),
    path('admin/read/property/', read_property, name='read-property'),
    path('admin/update/property/<int:pk>', update_property, name='update-property'),
    path('admin/delete/property/<int:pk>', delete_property, name='delete-property'),
    path('admin/detail/property/<int:pk>', property_detail, name='property-detail'),

    # requirement
    path('admin/create/requirement/', create_requirement, name='create-requirement'),
    path('admin/read/requirement/', read_requirement, name='read-requirement'),
    path('admin/update/requirement/<int:pk>', update_requirement, name='update-requirement'),
    path('admin/delete/requirement/<int:pk>', delete_requirement, name='delete-requirement'),
    path('admin/detail/requirement/<int:pk>', requirement_detail, name='requirement-detail'),

    # course class
    path('admin/create/course_class/<int:pk>', create_course_class, name='create-course-class'),
    path('admin/read/course_class/<int:pk>', read_course_class, name='read-course-class'),
    path('admin/update/course_class/<int:pk>/<int:pk1>', update_course_class, name='update-course-class'),
    path('admin/delete/course_class/<int:pk>/<int:pk1>', delete_course_class, name='delete-course-class'),
    path('admin/detail/course_class/<int:pk>/<int:pk1>', course_class_detail, name='course-class-detail'),

    # test
    path('admin/create/test/<int:pk>/<int:pk1>', create_test, name='create-test'),
    path('admin/update/test/<int:pk>/<int:pk1>/<int:pk2>', update_test, name='update-test'),
    path('admin/delete/test/<int:pk>/<int:pk1>/<int:pk2>', delete_test, name='delete-test'),
    path('admin/detail/test/<int:pk>/<int:pk1>/<int:pk2>', test_detail, name='test-detail'),

    # employment
    path('admin/create/employment/<int:pk>/<int:pk1>', create_employment, name='create-employment'),
    path('admin/update/employment/<int:pk>/<int:pk1>/<int:pk2>', update_employment, name='update-employment'),
    path('admin/delete/employment/<int:pk>/<int:pk1>/<int:pk2>', delete_employment, name='delete-employment'),
    path('admin/detail/employment/<int:pk>/<int:pk1>/<int:pk2>', employment_detail, name='employment-detail'),

    # qualification
    path('admin/create/qualification/<int:pk>', create_qualification, name='create-qualification'),
    path('admin/read/qualification/<int:pk>', read_qualification, name='read-qualification'),
    path('admin/update/qualification/<int:pk>/<int:pk1>', update_qualification, name='update-qualification'),
    path('admin/delete/qualification/<int:pk>/<int:pk1>', delete_qualification, name='delete-qualification'),
    path('admin/detail/qualification/<int:pk>/<int:pk1>', qualification_detail, name='qualification-detail'),

    # experience
    path('admin/create/experience/<int:pk>', create_experience, name='create-experience'),
    path('admin/read/experience/<int:pk>', read_experience, name='read-experience'),
    path('admin/update/experience/<int:pk>/<int:pk1>', update_experience, name='update-experience'),
    path('admin/delete/experience/<int:pk>/<int:pk1>', delete_experience, name='delete-experience'),
    path('admin/detail/experience/<int:pk>/<int:pk1>', experience_detail, name='experience-detail'),

    # course class logs
    # path('log/course_class/', course_class_log, name='course-class-log'),

    # employment logs
    path('log/employment/detail/<int:pk>/<int:pk1>', employment_log, name='employment-log-detail'),

    # dss admin
    path('dss/', include('dss_admin.urls')),

    # authentication
    path('accounts/', include('django.contrib.auth.urls')),

    # activating account
    path('activate/<uidb64>/<token>', ActivateAccountView.as_view(), name='activate'),

    # ajax integration
    path('ajax/load-districts/', load_districts, name='ajax_load_districts'),
    path('ajax/load-municipalities/', load_municipalities, name='ajax_load_municipalities'),
    path('ajax/load-office-districts/', load_office_districts, name='ajax_load_office_districts'),
    path('ajax/load-office-municipalities/', load_office_municipalities, name='ajax_load_office_municipalities'),
    path('ajax/load-permanent-districts/', load_permanent_districts, name='ajax_load_permanent_districts'),
    path('ajax/load-permanent-municipalities/', load_permanent_municipalities, name='ajax_load_permanent_municipalities'),
    path('ajax/load-temporary-districts/', load_temporary_districts, name='ajax_load_temporary_districts'),
    path('ajax/load-temporary-municipalities/', load_temporary_municipalities, name='ajax_load_temporary_municipalities')

] + static(MEDIA_URL, document_root=MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
