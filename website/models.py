from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Service(TimeStampedModel):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True)
    icon = models.CharField(
        max_length=60,
        default='bi-cpu',
        help_text='Bootstrap Icons class, e.g. bi-code-slash',
    )
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    features = models.TextField(
        blank=True,
        help_text='One feature per line',
    )
    is_featured = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('website:service_detail', kwargs={'slug': self.slug})

    def feature_list(self):
        return [f.strip() for f in self.features.splitlines() if f.strip()]


class Project(TimeStampedModel):
    CATEGORY_CHOICES = [
        ('software', 'Software Development'),
        ('mobile', 'Mobile Apps'),
        ('network', 'Networking'),
        ('consulting', 'IT Consultancy'),
        ('hitech', 'Hi-Tech Solutions'),
    ]

    title = models.CharField(max_length=160)
    slug = models.SlugField(unique=True, blank=True)
    client = models.CharField(max_length=120, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='software')
    summary = models.CharField(max_length=255)
    description = models.TextField()
    technologies = models.CharField(
        max_length=255,
        blank=True,
        help_text='Comma-separated technologies',
    )
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    project_url = models.URLField(blank=True)
    is_featured = models.BooleanField(default=False)
    completed_on = models.DateField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', '-completed_on', 'title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('website:project_detail', kwargs={'slug': self.slug})

    def tech_list(self):
        return [t.strip() for t in self.technologies.split(',') if t.strip()]


class TeamMember(TimeStampedModel):
    name = models.CharField(max_length=120)
    role = models.CharField(max_length=120)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='team/', blank=True, null=True)
    email = models.EmailField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f'{self.name} — {self.role}'


class Testimonial(TimeStampedModel):
    client_name = models.CharField(max_length=120)
    client_role = models.CharField(max_length=120, blank=True)
    company = models.CharField(max_length=120, blank=True)
    quote = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5)
    is_featured = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return f'{self.client_name} ({self.company or "Client"})'


class BlogPost(TimeStampedModel):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    excerpt = models.CharField(max_length=300)
    content = models.TextField()
    cover_image = models.ImageField(upload_to='blog/', blank=True, null=True)
    author = models.CharField(max_length=120, default='AUXANOS Editorial')
    published_at = models.DateTimeField(blank=True, null=True)
    is_published = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['-published_at', '-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('website:blog_detail', kwargs={'slug': self.slug})


class JobOpening(TimeStampedModel):
    EMPLOYMENT_TYPES = [
        ('full-time', 'Full-time'),
        ('part-time', 'Part-time'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
    ]

    title = models.CharField(max_length=160)
    slug = models.SlugField(unique=True, blank=True)
    department = models.CharField(max_length=100)
    location = models.CharField(max_length=120, default='Lagos, Nigeria')
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPES, default='full-time')
    summary = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField(help_text='One requirement per line')
    is_open = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('website:career_detail', kwargs={'slug': self.slug})

    def requirement_list(self):
        return [r.strip() for r in self.requirements.splitlines() if r.strip()]


class FAQ(TimeStampedModel):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'question']
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

    def __str__(self):
        return self.question


class ContactMessage(TimeStampedModel):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    company = models.CharField(max_length=120, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    service_interest = models.ForeignKey(
        Service,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='inquiries',
    )
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name}: {self.subject}'


class NewsletterSubscriber(TimeStampedModel):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.email
