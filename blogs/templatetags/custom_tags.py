from django import template
from blogs.models import Category,Post

register =template.Library()

@register.simple_tag(name="categories")

def all_categories():
    return Category.objects.all()[:5]

@register.simple_tag(name="category_page")

def category():
    return Category.objects.all()    

@register.simple_tag(name="hit_posts")

def hit_posts():

    return Post.objects.order_by('-hit')[:4]