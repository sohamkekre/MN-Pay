from django.apps import AppConfig


class DonationPortalConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Donation_Portal'

    def ready(self):
        import Donation_Portal.hooks
