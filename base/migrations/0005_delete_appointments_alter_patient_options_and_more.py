# Generated by Django 4.1.4 on 2022-12-30 13:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_appointments_doctorid_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Appointments',
        ),
        migrations.AlterModelOptions(
            name='patient',
            options={'ordering': ['-sent_date']},
        ),
        migrations.AddField(
            model_name='patient',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='accepted_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='sent_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='symptoms',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]