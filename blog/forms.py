from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    model = Post
    fields = ['title','content']
    widgets ={
        'title' : forms.TextInput(
            attrs={'class': 'form-control' , 'placehoder' :'Digite o Titulo'}
        ),
        'content' : forms.Textarea(
            attrs={'class': 'form-control' , 'placehoder' :'Digite o Conteudo'}
        ),
    }
    
    def clean_title(self):
        title  = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError('O Titulo deve possuir mais de 5 caracteres.')
        return title
    
    def clean_content(self):
        content  = self.cleaned_data.get('content')
        if len(content) < 20:
            raise forms.ValidationError('O Conteudo deve possuir mais de 20 caracteres.')
        return content
    

