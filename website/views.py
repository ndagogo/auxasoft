from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView, TemplateView

from .forms import ContactForm, NewsletterForm
from .models import (
    BlogPost,
    FAQ,
    JobOpening,
    Project,
    Service,
    TeamMember,
    Testimonial,
)


class HomeView(TemplateView):
    template_name = 'website/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'services': Service.objects.filter(is_active=True, is_featured=True)[:6],
            'projects': Project.objects.filter(is_active=True, is_featured=True)[:3],
            'testimonials': Testimonial.objects.filter(is_active=True, is_featured=True)[:4],
            'posts': BlogPost.objects.filter(is_published=True)[:3],
            'team_preview': TeamMember.objects.filter(is_active=True)[:4],
        })
        return context


class AboutView(TemplateView):
    template_name = 'website/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team'] = TeamMember.objects.filter(is_active=True)
        context['testimonials'] = Testimonial.objects.filter(is_active=True)[:3]
        return context


class ServiceListView(ListView):
    model = Service
    template_name = 'website/services.html'
    context_object_name = 'services'

    def get_queryset(self):
        return Service.objects.filter(is_active=True)


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'website/service_detail.html'
    context_object_name = 'service'
    slug_field = 'slug'

    def get_queryset(self):
        return Service.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_services'] = (
            Service.objects.filter(is_active=True)
            .exclude(pk=self.object.pk)[:3]
        )
        return context


class ProjectListView(ListView):
    model = Project
    template_name = 'website/projects.html'
    context_object_name = 'projects'
    paginate_by = 9

    def get_queryset(self):
        qs = Project.objects.filter(is_active=True)
        category = self.request.GET.get('category')
        if category:
            qs = qs.filter(category=category)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Project.CATEGORY_CHOICES
        context['active_category'] = self.request.GET.get('category', '')
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'website/project_detail.html'
    context_object_name = 'project'
    slug_field = 'slug'

    def get_queryset(self):
        return Project.objects.filter(is_active=True)


class TeamView(ListView):
    model = TeamMember
    template_name = 'website/team.html'
    context_object_name = 'team'

    def get_queryset(self):
        return TeamMember.objects.filter(is_active=True)


class BlogListView(ListView):
    model = BlogPost
    template_name = 'website/blog.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        qs = BlogPost.objects.filter(is_published=True)
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(
                Q(title__icontains=q)
                | Q(excerpt__icontains=q)
                | Q(content__icontains=q)
            )
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'website/blog_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_posts'] = (
            BlogPost.objects.filter(is_published=True)
            .exclude(pk=self.object.pk)[:4]
        )
        return context


class CareerListView(ListView):
    model = JobOpening
    template_name = 'website/careers.html'
    context_object_name = 'jobs'

    def get_queryset(self):
        return JobOpening.objects.filter(is_open=True)


class CareerDetailView(DetailView):
    model = JobOpening
    template_name = 'website/career_detail.html'
    context_object_name = 'job'
    slug_field = 'slug'

    def get_queryset(self):
        return JobOpening.objects.filter(is_open=True)


class FAQView(ListView):
    model = FAQ
    template_name = 'website/faq.html'
    context_object_name = 'faqs'

    def get_queryset(self):
        return FAQ.objects.filter(is_active=True)


class ContactView(TemplateView):
    template_name = 'website/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = kwargs.get('form') or ContactForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            inquiry = form.save()
            try:
                send_mail(
                    subject=f'[AUXANOS] {inquiry.subject}',
                    message=(
                        f'From: {inquiry.name} <{inquiry.email}>\n'
                        f'Phone: {inquiry.phone}\n'
                        f'Company: {inquiry.company}\n'
                        f'Service: {inquiry.service_interest}\n\n'
                        f'{inquiry.message}'
                    ),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=True,
                )
            except Exception:
                pass
            messages.success(
                request,
                'Thank you. Your message has been received. Our team will respond shortly.',
            )
            return redirect('website:contact')
        messages.error(request, 'Please correct the errors below and try again.')
        return self.render_to_response(self.get_context_data(form=form))


class PrivacyView(TemplateView):
    template_name = 'website/privacy.html'


class TermsView(TemplateView):
    template_name = 'website/terms.html'


def newsletter_subscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            from .models import NewsletterSubscriber
            NewsletterSubscriber.objects.get_or_create(email=email)
            messages.success(request, 'You are subscribed to AUXANOS insights.')
        else:
            messages.error(request, 'Please enter a valid email address.')
    next_url = request.POST.get('next') or request.META.get('HTTP_REFERER') or '/'
    return redirect(next_url)
