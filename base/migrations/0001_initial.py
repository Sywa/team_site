# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('contact', models.TextField(null=True)),
                ('value_contact', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('id_project', models.IntegerField(null=True)),
                ('id_person', models.IntegerField(null=True)),
                ('title_project', models.TextField(null=True)),
                ('features_project', models.TextField(null=True)),
                ('link_project', models.TextField(null=True)),
                ('type_project', models.TextField(null=True)),
                ('GitLink', models.TextField(null=True)),
                ('description_project', models.TextField(null=True)),
                ('category', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('id_person', models.IntegerField(null=True)),
                ('name_person', models.TextField(null=True)),
                ('contacts_person', models.TextField(null=True)),
                ('social_person', models.TextField(null=True)),
                ('skils_person', models.TextField(null=True)),
                ('about_person', models.TextField(null=True)),
            ],
        ),
    ]
