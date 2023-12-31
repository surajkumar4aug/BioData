from django.db import models

class MarriageBiodata(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    marital_status = models.CharField(max_length=20)
    religion = models.CharField(max_length=50)
    caste = models.CharField(max_length=50)
    education = models.CharField(max_length=100)
    education_2 = models.CharField(max_length=100)
    education_3 = models.CharField(max_length=100)
    education_4 = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    languages_known = models.CharField(max_length=100)
    hobbies = models.CharField(max_length=200)
    father_name = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100)
    siblings = models.IntegerField()
    about_family = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name
