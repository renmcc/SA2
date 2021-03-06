# Generated by Django 2.2.12 on 2020-06-17 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_projectregion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='remark',
            field=models.TextField(blank=True, help_text='备注', null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='projectarea',
            name='remark',
            field=models.TextField(blank=True, help_text='备注', null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='projectrole',
            name='remark',
            field=models.TextField(blank=True, help_text='备注', null=True, verbose_name='备注'),
        ),
    ]
