from django.db import models
from django.contrib.auth.models import User
from django.utils.text import get_text_list
from django.utils.encoding import force_text
from django.utils.translation import ugettext as _

class DataSet(models.Model):
    name = models.CharField(max_length=100)
    create_time = models.DateTimeField('date published')
    
    def __unicode__(self):
        return self.name
    
# Create your models here.
class Project(models.Model):
    def __init__(self, *args, **kwargs):
        super(Project, self).__init__(*args, **kwargs)
        self.unsaved = {}
        for field in self._meta.fields:
            self.unsaved[field.name] = getattr(self, field.name, None)

    def construct_change_message(self, force_insert=False, force_update=False, using=None):
        oldArr = {}
        newArr = {}
        change_message = []
        changed_fields = []
        old_values = ''
        new_values = ''
        for name, value in self.unsaved.iteritems():
            if not value == getattr(self, name, None):
                changed_fields.append(name)
                old_values = old_values + str(value) + ' SEP '
                new_values = new_values + str(getattr(self, name, None)) + ' SEP '
                
        change_message.append(_('Changed %(list)s.')
                % {'list': get_text_list(changed_fields, _('and'))})        
                
        # change_message.append(_('Changed %(list)s for %(name)s "%(object)s".')
                # % {'list': get_text_list(changed_fields, _('and')),
                # 'name': force_text(self._meta.verbose_name),
                # 'object': force_text(self)})
        #print "Field:%s Old:%s New:%s" % (name, value, getattr(self, name, None))
        change_message = ' '.join(change_message)
        return change_message or _('No fields changed.')  
        # old values can be accessed through the self.unsaved member
        # super(MyModel, self).save(force_insert, force_update, using)
        
    user = models.ForeignKey(User)
    dataset = models.ForeignKey(DataSet)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    create_time = models.DateTimeField('date published')
    is_private = models.BooleanField(default = 1)
    is_deleted = models.BooleanField(default = 0)
    
    # Relations
    collaborators = models.ManyToManyField(User, 
                                                 related_name=u"user_projects", 
                                                 blank=True)
    
    def __unicode__(self):
        return self.name   
        
    def is_creator(self, user):
        return user == self.user #or user.has_perm('your_app.manage_object')
        
    def is_collaborator(self, user):
        return user in self.collaborators.all()   
    
class Comment(models.Model):
    project = models.ForeignKey(Project)
    user = models.ForeignKey(User)
    content = models.CharField(max_length=500)    
    create_time = models.DateTimeField('date published')
    is_deleted = models.BooleanField(default = 0)
    
    edit_enable = False
    
    def __unicode__(self):
        return self.content   
    
    def is_comment_creator(self, user):
        return user == self.user
        
    def is_project_creator(self, user):
        return user == self.project.user
        
    class Meta:
        ordering = ['-create_time']
        
class Doc(models.Model):
    dataset = models.ForeignKey(DataSet)
    people = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    misc = models.CharField(max_length=200)
    text = models.CharField(max_length=200)