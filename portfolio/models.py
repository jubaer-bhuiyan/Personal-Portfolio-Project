from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    order = models.IntegerField(default=0, help_text="Lower number appears first")
    
    class Meta:
        ordering = ['order', '-id']
    
    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Proficiency percentage (0-100)"
    )
    category = models.CharField(
        max_length=50,
        choices=[
            ('technical', 'Technical Skills'),
            ('soft', 'Soft Skills'),
            ('tools', 'Tools & Technologies'),
        ],
        default='technical'
    )
    icon = models.CharField(max_length=50, blank=True, help_text="FontAwesome icon class (e.g., 'fa-python')")
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'name']
    
    def __str__(self):
        return f"{self.name} ({self.proficiency}%)"


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=50)
    proficiency = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    icon = models.CharField(max_length=50, blank=True, help_text="FontAwesome icon class")
    color = models.CharField(max_length=7, default="#007bff", help_text="Hex color code")
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order', 'name']
    
    def __str__(self):
        return self.name


class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True, help_text="Leave blank if currently working")
    description = models.TextField()
    is_current = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.title} at {self.company}"


class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True, blank=True, help_text="Leave blank if ongoing")
    gpa = models.CharField(max_length=10, blank=True, help_text="e.g., 3.8/4.0")
    description = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-start_year']
    
    def __str__(self):
        return f"{self.degree} - {self.institution}"


class Certification(models.Model):
    name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    date_obtained = models.DateField()
    credential_id = models.CharField(max_length=200, blank=True)
    credential_url = models.URLField(blank=True)
    
    class Meta:
        ordering = ['-date_obtained']
    
    def __str__(self):
        return f"{self.name} - {self.issuer}"


class PersonalInfo(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200, help_text="e.g., 'Full Stack Developer'")
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='portfolio/profile/')
    resume = models.FileField(upload_to='portfolio/resume/', blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=200, blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    
    class Meta:
        verbose_name_plural = "Personal Information"
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.pk and PersonalInfo.objects.exists():
            raise ValueError('Only one PersonalInfo instance is allowed')
        return super().save(*args, **kwargs)


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Message from {self.name} - {self.subject}"