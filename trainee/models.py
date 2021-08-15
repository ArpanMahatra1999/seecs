from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db import models
from nepali_datetime_field.models import NepaliDateField

from course_class.models import CourseClass
from dss.models import DSS
from location.models import Province, District, Municipality


# Create your models here.
class Trainee(models.Model):

    # Regex Validators
    phone_regex = RegexValidator(regex=r'^(9\d{9}|0\d{1,2}-\d{6})$')

    # Choices
    GENDERS = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Sexual Minority', 'Sexual Minority')
    )
    MARITAL_STATUS = (
        ('Unmarried', 'Unmarried'),
        ('Married', 'Married'),
        ('Multimarried', 'Multimarried'),
        ('Widow', 'Widow'),
        ('Divorced', 'Divorced'),
        ('Separated', 'Separated')
    )
    MIGRATION_STATUS = (
        ('Internal Migrant', 'Internal Migrant'),
        ('Returnee', 'Returnee'),
        ('None', 'None')
    )
    SPECIAL_FOCUS_GROUP = (
        ('Halaiya', 'Halaiya'),
        ('Kamaiya', 'Kamaiya'),
        ('HIV Infected', 'HIV Infected'),
        ('Single Women', 'Single Women'),
        ('None', 'None')
    )
    ETHNICITIES = (
        ('Khas/Chhetri', 'Khas/Chhetri'),
        ('Brahmin-Hill/Bahun', 'Brahmin-Hill/Bahun'),
        ('Magar', 'Magar'),
        ('Tharu', 'Tharu'),
        ('Tamang', 'Tamang'),
        ('Newar', 'Newar'),
        ('Kami', 'Kami'),
        ('Musalman/Nepali Muslims', 'Musalman/Nepali Muslims'),
        ('Yadav Yadav/Ahir', 'Yadav Yadav/Ahir'),
        ('Rai', 'Rai'),
        ('Gurung', 'Gurung'),
        ('Damai/Dholi', 'Damai/Dholi'),
        ('Thakuri	Khas', 'Thakuri	Khas'),
        ('Limbu', 'Limbu'),
        ('Sarki', 'Sarki'),
        ('Teli', 'Teli'),
        ('Chamar/Harijan/Ram', 'Chamar/Harijan/Ram'),
        ('Kushwaha', 'Kushwaha'),
        ('Musahar', 'Musahar'),
        ('Kurmi', 'Kurmi'),
        ('Sanyasi/Dasnami', 'Sanyasi/Dasnami'),
        ('Dhanuk', 'Dhanuk'),
        ('Kanu/Haluwai', 'Kanu/Haluwai'),
        ('Dusadh/Pasawan/Pasi', 'Dusadh/Pasawan/Pasi'),
        ('Mallaha', 'Mallaha'),
        ('Kewat', 'Kewat'),
        ('Kathabaniyan', 'Kathabaniyan'),
        ('Brahmin-Tarai', 'Brahmin-Tarai'),
        ('Kalwar', 'Kalwar'),
        ('Kanu', 'Kanu'),
        ('Kumal', 'Kumal'),
        ('Bhujel', 'Bhujel'),
        ('Hajam/Thakur', 'Hajam/Thakur'),
        ('Rajbanshi', 'Rajbanshi'),
        ('Sherpa', 'Sherpa'),
        ('Dhobi', 'Dhobi'),
        ('Tatma/Tatwa', 'Tatma/Tatwa'),
        ('Lohar', 'Lohar'),
        ('Khatwe', 'Khatwe'),
        ('Sudhi', 'Sudhi'),
        ('Danuwar', 'Danuwar'),
        ('Majhi', 'Majhi'),
        ('Barai', 'Barai'),
        ('Bin', 'Bin'),
        ('Nuniya', 'Nuniya'),
        ('Chepang', 'Chepang'),
        ('Sonar', 'Sonar'),
        ('Kumhar', 'Kumhar'),
        ('Sunwar', 'Sunwar'),
        ('Bantar/Sardar', 'Bantar/Sardar'),
        ('Kahar', 'Kahar'),
        ('Santhal', 'Santhal'),
        ('Marwadi', 'Marwadi'),
        ('Kayastha', 'Kayastha'),
        ('Rajput/Terai', 'Rajput/Terai'),
        ('Badi', 'Badi'),
        ('Jhangar/Uraon', 'Jhangar/Uraon'),
        ('Gangai', 'Gangai'),
        ('Lodh', 'Lodh'),
        ('Badhaee', 'Badhaee'),
        ('Thami', 'Thami'),
        ('Kulung', 'Kulung'),
        ('Bengali', 'Bengali'),
        ('Gaderi/Bhediyar/Gangajali', 'Gaderi/Bhediyar/Gangajali'),
        ('Dhimal', 'Dhimal'),
        ('Yakkha', 'Yakkha'),
        ('Ghale', 'Ghale'),
        ('Tajpuriya', 'Tajpuriya'),
        ('Khawas', 'Khawas'),
        ('Darai', 'Darai'),
        ('Mali', 'Mali'),
        ('Dhuniya', 'Dhuniya'),
        ('Pahari', 'Pahari'),
        ('Rajdhob', 'Rajdhob'),
        ('Bhote', 'Bhote'),
        ('Dom', 'Dom'),
        ('Thakali', 'Thakali'),
        ('Kori', 'Kori'),
        ('Chhantyal', 'Chhantyal'),
        ('Hyolmo', 'Hyolmo'),
        ('Bote', 'Bote'),
        ('Rajbhar', 'Rajbhar'),
        ('Brahmu/Baramo', 'Brahmu/Baramo'),
        ('Punjabi', 'Punjabi'),
        ('Nachhring', 'Nachhring'),
        ('Yamphu', 'Yamphu'),
        ('Gaine', 'Gaine'),
        ('Chamling', 'Chamling'),
        ('Athpahariya', 'Athpahariya'),
        ('Jirel', 'Jirel'),
        ('Dura', 'Dura'),
        ('Sarabaria', 'Sarabaria'),
        ('Meche', 'Meche'),
        ('Bantaba', 'Bantaba'),
        ('Raji', 'Raji'),
        ('Dolpo', 'Dolpo'),
        ('Halkhor', 'Halkhor'),
        ('Byansi/Sauka', 'Byansi/Sauka'),
        ('Amat', 'Amat'),
        ('Thulung', 'Thulung'),
        ('Lepcha', 'Lepcha'),
        ('Pathakatta/Kushwadia', 'Pathakatta/Kushwadia'),
        ('Mewahang', 'Mewahang'),
        ('Bahing', 'Bahing'),
        ('Natuwa', 'Natuwa'),
        ('Hayu', 'Hayu'),
        ('Dhankar/Dharikar', 'Dhankar/Dharikar'),
        ('Lhopa', 'Lhopa'),
        ('Munda', 'Munda'),
        ('Dev', 'Dev'),
        ('Dhandi', 'Dhandi'),
        ('Kamar', 'Kamar'),
        ('Kisan', 'Kisan'),
        ('Sampang', 'Sampang'),
        ('Koche', 'Koche'),
        ('Lhomi', 'Lhomi'),
        ('Khaling', 'Khaling'),
        ('Topkegola', 'Topkegola'),
        ('Chidimar', 'Chidimar'),
        ('Walung', 'Walung'),
        ('Lohorung', 'Lohorung'),
        ('Kalar', 'Kalar'),
        ('Raute', 'Raute'),
        ('Nurang', 'Nurang'),
        ('Kusunda', 'Kusunda'),
        ('Foreigners', 'Foreigners'),
        ('Others/Undefined', 'Others/Undefined')
    )
    RELIGIONS = (
        ('No Religion', 'No Religion'),
        ('Buddhism', 'Buddhism'),
        ('Christianity', 'Christianity'),
        ('Hinduism', 'Hinduism'),
        ('Jainism', 'Jainism'),
        ('Kiratism', 'Kiratism'),
        ('Sikhism', 'Sikhism'),
        ('Others', 'Others'),
    )
    WARD_NUMBER = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),
        (11, 11),
        (12, 12),
        (13, 13),
        (14, 14),
        (15, 15),
        (16, 16),
        (17, 17),
        (18, 18),
        (19, 19),
        (20, 20),
        (21, 21),
        (22, 22),
        (23, 23),
        (24, 24),
        (25, 25),
        (26, 26),
        (27, 27),
        (28, 28),
        (29, 29),
        (30, 30),
        (31, 31),
        (32, 32),
    )
    IDENTITIES = (
        ("Citizenship", "Citizenship"),
        ("Passport", "Passport"),
        ("Driving License", "Driving License")
    )
    DISABILITIES = (
        ("Hearing", "Hearing"),
        ("Seeing", "Seeing"),
        ("Movement", "Movement"),
        ("Others", "Others"),
        ("None", "None")
    )
    AGREEMENT = (
        ('Yes', 'Yes'),
        ('No', 'No')
    )
    COMPLETENESS = (
        ('Completed', 'Completed'),
        ('Incompleted', 'Incompleted')
    )
    CERTIFICATION_TYPES = (
        ('NSTB Registration', 'NSTB Registration'),
        ('Foreign Certificate', 'Foreign Certificated')
    )
    CALENDAR = (
        ('BS', 'BS'),
        ('AD', 'AD')
    )

    # general_information
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255)

    # identity
    photo = models.ImageField(null=True, blank=True, upload_to='images/trainee/', default='images/trainee/default_trainee.png')
    phone_number = models.CharField(max_length=255, validators=[phone_regex], help_text="Phone number must be entered in the format: '000-555555' or '9999999999'.")
    email = models.EmailField()

    # demographics
    gender = models.CharField(max_length=255, choices=GENDERS)
    marital_status = models.CharField(max_length=255, choices=MARITAL_STATUS)
    migration_status = models.CharField(max_length=255, choices=MIGRATION_STATUS)
    special_focus_group = models.CharField(max_length=255, choices=SPECIAL_FOCUS_GROUP)
    religion = models.CharField(max_length=255, choices=RELIGIONS)
    ethnicity = models.CharField(max_length=255, choices=ETHNICITIES)
    disability = models.CharField(max_length=255, choices=DISABILITIES)

    # address
    permanent_province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name="trainee_permanent_province")
    permanent_district = models.ForeignKey(District, on_delete=models.CASCADE, related_name="trainee_permanent_district")
    permanent_municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE,
                                               related_name="trainee_permanent_municipality")
    permanent_ward_number = models.PositiveIntegerField(choices=WARD_NUMBER)
    permanent_street_name = models.CharField(max_length=255, null=True, blank=True)
    permanent_tole_name = models.CharField(max_length=255, null=True, blank=True)
    permanent_house_number = models.PositiveIntegerField(null=True, blank=True)
    permanent_phone_number = models.CharField(max_length=255, validators=[phone_regex],
                                              help_text="Phone number must be entered in the format: '000-555555' or '9999999999'.")

    temporary_province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name="trainee_temporary_province")
    temporary_district = models.ForeignKey(District, on_delete=models.CASCADE, related_name="trainee_temporary_district")
    temporary_municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE,
                                               related_name="trainee_temporary_municipality")
    temporary_ward_number = models.PositiveIntegerField(choices=WARD_NUMBER)
    temporary_street_name = models.CharField(max_length=255, null=True, blank=True)
    temporary_tole_name = models.CharField(max_length=255, null=True, blank=True)
    temporary_house_number = models.PositiveIntegerField(null=True, blank=True)
    temporary_phone_number = models.CharField(max_length=255, validators=[phone_regex],
                                              help_text="Phone number must be entered in the format: '000-555555' or '9999999999'.")

    calendar = models.CharField(max_length=255, choices=CALENDAR)

    date_of_birth_BS = NepaliDateField(null=True, blank=True, help_text="Write in YYYY-MM-DD format")
    date_of_joining_BS = NepaliDateField(null=True, blank=True, help_text="Write in YYYY-MM-DD format")
    date_of_birth_AD = models.DateField(null=True, blank=True)
    date_of_joining_AD = models.DateField(null=True, blank=True)

    # family
    father_first_name = models.CharField(max_length=255)
    father_middle_name = models.CharField(max_length=255, null=True, blank=True)
    father_last_name = models.CharField(max_length=255)
    father_occupation = models.CharField(max_length=255)
    mother_first_name = models.CharField(max_length=255)
    mother_middle_name = models.CharField(max_length=255, null=True, blank=True)
    mother_last_name = models.CharField(max_length=255)
    mother_occupation = models.CharField(max_length=255)
    grandfather_first_name = models.CharField(max_length=255, null=True, blank=True)
    grandfather_middle_name = models.CharField(max_length=255, null=True, blank=True)
    grandfather_last_name = models.CharField(max_length=255, null=True, blank=True)
    spouse_first_name = models.CharField(max_length=255, null=True, blank=True)
    spouse_middle_name = models.CharField(max_length=255, null=True, blank=True)
    spouse_last_name = models.CharField(max_length=255, null=True, blank=True)

    # citizenship records
    citizenship_number = models.CharField(max_length=255)
    citizenship_issued_district = models.ForeignKey(District, on_delete=models.CASCADE,
                                                    related_name="trainee_citizenship_issued_district")
    citizenship_issued_date_BS = NepaliDateField(null=True, blank=True, help_text="Write in YYYY-MM-DD format")
    citizenship_issued_date_AD = models.DateField(null=True, blank=True)

    # pdf records
    proof_of_identity = models.CharField(max_length=255, choices=IDENTITIES)
    front = models.FileField(upload_to="files/identity/front/")
    back = models.FileField(upload_to="files/identity/back/")

    # trainee information
    source_of_information = models.CharField(max_length=255)
    has_taken_similar_training_before = models.CharField(max_length=255, choices=AGREEMENT)
    training_status = models.CharField(max_length=255, choices=COMPLETENESS)
    certification_type = models.CharField(max_length=255, choices=CERTIFICATION_TYPES)
    registration_number = models.CharField(max_length=255)

    # others
    course_class = models.ForeignKey(CourseClass, on_delete=models.SET_NULL, null=True, blank=True)
    dss = models.ForeignKey(DSS, on_delete=models.CASCADE)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)
