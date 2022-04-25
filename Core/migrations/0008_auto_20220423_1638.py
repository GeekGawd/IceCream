# Generated by Django 3.2.4 on 2022-04-23 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0007_registration_whatsapp'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='code',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='message',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='registration',
            name='domain',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='registrations', to='Core.domain'),
        ),
        migrations.AlterField(
            model_name='registration',
            name='roll_no',
            field=models.CharField(max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='registration',
            name='year',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Core.year'),
        ),
    ]