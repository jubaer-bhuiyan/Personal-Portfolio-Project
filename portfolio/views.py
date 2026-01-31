from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import (
    Project, Skill, ProgrammingLanguage, Experience,
    Education, Certification, PersonalInfo, ContactMessage
)

def home(request):
    try:
        personal_info = PersonalInfo.objects.first()
    except PersonalInfo.DoesNotExist:
        personal_info = None
    
    context = {
        'personal_info': personal_info,
        'projects': Project.objects.all(),
        'skills': Skill.objects.all(),
        'programming_languages': ProgrammingLanguage.objects.all(),
        'experiences': Experience.objects.all(),
        'educations': Education.objects.all(),
        'certifications': Certification.objects.all(),
    }
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Save to database
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        # Send email to you
        try:
            email_subject = f'Portfolio Contact: {subject}'
            email_message = f'''
You have received a new message from your portfolio website!

From: {name}
Email: {email}
Subject: {subject}

Message:
{message}

---
This message was sent from your portfolio contact form.
            '''
            
            send_mail(
                email_subject,
                email_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            messages.success(request, 'Thank you for your message! I will get back to you soon.')
        except Exception as e:
            # Still show success to user even if email fails
            # The message is saved in database anyway
            messages.success(request, 'Thank you for your message! I will get back to you soon.')
            print(f"Email error: {e}")  # For debugging
        
        return redirect('home')
    
    return render(request, 'portfolio/home.html', context)