from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from django.views.decorators.csrf import csrf_exempt
from django.dispatch import receiver
from .models import Transaction,Pool
from django.contrib.auth.models import User
from django.conf import settings

@csrf_exempt
@receiver(valid_ipn_received)
def webhook(sender, **kwargs):
    ipn_obj = sender
    print(ipn_obj)
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        transaction = Transaction.objects.create(
            # sender=User.objects.get(username=ipn_obj.custom),
            # sender = settings.AUTH_USER_MODEL.objects.get(username=ipn_obj.custom),
            sender = ipn_obj.custom,
            receiver=ipn_obj.item_name,
            sender_paypal_email=ipn_obj.payer_email,
            receiver_paypal_email=ipn_obj.receiver_email,
            date=ipn_obj.payment_date,
            amount=ipn_obj.mc_gross,
            currency=ipn_obj.mc_currency,
            payment_status=ipn_obj.payment_status,
            mode_of_payment=ipn_obj.payment_type,
            # user_country
            # ngo_country
        )
        print(f"{ipn_obj.item_name}\n{ipn_obj.receiver_email}\n")
        # Save the Transaction instance
        transaction.save()

        pool = Pool.objects.create(
            # sender=User.objects.get(username=ipn_obj.custom),
            # sender = settings.AUTH_USER_MODEL.objects.get(username=ipn_obj.custom),
            sender = ipn_obj.custom,
            receiver=ipn_obj.item_name,
            sender_paypal_email=ipn_obj.payer_email,
            receiver_paypal_email=ipn_obj.receiver_email,
            date=ipn_obj.payment_date,
            amount=ipn_obj.mc_gross,
            currency=ipn_obj.mc_currency,
            payment_status=ipn_obj.payment_status,
            mode_of_payment=ipn_obj.payment_type,
        )
        # Save the Pool instance
        pool.save()
        # anything
