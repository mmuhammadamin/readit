from  django import forms
from apps.articles.models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields='__all__'
        exclude=['post']
    def __init__(self,*args,**kwargs):
        super(CommentForm,self).__init__(*args,**kwargs)
        self.fields['full_name'].widget.attrs['placeholder']='Your name'
        self.fields['message'].widget.attrs['placeholder'] = 'Your message'
