from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

@receiver(post_save,sender=get_user_model())
def assign_default_group(sender,instance,created,**kwargs):
    if created:
        Reader=Group.objects.get(name='Reader')
        Author=Group.objects.get(name='Author')
        if instance.category == 'R':
            instance.groups.add(Reader)
        else:
            instance.groups.add(Author)