# Generated by Django 4.2 on 2023-06-05 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MarriageBiodata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('marital_status', models.CharField(max_length=20)),
                ('religion', models.CharField(max_length=50)),
                ('caste', models.CharField(max_length=50)),
                ('education', models.CharField(max_length=100)),
                ('occupation', models.CharField(max_length=100)),
                ('height', models.CharField(max_length=10)),
                ('weight', models.CharField(max_length=10)),
                ('complexion', models.CharField(max_length=50)),
                ('languages_known', models.CharField(max_length=100)),
                ('hobbies', models.CharField(max_length=200)),
                ('father_name', models.CharField(max_length=100)),
                ('father_occupation', models.CharField(max_length=100)),
                ('mother_name', models.CharField(max_length=100)),
                ('mother_occupation', models.CharField(max_length=100)),
                ('siblings', models.IntegerField()),
                ('about_family', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('pincode', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
            ],
        ),
    ]