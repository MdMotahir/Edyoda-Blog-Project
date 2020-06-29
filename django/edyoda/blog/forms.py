from django import forms
from blog.models import Category,Post
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.utils.text import slugify
from django.core.exceptions import ObjectDoesNotExist


class ContactUsForm(forms.Form):
    name=forms.CharField(max_length=100,help_text='your name please')
    email=forms.EmailField(required=False)
    contact=forms.RegexField(regex="^[6-9]\d{9}", required=False)

    def clean(self):
        cleaned_data=super().clean()
        if not (cleaned_data.get('email') or cleaned_data.get('contact')):
            raise forms.ValidationError('Please Enter Email or Phone Number',code="Invalid")

class PostCreateForm(forms.ModelForm):
    content=forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = Post
        fields = ('title','content','status','category','image_url','image')

    def clean_title(self):
        cleaned_data=super().clean()
        title=cleaned_data.get('title')
        slug=slugify(title)
        try:
            post_obj=Post.objects.get(slug=slug)
            raise forms.ValidationError("Title is already exits",code='Invalid')
        except ObjectDoesNotExist:
            return title

    # def clean_image(self):
    #     image=self.cleaned_data.get('image')
    #     if image:
    #         if image.size >= 2621440:
    #             raise forms.ValidationError("Image must be less than 2.5 mb",code="Invalid")

class PostUpdateForm(forms.ModelForm):
    content=forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = Post
        fields = ('title','content','status','category','image_url','image')
        
    # def clean_image(self):
    #     image=self.cleaned_data.get('image')
    #     if image:
    #         if image.size >= 2621440:
    #             raise forms.ValidationError("Image must be less than 2.5 mb",code="Invalid")