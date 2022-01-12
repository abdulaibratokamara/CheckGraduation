# Generated by Django 3.2.11 on 2022-01-12 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studid', models.CharField(max_length=200, null=True, unique=True)),
                ('fullname', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('Graduated', 'To be graduated'), ('Check Finance', 'Check Finance'), ('Check Finance and Registry', 'Check Finance and Registry'), ('Check Registry', 'Check Registry'), ('Check Exams Office', 'Check Exams Office')], max_length=200)),
                ('department', models.CharField(choices=[('Accounting Finance', 'Accounting Finance'), ('Human Resource Management', 'Human Resource Management'), ('Banking and Finance', 'Banking and Finance'), ('Public Administration  Management', 'Public Administration  Management'), ('Procurement Logistics  Supply Chain Management', 'Procurement Logistics  Supply Chain Management'), ('Education Language and Linguistics', 'Education Language and Linguistics'), ('Special Education', 'Special Education'), ('Educational Administration', 'Educational Administration'), ('Guidance and Counselling', 'Guidance and Counselling'), ('Measurement and Evaluation', 'Measurement and Evaluation'), ('Education Math and Statistics', 'Education Math and Statistics'), ('Computer Science', 'Computer Science'), ('Mass Communication', 'Mass Communication'), ('Philosophy and Humanities', 'Philosophy and Humanities'), ('Political Science and International Relations', 'Political Science and International Relations'), ('Law', 'Law'), ('Development Studies', 'Development Studies'), ('Counselling Psychology', 'Counselling Psychology'), ('Economics', 'Economics'), ('Public Health', 'Public Health'), ('Peace Studies', 'Peace Studies'), ('Development Communication', 'Development Communication'), ('Business Administration', 'Business Administration'), ('Good Governance and Human Rights', 'Good Governance and Human Rights'), ('Agriculture', 'Agriculture'), ('Religious Studies', 'Religious Studies'), ('HTC Integration Sciences', 'HTC Integration Sciences'), ('HTC  Mathematics', 'HTC  Mathematics'), ('HTC Language Arts', 'HTC Language Arts'), ('Mental Health Capacity Building', 'Mental Health Capacity Building')], max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField()),
            ],
        ),
    ]
