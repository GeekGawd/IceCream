from __future__ import unicode_literals

import os
import uuid

from django.core.exceptions import ValidationError
from django.db import models


## DO NOT DELETE THIS FUNCTION
## If you think that this function is outright useless because it is never called,
## stop right there. You delete this and all the migrations will FAIL!
def upload_location(instance, filename):
    return '%s/%s' % (instance.id, filename)



def members_upload_location(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/members', filename)


def projects_upload_location(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/projects', filename)


class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    contact = models.BigIntegerField()
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'contact us'


class Designation(models.Model):
    name = models.CharField(max_length=225, unique=True, null=False,
                            blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Designations"


class Technology(models.Model):
    name = models.CharField(max_length=225, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Technologies"


class Member(models.Model):
    name = models.CharField(max_length=225, null=False, blank=False)
    designation = models.ForeignKey(to=Designation, null=True)
    technology = models.ManyToManyField(to=Technology)
    presently_at = models.CharField(max_length=225, null=False, blank=True)
    is_alumni = models.BooleanField(default=False)
    batch = models.IntegerField(null=False)
    pic_path = models.FileField(upload_to=members_upload_location, null=True,
                                default=None)
    facebook = models.CharField(max_length=225, null=True, default=None)
    github = models.CharField(max_length=225, null=True, default=None)
    linkedin = models.CharField(max_length=225, null=True, default=None)

    def __str__(self):
        return self.name + " | " + str(
            self.batch) + " | " + self.designation.name

    class Meta:
        verbose_name_plural = "Members"
        ordering = ['batch']


class Project(models.Model):
    name = models.CharField(max_length=225, null=False, blank=False)
    description = models.CharField(max_length=225, null=False, blank=False)
    completion_year = models.IntegerField(null=True, default=None)
    image_path = models.FileField(upload_to=projects_upload_location, null=True,
                                  default=None)

    def __str__(self):
        return self.name + str(self.completion_year)

    class Meta:
        verbose_name_plural = "Projects"


class Branch(models.Model):
    name = models.CharField(max_length=3, null=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Branches'


class Year(models.Model):
    value = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.value)


class Registration(models.Model):
    name = models.CharField(max_length=225, null=False)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=10, unique=True, null=False)
    student_number = models.CharField(max_length=8)
    branch = models.ForeignKey('Branch')
    year = models.ForeignKey('Year')
    gender = models.ForeignKey('Gender')
    hosteler = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    event = models.ForeignKey('Event')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.event = Event.objects.filter(active=True).first()

        super(Registration, self).save()

    def __str__(self):
        return "{} || {} || {}".format(self.name, self.branch, str(self.year))


def event_validator(value):
    if value is True and Event.objects.filter(active=True).count() >= 1:
        raise ValidationError(
            'More than one events cannot be active at a given time'
        )


class Event(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False, validators=[event_validator, ])

    def __str__(self):
        return "{} | {}".format(self.name, self.timestamp.date())


class Gender(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
