# Generated by Django 5.2 on 2025-04-20 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoanApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('purpose', models.TextField()),
                ('term_months', models.PositiveIntegerField()),
                ('interest_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('APPROVED', 'Approved'), ('REJECTED', 'Rejected'), ('DISBURSED', 'Disbursed'), ('REPAID', 'Repaid'), ('DEFAULTED', 'Defaulted')], default='PENDING', max_length=20)),
                ('application_date', models.DateTimeField(auto_now_add=True)),
                ('decision_date', models.DateTimeField(blank=True, null=True)),
                ('notes', models.TextField(blank=True)),
                ('external_loan_id', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'ordering': ['-application_date'],
            },
        ),
        migrations.CreateModel(
            name='LoanStatusUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_status', models.CharField(max_length=20)),
                ('new_status', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
