from django.db import models

# Create your models here.

class Team(models.Model):
    id = models.IntegerField(primary_key=True)
    id_person = models.IntegerField(null=True)
    name_person = models.TextField(null=True)
    contacts_person = models.TextField(null=True)
    social_person = models.TextField(null=True)
    skils_person = models.TextField(null=True)
    about_person = models.TextField(null=True)

    #class Meta:
        #order_with_respect_to = 'id'

class Projects(models.Model):
    id = models.IntegerField(primary_key=True)
    id_project = models.IntegerField(null=True)
    id_person = models.IntegerField(null=True)
    title_project = models.TextField(null=True)
    features_project = models.TextField(null=True)
    link_project = models.TextField(null=True)
    type_project = models.TextField(null=True)
    GitLink = models.TextField(null=True)
    description_project = models.TextField(null=True)
    category = models.TextField(null=True)

class Contact(models.Model):
    id = models.IntegerField(primary_key=True)
    contact = models.TextField(null=True)
    value_contact = models.TextField(null=True)