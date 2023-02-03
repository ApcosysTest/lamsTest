# Generated by Django 4.1.5 on 2023-02-01 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addemployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Contact', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('D_O_B', models.DateField(blank=True, null=True)),
                ('Date_of_join', models.DateField(blank=True, null=True)),
                ('department', models.CharField(max_length=200)),
                ('Designation', models.CharField(max_length=200)),
                ('Reporting_Dept', models.CharField(max_length=200)),
                ('Email', models.EmailField(blank=True, max_length=70, unique=True)),
                ('User_name', models.CharField(max_length=200)),
                ('Password', models.CharField(max_length=200)),
                ('Confirm_Password', models.CharField(max_length=200)),
                ('Emp_ID', models.CharField(max_length=200)),
                ('Image', models.ImageField(upload_to='images/')),
                ('Emp_status', models.IntegerField(blank=True, default=0, null=True)),
                ('Total_Paid_Leave', models.CharField(blank=True, default='15', max_length=10, null=True)),
                ('Total_Sick_Leave', models.CharField(blank=True, default='15', max_length=10, null=True)),
                ('Total_HalfDay_Leave', models.CharField(blank=True, default='15', max_length=10, null=True)),
                ('Total_Unpaid_Leave', models.CharField(blank=True, default='15', max_length=10, null=True)),
                ('Pending_Paid_Leave', models.CharField(blank=True, default='15', max_length=10, null=True)),
                ('Pending_Sick_Leave', models.CharField(blank=True, default='15', max_length=10, null=True)),
                ('Pending_HalfDay_Leave', models.CharField(blank=True, default='15', max_length=10, null=True)),
                ('Pending_Unpaid_Leave', models.CharField(blank=True, default='15', max_length=10, null=True)),
            ],
            options={
                'db_table': 'add_employee',
            },
        ),
        migrations.CreateModel(
            name='Admin_Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'admin_Login',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Leave_App',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(auto_now=True)),
                ('Category', models.CharField(max_length=200)),
                ('From', models.CharField(max_length=200)),
                ('to', models.CharField(max_length=200)),
                ('leavedayCategory_From', models.CharField(max_length=200)),
                ('leavedayCategory_to', models.CharField(max_length=200)),
                ('Reason', models.CharField(max_length=250)),
                ('Emp_ID', models.CharField(blank=True, max_length=200, null=True)),
                ('Leave_count_Category', models.CharField(blank=True, max_length=2, null=True)),
                ('leave_status', models.IntegerField(blank=True, default=0, null=True)),
                ('comments', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'leave',
            },
        ),
    ]
