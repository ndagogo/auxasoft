from django.core.management.base import BaseCommand
from django.utils import timezone

from website.models import (
    BlogPost,
    FAQ,
    JobOpening,
    Project,
    Service,
    TeamMember,
    Testimonial,
)


class Command(BaseCommand):
    help = 'Seed demo content for AUXANOS GLOBAL SOLUTIONS LTD'

    def handle(self, *args, **options):
        self.stdout.write('Seeding AUXANOS content...')

        services = [
            {
                'title': 'Software Development',
                'icon': 'bi-code-slash',
                'short_description': 'Custom enterprise applications engineered for scale, security, and speed.',
                'description': (
                    'We design and build bespoke software platforms that streamline operations, '
                    'unlock data, and create lasting competitive advantage. From discovery to '
                    'deployment, our engineers partner with your stakeholders to deliver '
                    'reliable, maintainable systems.'
                ),
                'features': 'Requirements discovery & architecture\nWeb & desktop applications\nAPI & integrations\nCloud-native delivery\nOngoing support & optimization',
                'order': 1,
            },
            {
                'title': 'IT Consultancy',
                'icon': 'bi-briefcase',
                'short_description': 'Strategic technology advisory that aligns IT investments with business outcomes.',
                'description': (
                    'Our consultants help organizations assess infrastructure, modernize legacy systems, '
                    'and define digital roadmaps. We translate complex technology decisions into clear '
                    'business value.'
                ),
                'features': 'Digital transformation roadmaps\nIT audits & assessments\nArchitecture reviews\nVendor & stack selection\nGovernance & best practices',
                'order': 2,
            },
            {
                'title': 'Mobile App Development',
                'icon': 'bi-phone',
                'short_description': 'Native and cross-platform mobile experiences that users love.',
                'description': (
                    'From consumer apps to enterprise field tools, we craft polished iOS and Android '
                    'applications with intuitive UX, robust backends, and measurable engagement.'
                ),
                'features': 'iOS & Android development\nCross-platform (Flutter / React Native)\nUI/UX design\nApp Store & Play Store launch\nAnalytics & iteration',
                'order': 3,
            },
            {
                'title': 'Networking Solutions',
                'icon': 'bi-hdd-network',
                'short_description': 'Secure, resilient network infrastructure for modern enterprises.',
                'description': (
                    'We design, deploy, and manage network environments that keep your people and '
                    'systems connected — with security, uptime, and performance at the core.'
                ),
                'features': 'LAN / WAN / WLAN design\nFirewall & security hardening\nVPN & remote access\nMonitoring & maintenance\nStructured cabling & hardware',
                'order': 4,
            },
            {
                'title': 'Cloud & DevOps',
                'icon': 'bi-cloud-check',
                'short_description': 'Cloud migration, automation, and continuous delivery pipelines.',
                'description': (
                    'Accelerate delivery with infrastructure as code, CI/CD, and cloud platforms '
                    'tuned for cost, reliability, and growth.'
                ),
                'features': 'AWS / Azure / GCP\nCI/CD pipelines\nContainerization & Kubernetes\nObservability\nCost optimization',
                'order': 5,
            },
            {
                'title': 'Cybersecurity & Hi-Tech',
                'icon': 'bi-shield-lock',
                'short_description': 'Advanced security and emerging technology solutions for tomorrow’s threats.',
                'description': (
                    'Protect your digital assets with layered security practices and explore '
                    'hi-tech capabilities — IoT, AI-assisted systems, and intelligent automation.'
                ),
                'features': 'Security assessments\nIdentity & access management\nEndpoint protection\nIoT & smart systems\nAI / automation advisory',
                'order': 6,
            },
        ]

        for data in services:
            obj, created = Service.objects.update_or_create(
                title=data['title'],
                defaults=data,
            )
            if not obj.slug:
                obj.save()

        projects = [
            {
                'title': 'Enterprise Operations Platform',
                'client': 'Regional Logistics Group',
                'category': 'software',
                'summary': 'End-to-end operations dashboard unifying fleet, inventory, and billing.',
                'description': 'A modular web platform that replaced fragmented spreadsheets with real-time operational visibility across multiple depots.',
                'technologies': 'Django, React, PostgreSQL, Redis',
                'is_featured': True,
                'order': 1,
            },
            {
                'title': 'Field Service Mobile Suite',
                'client': 'National Utilities Partner',
                'category': 'mobile',
                'summary': 'Offline-first mobile app for technicians managing work orders on site.',
                'description': 'Cross-platform mobile application with sync, GPS tagging, and photo evidence capture for field teams.',
                'technologies': 'Flutter, Firebase, REST APIs',
                'is_featured': True,
                'order': 2,
            },
            {
                'title': 'Secure Branch Network Rollout',
                'client': 'Multi-site Retail Brand',
                'category': 'network',
                'summary': 'Standardized secure networking across 40+ retail locations.',
                'description': 'Designed and deployed segmented networks, SD-WAN connectivity, and centralized monitoring.',
                'technologies': 'Cisco, Fortinet, Zabbix',
                'is_featured': True,
                'order': 3,
            },
            {
                'title': 'Digital Transformation Roadmap',
                'client': 'Financial Services SME',
                'category': 'consulting',
                'summary': '18-month technology modernization strategy and vendor selection.',
                'description': 'Comprehensive IT assessment culminating in a phased cloud migration and application modernization plan.',
                'technologies': 'TOGAF, Azure, Power BI',
                'is_featured': False,
                'order': 4,
            },
        ]

        for data in projects:
            Project.objects.update_or_create(title=data['title'], defaults=data)

        team = [
            {'name': 'Adaeze Okonkwo', 'role': 'Managing Director', 'bio': 'Leads strategy and client partnerships across West Africa.', 'order': 1},
            {'name': 'Chinedu Adebayo', 'role': 'Head of Engineering', 'bio': 'Architects scalable platforms and mentors delivery teams.', 'order': 2},
            {'name': 'Fatima Ibrahim', 'role': 'Solutions Consultant', 'bio': 'Translates business goals into technology roadmaps.', 'order': 3},
            {'name': 'Tunde Balogun', 'role': 'Network & Security Lead', 'bio': 'Designs resilient infrastructure and security postures.', 'order': 4},
        ]
        for data in team:
            TeamMember.objects.update_or_create(name=data['name'], defaults=data)

        testimonials = [
            {
                'client_name': 'Ifeanyi Nwosu',
                'client_role': 'COO',
                'company': 'SwiftHaul Logistics',
                'quote': 'AUXANOS delivered a platform that finally gave us one source of truth across operations. Professional, precise, and proactive.',
                'rating': 5,
                'order': 1,
            },
            {
                'client_name': 'Amaka Eze',
                'client_role': 'IT Director',
                'company': 'BrightPath Retail',
                'quote': 'Their networking rollout was seamless. Downtime dropped dramatically and our branches finally feel like one connected business.',
                'rating': 5,
                'order': 2,
            },
            {
                'client_name': 'David Mensah',
                'client_role': 'Product Lead',
                'company': 'OrbitPay',
                'quote': 'The mobile app exceeded expectations — clean UX, solid engineering, and thoughtful post-launch support.',
                'rating': 5,
                'order': 3,
            },
        ]
        for data in testimonials:
            Testimonial.objects.update_or_create(client_name=data['client_name'], company=data['company'], defaults=data)

        now = timezone.now()
        posts = [
            {
                'title': 'Why Modern Enterprises Need a Digital Foundation',
                'excerpt': 'Technology is no longer a support function — it is the operating system of growth.',
                'content': (
                    'Organizations that treat technology as a strategic asset outperform those that treat it as an afterthought. '
                    'At AUXANOS, we help leaders build durable digital foundations — from software platforms to secure networks — '
                    'so innovation can scale without chaos.\n\n'
                    'A strong foundation includes clear architecture, reliable infrastructure, and delivery practices that '
                    'shorten the path from idea to production.'
                ),
                'author': 'AUXANOS Editorial',
                'published_at': now,
                'is_featured': True,
            },
            {
                'title': 'Mobile-First Field Operations: Lessons from Delivery',
                'excerpt': 'Offline capability and simple UX often matter more than feature volume.',
                'content': (
                    'Field teams work in unpredictable environments. The best mobile tools respect that reality: '
                    'they sync gracefully, capture evidence quickly, and stay usable on imperfect networks.\n\n'
                    'Our approach prioritizes the workflow, then the polish — ensuring adoption sticks.'
                ),
                'author': 'Chinedu Adebayo',
                'published_at': now,
            },
            {
                'title': 'Securing Branch Networks Without Slowing Growth',
                'excerpt': 'Segmentation, visibility, and standards turn multi-site IT into a controllable system.',
                'content': (
                    'As businesses expand locations, networks become attack surfaces and operational bottlenecks. '
                    'Standardized designs, centralized monitoring, and disciplined change management keep expansion '
                    'from becoming technical debt.'
                ),
                'author': 'Tunde Balogun',
                'published_at': now,
            },
        ]
        for data in posts:
            BlogPost.objects.update_or_create(title=data['title'], defaults=data)

        jobs = [
            {
                'title': 'Senior Software Engineer',
                'department': 'Engineering',
                'location': 'Lagos / Hybrid',
                'employment_type': 'full-time',
                'summary': 'Build and own critical product surfaces for enterprise clients.',
                'description': 'Join our engineering team to design, develop, and ship high-quality software solutions across web and API layers.',
                'requirements': '5+ years professional software experience\nStrong Python/Django or equivalent backend skills\nExperience with modern frontend stacks\nExcellent communication and ownership mindset',
            },
            {
                'title': 'IT Solutions Consultant',
                'department': 'Consultancy',
                'location': 'Lagos, Nigeria',
                'employment_type': 'full-time',
                'summary': 'Advise clients on technology strategy and solution design.',
                'description': 'Work closely with stakeholders to assess needs, propose architectures, and guide delivery partnerships.',
                'requirements': 'Proven consulting or solutions architecture experience\nBroad knowledge of cloud, software, and networking\nStrong presentation and stakeholder skills\nWillingness to travel within Nigeria as needed',
            },
        ]
        for data in jobs:
            JobOpening.objects.update_or_create(title=data['title'], defaults=data)

        faqs = [
            {
                'question': 'What industries do you serve?',
                'answer': 'We partner with organizations across logistics, retail, financial services, utilities, education, and growing SMEs seeking reliable technology partners.',
                'order': 1,
            },
            {
                'question': 'Do you work with startups and enterprises alike?',
                'answer': 'Yes. Engagements are scoped to fit — from focused MVP builds to multi-phase enterprise programs.',
                'order': 2,
            },
            {
                'question': 'How do projects typically start?',
                'answer': 'We begin with a discovery conversation, clarify goals and constraints, then propose a clear scope, timeline, and commercial model.',
                'order': 3,
            },
            {
                'question': 'Can you support systems after launch?',
                'answer': 'Absolutely. We offer managed support, maintenance retainers, and continuous improvement programs.',
                'order': 4,
            },
            {
                'question': 'Where are you based?',
                'answer': 'AUXANOS GLOBAL SOLUTIONS LTD is based in Lagos, Nigeria, and serves clients nationally and internationally.',
                'order': 5,
            },
        ]
        for data in faqs:
            FAQ.objects.update_or_create(question=data['question'], defaults=data)

        self.stdout.write(self.style.SUCCESS('Seed complete.'))
