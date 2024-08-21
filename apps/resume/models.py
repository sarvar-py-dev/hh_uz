from django.contrib.auth import get_user_model
from django.db.models import (
    Model, CharField, DateField,
    ForeignKey, TextField,
    BooleanField, PositiveIntegerField,
    CASCADE, SET_NULL,
    TextChoices, OneToOneField
)


# User = get_user_model()


class Resume(Model):
    profession = CharField(max_length=255)
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    middle_name = CharField(max_length=255, null=True, blank=True)
    city_or_country = CharField(max_length=255)
    birthdate = DateField(null=True, blank=True)
    phone_number = CharField(max_length=15)
    citizenship = CharField(max_length=100)
    work_permit = CharField(max_length=100)


class Education(Model):
    name = CharField(max_length=255)
    faculty = CharField(max_length=255)
    speciality = CharField(max_length=255)
    graduated_year = CharField(max_length=4)
    resume = ForeignKey('resume.Resume', CASCADE, related_name='educations')

    def __str__(self):
        return self.name


class Experience(Model):
    company_name = CharField(max_length=255)
    position = CharField(max_length=255)
    description = TextField()
    start_year = DateField()
    end_year = DateField()
    till_now = BooleanField(default=True)
    resume = ForeignKey('resume.Resume', CASCADE, related_name='experiences')

    def __str__(self):
        return self.company_name


class Level(Model):
    name = CharField(max_length=255)
    description = CharField(max_length=500)

    def __str__(self):
        return self.name


class Ability(Model):
    name = CharField(max_length=255)
    resume = ForeignKey('resume.Resume', CASCADE, related_name='abilities')
    level = ForeignKey('resume.Level', SET_NULL, null=True)

    def __str__(self):
        return self.name


class DesiredPositionAndSalary(Model):
    class CurrencyChoices(TextChoices):
        UZS = 'uzs', 'Uzs'
        EURO = 'eur', 'Euro'
        USD = 'usd', 'Usd'

    desired_position = CharField(max_length=255)
    salary = PositiveIntegerField()
    currency = CharField(max_length=3, choices=CurrencyChoices.choices, default=CurrencyChoices.USD)
    resume = ForeignKey('resume.Resume', CASCADE, related_name='desired_position')


class Specialization(Model):
    name = CharField(max_length=255)
    desired_position = ForeignKey('resume.DesiredPositionAndSalary', CASCADE, related_name='specialization')


class Employment(Model):
    full_time = BooleanField(default=True)
    part_time = BooleanField(default=False)
    project_work = BooleanField(default=False)
    volunteering = BooleanField(default=False)

    desired_position = OneToOneField('resume.DesiredPositionAndSalary', CASCADE, related_name='employment')


class WorkSchedule(Model):
    full_day = BooleanField(default=False)
    shift_schedule = BooleanField(default=False)
    flexible_schedule = BooleanField(default=False)
    remote_working = BooleanField(default=False)
    rotation_based = BooleanField(default=False)

    desired_position = OneToOneField(DesiredPositionAndSalary, CASCADE)
