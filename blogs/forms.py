from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Field,Submit
from .models import *
from django import forms

class PostCreationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PostCreationForm,self).__init__(*args,**kwargs)
        self.helper=FormHelper()

        self.helper.form_method="post"
        self.helper.field_class="mt-10"
        self.helper.layout=Layout(
            Field("title",css_class="single-input"),
            Field("category",css_class="single-input"),
            Field("content",css_class="single-input"),
            Field("image",css_class="single-input"),
        )
        self.helper.add_input(Submit('submit',"Paylaş",css_class="genric-btn success circle mt-4"))
    class Meta:
        model=Post
        labels={
            "title":"Başlık",
            "category":"Kategoriler",
            "content":"İçerik",
            "image":"Resim Seç"
        }
        fields=[
            "title",
            "category",
            "content",
            "image"
        ]

class PostUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PostUpdateForm,self).__init__(*args,**kwargs)
        self.helper=FormHelper()

        self.helper.form_method="post"
        self.helper.field_class="mt-10"
        self.helper.layout=Layout(
            Field("title",css_class="single-input"),
            Field("category",css_class="single-input"),
            Field("content",css_class="single-input"),
            Field("image",css_class="single-input"),
        )
        self.helper.add_input(Submit('submit',"Güncelle",css_class="genric-btn success circle mt-4"))
    class Meta:
        model=Post
        labels={
            "title":"Başlık",
            "category":"Kategoriler",
            "content":"İçerik",
            "image":"Resim Seç"
        }
        fields=[
            "title",
            "category",
            "content",
            "image"
        ]
class CreateCommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateCommentForm,self).__init__(*args,**kwargs)
        self.helper=FormHelper()
        self.helper.form_method="post"
        self.helper.layout=Layout(
            Field("name",css_class="form-control"),
            Field("email",css_class="form-control"),
            Field("content",css_class="form-control mb-10"),
        )

        self.helper.add_input(Submit("submit","Yorum Ekle",css_class="primary-btn submit_btn"))
    class Meta:
        model=Comment
        fields=[
            "name",
            "email",
            "content"
        ]        