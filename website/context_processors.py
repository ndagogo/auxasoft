from django.conf import settings


def company_info(request):
    return {
        'company': settings.COMPANY,
        'newsletter_form_action': 'website:newsletter',
    }
