from django.contrib import admin
from .models import (
    BlogPost,
    ContactMessage,
    FAQ,
    JobOpening,
    NewsletterSubscriber,
    Project,
    Service,
    TeamMember,
    Testimonial,
)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured', 'is_active', 'order')
    list_filter = ('is_featured', 'is_active')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'short_description')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'client', 'is_featured', 'is_active', 'completed_on')
    list_filter = ('category', 'is_featured', 'is_active')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'client', 'summary')


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'is_active', 'order')
    list_filter = ('is_active',)
    search_fields = ('name', 'role')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'company', 'rating', 'is_featured', 'is_active')
    list_filter = ('is_featured', 'is_active', 'rating')


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_at', 'is_published', 'is_featured')
    list_filter = ('is_published', 'is_featured')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'excerpt', 'content')


@admin.register(JobOpening)
class JobOpeningAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'location', 'employment_type', 'is_open')
    list_filter = ('employment_type', 'is_open', 'department')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'order', 'is_active')
    list_filter = ('is_active',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'service_interest', 'is_read', 'created_at')
    list_filter = ('is_read', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('email',)
