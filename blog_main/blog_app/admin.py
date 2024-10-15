from django.contrib import admin
from .models import  Post, Category
from ckeditor.widgets import CKEditorWidget
from django import forms 


# Register your models here.


class PostAdminForm(forms.ModelForm):
    content=forms.CharField(widget=CKEditorWidget())
    
    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    list_display=('title', 'author', 'category', 'created_at')
    list_filter =('category', 'author', 'created_at')
    search_fields= ('title', 'content')
    prepopulated_fields = {'slug': ('title', )}
    raw_id_fields = ('author', )
    date_hierarchy = 'created_at'
    ordering = ('created_at', )
    
    form = PostAdminForm
    
    

    


# # Replace 'admin' with the actual username of the superuser
# user = User.objects.get(username='sai2773')
# user.set_password('pavan2241')  # Replace 'new_password' with your new password
# user.save()

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
