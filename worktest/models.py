#-*- coding:utf-8 -*-
from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    SHIRT_SIZES = (
        (u'input', u'input'),
        (u'textarea', u'textarea'),
        (u'radio', u'radio'),
        (u'checkbox', u'checkbox'),
    )
    
    name = models.CharField(max_length=400)
    type = models.CharField(max_length=8, choices=SHIRT_SIZES)
    correctanswer = models.CharField(max_length=8)
    
    def __unicode__(self):
        return self.name
    
    
class Answer(models.Model):
    q = models.ForeignKey(Question)
    a = models.CharField(max_length=40)
    
    def __unicode__(self):
        return self.a
    
    

    
