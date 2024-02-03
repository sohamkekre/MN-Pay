from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class Country(models.Model):
    country_code = models.CharField(max_length=3)
    country_name = models.CharField(max_length=30, unique=True)
    country_account = models.CharField(max_length=50, default='null')
    def __str__(self):
        return self.country_name
    
class UserType(models.Model):
    user_type = models.CharField(max_length=10, unique=True)    
    def __str__(self):
        return self.user_type

class Customer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    phone = models.IntegerField()
    address = models.CharField(max_length=50)
    # country = models.CharField(max_length=20)
    country = models.ForeignKey(Country, on_delete=models.CASCADE,related_name='customer_country', to_field="country_name")
    # ac_number = models.IntegerField(unique=True)
    # ifsc_code = models.CharField(max_length=11)
    def __str__(self):
        return str(self.id)

class NGO(models.Model):
    name = models.CharField(max_length=50)
    # registration_number = models.CharField(max_length=50)
    contact_person = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    # country = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE,related_name='ngo_country', to_field="country_name")
    mission_statement = models.TextField()
    website = models.URLField(blank=True, null=True)
    # bank_account_number = models.CharField(max_length=30)
    # projects_description = models.TextField()
    # social_media_links = models.URLField(blank=True, null=True)
    registration_proof = models.ImageField(upload_to='media/static/images/')
    # accepted_terms = models.BooleanField(default=False)
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Transaction(models.Model):
    # sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sender')
    # receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receiver')
    sender = models.CharField(max_length=30)
    receiver = models.CharField(max_length=30)
    sender_paypal_email = models.EmailField()
    receiver_paypal_email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    currency = models.CharField(max_length=20)
    payment_status = models.CharField(max_length=30)
    mode_of_payment = models.CharField(max_length=20)

class Pool(models.Model):
    # sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pool_sender')
    # receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pool_receiver')
    sender = models.CharField(max_length=30)
    receiver = models.CharField(max_length=30)
    sender_paypal_email = models.EmailField()
    receiver_paypal_email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    currency = models.CharField(max_length=20)
    payment_status = models.CharField(max_length=30)
    mode_of_payment = models.CharField(max_length=20)

# adding attributes to users model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
from django.db import models
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    country = models.ForeignKey(Country, on_delete=models.CASCADE,related_name='user_country', to_field="country_name")
    user_type = models.ForeignKey(UserType, on_delete=models.CASCADE,related_name='type_user', to_field="user_type")

    groups = models.ManyToManyField(Group, blank=True, related_name='custom_users')  # Specify the related_name here
    user_permissions = models.ManyToManyField(Permission, blank=True,related_name='custom_users_permissions')  # Specify the related_name here

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [username, email, country]

    def __str__(self):
        return self.username