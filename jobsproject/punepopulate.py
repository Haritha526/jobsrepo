import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jobsproject.settings')
import django
django.setup()
from jobsapp.models import PuneJobs
from faker import Faker
from random import *
fake = Faker()

def phonenumbergen():
    d1 = randint(6,9)
    num = ""+str(d1)
    for i in range(9):
        num += str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company
        ftitle = fake.random_element(elements=('Project Manager','Team Lead','Software Engineer','Assosiate Engineer'))
        feligibility = fake.random_element(elements=('B.Tech','M.tech','MCA','PHD'))
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = phonenumbergen()
        PuneJobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phonenumber=fphonenumber)
n=int(input('enter number of records:'))
populate(n)
print(f'{n} records inserted successfully...........')
