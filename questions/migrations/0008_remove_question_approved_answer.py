# Generated by Django 2.1.7 on 2019-08-08 02:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0007_auto_20190808_0833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='approved_answer',
        ),
    ]