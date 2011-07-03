from django.db import models

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=200)
    founded_date = models.DateField()
    legal_status = models.CharField(max_length=50)
    number_staff = models.IntegerField('number of staff')
    contact_person = models.ForeignKey('Person', related_name='+')
    
    def __unicode__(self):
            return self.name
            
class Person(models.Model):
    ENUM_CHOICES = (
        (u'Y', u'Yes'),
        (u'N', u'No'),
    )
    organization = models.ForeignKey(Organization)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    attended_trainings = models.CharField(max_length=2, choices=ENUM_CHOICES)
    electoral_experience = models.CharField(max_length=2, choices=ENUM_CHOICES)
    active_projects = models.CharField(max_length=255)
    
    def __unicode__(self):
            return self.name
    
class Internal(models.Model):
    ENUM_CHOICES = (
        (u'Y', u'Yes'),
        (u'N', u'No'),
    )
    
    RELATIONSHIP_CHOICES = (
        (u'Da', u'Dating'),
        (u'Di', u'Divorced'),
        (u'Ma', u'Married'),
        (u'Si', u'Single'),        
    )    
    
    ACTIVITY_CHOICES = (
        (u'Pro', u'Proactive'),
        (u'Re', u'Reactive'),
    )
    
    organization = models.ForeignKey(Organization)
    relationship_status = models.CharField(max_length=4, choices=RELATIONSHIP_CHOICES)
    familiarity = models.CharField(max_length=2, choices=ENUM_CHOICES)
    action_steps = models.TextField()
    activity_level = models.CharField(max_length=4, choices=ACTIVITY_CHOICES)
    
    def __unicode__(self):
            return self.name
