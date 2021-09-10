from django.core.validators import RegexValidator
from django.db import models


class Company(models.Model):
    name = models.CharField('Название', max_length = 75)
    description = models.TextField('Описание', default='Нет описания')
    creation_date = models.DateField('Дата создания', auto_now=False, auto_now_add=False, default='Нет даты создания')
    budget = models.FloatField('Бюджет', default='Нет общего бюджета компании')
    is_active = models.BooleanField('Открыта ли компания', default=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"


class Personal(models.Model):
    positions_choices = [
        ('IT', 'IT Department'),
        ('FD', 'Financial Department'),
        ('AN', 'Analyst'),
        ('AD', 'Advertising Department'),
        ('DC', 'Deputy Chief'),
        ('CH', 'Chief'),
    ]
    name = models.CharField('ФИО сотрудника', max_length=75)
    position = models.TextField('Должность', choices=positions_choices)
    is_active_now = models.BooleanField('Работает ли в данный мосент', default=True)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    photo = models.ImageField(upload_to='personal-photo')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{12,12}$', message="Phone number must be entered in the format: '+375000000000'. Up to 12 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=13)
    def __str__(self):
        return f'{self.name} | {self.position}'


class Company_Pictures(models.Model):
    photo_name = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    photo = models.ImageField(upload_to='company-photo')