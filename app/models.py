

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser,User
from app.managers import Custom_Manager
from django.utils.translation import gettext_lazy as _
from uuid import uuid4
from app.utils import UnicodeUsernameValidator
# Create your models here.



class CustomUser(AbstractUser):
    uu_id = models.UUIDField(_("UUID"),primary_key=True,default=uuid4,editable=False)
    is_online = models.BooleanField(default=False,editable=True)
    is_reserved = models.BooleanField(default=False,editable=True)

#    make sure remove these fields from admins.py also
    first_name = None
    last_name = None

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects =  Custom_Manager()

    def __str__(self):
        return self.username

room_name=UnicodeUsernameValidator()

class room_model(models.Model):
    room = models.CharField(_("ROOM NAMES"), max_length=50)
    slug = models.SlugField(unique=False,default='',null=False)

    def __str__(self):
        return self.room



# CREATE FAKE DATA FUNCTION
from faker import Faker
fk = Faker()
def create_fake_data(num=10):
    password ='ankit1234'

    for _ in range(num):
        name = fk.name()
        uu_id= uuid4()
        email= fk.email()

        print(f'username:{name}    uu_id:{uu_id}  email:{email} password:{password} ' ,sep=" ",end="\n")
        # db_object=CustomUser.objects.create(username=name,is_online=False,uu_id=uu_id,email=email,password=password)
        # db_object.save()
    
# call = create_fake_data(num=20)    


'''fake.name()
fake.address()
fake.email()
fake.text()
fake.country() 
fake.profile()
fake.sentence()'''