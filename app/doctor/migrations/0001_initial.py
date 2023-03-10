# Generated by Django 4.1.4 on 2022-12-23 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('Specialty', models.IntegerField(choices=[(1, 'پوست و مو'), (2, 'داخلی')])),
                ('Data_time_Doctor_come', models.DateTimeField()),
                ('Data_time_Doctor_come1', models.DateTimeField()),
                ('Data_time_Doctor_come2', models.DateTimeField()),
                ('visit_price', models.IntegerField(choices=[(1, '4000000'), (2, '5000000'), (3, '6000000'), (4, 'سه 7000000')])),
                ('doctor_img', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Nurse_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nurse_Nmae', models.CharField(max_length=100)),
                ('nurse_Lastname', models.CharField(max_length=1000)),
                ('natinalCode', models.CharField(max_length=100)),
                ('nurse_img', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Visit_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('natinal_code', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('phone_num', models.CharField(max_length=100)),
                ('mirid', models.BooleanField()),
                ('doctor_time', models.IntegerField(choices=[(1, '08:00'), (2, '09:00'), (3, '10:00'), (4, '11:00'), (5, '12:00'), (6, '13:00'), (7, '14:00'), (8, '15:00'), (9, '16:00'), (10, '17:00'), (11, '18:00'), (12, '19:00'), (13, '20:00'), (14, '21:00')])),
                ('Date_Time', models.DateTimeField()),
                ('doctor_choses', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='doctor.doctor_model')),
            ],
        ),
    ]
