# Generated by Django 3.2.4 on 2022-04-25 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0012_registration_is_hosteler'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Verification',
        ),
        migrations.AlterField(
            model_name='registration',
            name='student_number',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]