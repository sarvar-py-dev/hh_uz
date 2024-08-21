from django.contrib.admin import ModelAdmin, register, StackedInline
from .models import (
    Level, Ability, Education,
    Experience, Resume, Employment,
    WorkSchedule, DesiredPositionAndSalary, Specialization)


class AbilityStackedInline(StackedInline):
    model = Ability
    fields = 'name', 'resume', 'level'


class EducationStackedInline(StackedInline):
    model = Education
    fields = 'name', 'faculty', 'speciality', 'graduated_year', 'resume'


class ExperienceStackedInline(StackedInline):
    model = Experience
    fields = 'company_name', 'position', 'description', 'start_year', 'end_year', 'till_now', 'resume'


@register(Resume)
class ResumeModelAdmin(ModelAdmin):
    inlines = AbilityStackedInline, ExperienceStackedInline, EducationStackedInline


@register(Level)
class LevelModelAdmin(ModelAdmin):
    pass


class SpecializationStackedInline(StackedInline):
    model = Specialization
    fields = 'name', 'desired_position'


class EmploymentStackedInline(StackedInline):
    model = Employment
    fields = 'full_time', 'part_time', 'project_work', 'volunteering', 'desired_position'


class WorkScheduleStackedInline(StackedInline):
    model = WorkSchedule
    fields = 'full_day', 'shift_schedule', 'flexible_schedule', 'remote_working', 'rotation_based', 'desired_position'


@register(DesiredPositionAndSalary)
class DesiredPositionModelAdmin(ModelAdmin):
    inlines = SpecializationStackedInline, EmploymentStackedInline, WorkScheduleStackedInline
