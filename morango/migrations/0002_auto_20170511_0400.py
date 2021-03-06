# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-05-11 04:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager
import morango.utils.uuids


class Migration(migrations.Migration):

    dependencies = [
        ('morango', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificatemodel',
            name='issuer',
        ),
        migrations.AlterModelManagers(
            name='certificate',
            managers=[
                ('_default_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='buffer',
            name='conflicting_serialized_data',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='store',
            name='conflicting_serialized_data',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='buffer',
            name='last_saved_instance',
            field=morango.utils.uuids.UUIDField(),
        ),
        migrations.AlterField(
            model_name='certificate',
            name='id',
            field=morango.utils.uuids.UUIDField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='databaseidmodel',
            name='id',
            field=morango.utils.uuids.UUIDField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='instanceidmodel',
            name='id',
            field=morango.utils.uuids.UUIDField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='store',
            name='last_saved_instance',
            field=morango.utils.uuids.UUIDField(),
        ),
        migrations.AlterField(
            model_name='trustedkey',
            name='id',
            field=morango.utils.uuids.UUIDField(editable=False, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='CertificateModel',
        ),
    ]
