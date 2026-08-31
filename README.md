# AUXANOS GLOBAL SOLUTIONS LTD

Corporate website for **AUXANOS GLOBAL SOLUTIONS LTD** — Software Development, IT Consultancy, Mobile App Development, Networking, and Hi-Tech solutions.

Built with **Django** and **Bootstrap 5**.

## Features

- Home, About, Services (with detail pages)
- Projects portfolio with category filters
- Team, Insights/Blog with search
- Careers with job detail pages
- Contact form (saved to admin + console email)
- FAQ, Privacy Policy, Terms of Use
- Newsletter signup
- Django admin CMS for all content

## Quick start

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_data
python manage.py createsuperuser
python manage.py runserver
```

Visit:

- Site: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## Configuration

Update company details in `config/settings.py` under `COMPANY` (name, email, phone, address).

Optional environment variables:

- `DJANGO_SECRET_KEY`
- `DJANGO_DEBUG`
- `DJANGO_ALLOWED_HOSTS`
- `CONTACT_EMAIL`
