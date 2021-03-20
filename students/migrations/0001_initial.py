# Generated by Django 3.0.8 on 2021-03-20 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Student Name')),
                ('fname', models.CharField(max_length=500, verbose_name='Father Name')),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('pin', models.CharField(max_length=500)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('classes', models.CharField(choices=[('5th', 'Class 5th'), ('6th', 'Class 6th'), ('7th', 'Class 7th'), ('8th', 'Class 8th'), ('9th', 'Class 9th'), ('10th', 'Class 10th')], max_length=50)),
                ('marks', models.IntegerField(verbose_name='Percentage')),
                ('enrolled', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
