# Generated by Django 4.1.1 on 2022-11-09 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0007_rename_password1_info_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='password',
            new_name='pass1',
        ),
        migrations.RenameField(
            model_name='info',
            old_name='password2',
            new_name='pass2',
        ),
    ]
