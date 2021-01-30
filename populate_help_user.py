import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proTwo.settings')

import django
django.setup()

# import random
from help.models import User
from faker import Faker

fake = Faker()


def add_user(N=5):
    for entry in range(N):
        f_name = fake.first_name()
        l_name = fake.last_name()
        email = fake.ascii_safe_email()
        phone = fake.phone_number()

        User.objects.get_or_create(first_name=f_name, last_name=l_name, email=email, phone=phone)


if __name__ == "__main__":
    print('generating data')
    add_user(20)
    print('fake data is created')
