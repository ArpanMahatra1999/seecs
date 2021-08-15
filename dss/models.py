from ckeditor.fields import RichTextField

from django.core.validators import RegexValidator
from django.db import models
from nepali_datetime_field.models import NepaliDateField

from location.models import Province, District, Municipality


# Create your models here.
class DSS(models.Model):

    # Regex validators
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
    )
    SPECIAL_FOCUS_GROUP = (
        ('Halaiya', 'Halaiya'),
        ('Kamaiya', 'Kamaiya'),
        ('HIV Infected', 'HIV Infected'),
        ('Single Women', 'Single Women')
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

    # general information
    title = models.CharField(max_length=255)

    CALENDAR = (
        ('BS', 'BS'),
        ('AD', 'AD')
    )

    calendar = models.CharField(max_length=255, choices=CALENDAR)

    date_of_establishment_BS = NepaliDateField(null=True, blank=True, help_text="Write in YYYY-MM-DD format")
    date_of_establishment_AD = models.DateField(null=True, blank=True)

    description = RichTextField(null=True, blank=True)

    # identity
    photo = models.ImageField(null=True, blank=True, upload_to='images/dss/', default='images/dss/default_dss.png')
    phone_number = models.CharField(max_length=255, validators=[phone_regex], help_text="Phone number must be entered in the format: '000-555555' or '9999999999'.")

    # address
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE)
    ward_number = models.PositiveIntegerField(choices=WARD_NUMBER)
    street_name = models.CharField(max_length=255, null=True, blank=True)
    tole_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.title)
