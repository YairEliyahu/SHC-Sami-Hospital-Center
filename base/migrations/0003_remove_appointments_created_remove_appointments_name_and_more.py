# Generated by Django 4.1.4 on 2022-12-15 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_appointments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointments',
            name='created',
        ),
        migrations.RemoveField(
            model_name='appointments',
            name='name',
        ),
        migrations.RemoveField(
            model_name='appointments',
            name='updated',
        ),
        migrations.AddField(
            model_name='appointments',
            name='appointmentDate',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='appointments',
            name='doctorId',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='appointments',
            name='doctorName',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='appointments',
            name='patientId',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='appointments',
            name='patientName',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='appointments',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]