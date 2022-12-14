# Generated by Django 3.2.15 on 2022-08-05 11:55

import api.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. This should be your Phone number, for example: +380632737373', max_length=150, unique=True, validators=[api.validators.PhoneNumberValidator()], verbose_name='username')),
                ('last_activity', models.DateField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
