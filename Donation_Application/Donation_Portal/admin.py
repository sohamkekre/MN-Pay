from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import(
    Customer,
    Transaction,
    Pool,
    # Miner,
    NGO,
    CustomUser,
    Country,
    UserType
)
# Register your models here.
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','phone','address','country']
    # 'ac_number','ifsc_code'

@admin.register(Transaction)
class TransactionModelAdmin(admin.ModelAdmin):
    list_display = ['id','sender','receiver','sender_paypal_email','receiver_paypal_email','payment_status','date','amount','currency','mode_of_payment']

@admin.register(Pool)
class PoolModelAdmin(admin.ModelAdmin):
    list_display = ['id','sender','receiver','sender_paypal_email','receiver_paypal_email','payment_status','date','amount','currency','mode_of_payment']

# @admin.register(Miner)
# class MinerModelAdmin(admin.ModelAdmin):
#     list_display = ['id','ip_address','country']

@admin.register(NGO)
class NGOModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','contact_person','email','phone_number','address','country','mission_statement','website','registration_proof']
    # 'bank_account_number','registration_number','social_media_links',,'created_at'

@admin.register(Country)
class CountryModelAdmin(admin.ModelAdmin):
    list_display = ['country_code','country_name','country_account']

@admin.register(UserType)
class UserTypeModelAdmin(admin.ModelAdmin):
    list_display = ['user_type']

class CustomUserAdmin(UserAdmin):
    list_display = ('username','email', 'first_name', 'last_name', 'is_staff', 'country', 'user_type')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username','email', 'first_name', 'last_name')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'country', 'user_type')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','first_name','last_name','country',
                       'user_type' ,'email', 'password1', 'password2'),
        }),
    )

# Register the custom user admin class with your CustomUser model
admin.site.register(CustomUser, CustomUserAdmin)