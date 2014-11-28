from django import forms
from django.contrib import admin
from home.models import COMMENT, POST,TAICHINH


class POSTForm(forms.ModelForm):

    class Meta:
        model = POST
        fields = ('author', 'content')


class CustomPOSTAdmin(admin.ModelAdmin):
    fieldsets = None
    form = POSTForm
    list_display  = ('author', 'content', 'date',)
    search_fields = ('=content',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = COMMENT
        fields = ('author', 'content', 'post')


class CustomCommentAdmin(admin.ModelAdmin):
    fieldsets = None
    form = CommentForm
    list_display  = ('author', 'content', 'date',)
    search_fields = ('=content',)


class TaiChinhForm(forms.ModelForm):

    class Meta:
        model = TAICHINH
        fields = ('content','money','chi',)


class CustomTaiChinhAdmin(admin.ModelAdmin):
    fieldsets = None
    form = TaiChinhForm
    list_display  = ('author', 'content','money','chi','date', )
    search_fields = ('=content','=date')

    def save_model(self, request, obj, form, change): 
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        return instance

admin.site.register(TAICHINH, CustomTaiChinhAdmin)    
admin.site.register(POST, CustomPOSTAdmin)
admin.site.register(COMMENT, CustomCommentAdmin)