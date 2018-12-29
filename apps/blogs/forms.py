from django import forms

from .models import Blog


class BlogForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.blog_post = kwargs.pop('blog_post', None)
        super().__init__(*args, **kwargs)
        self.fields['title'].required = True
        self.fields['content'].required = True
        if self.blog_post:
            self.fields['title'].initial = self.blog_post.title
            self.fields['content'].initial = self.blog_post.content
            self.fields['author'].initial = self.blog_post.author
            self.fields['pub_date'].initial = self.blog_post.pub_date
            self.fields['is_hidden'].initial = self.blog_post.is_hidden

    class Meta:
        model = Blog
        fields = ('title', 'author', 'pub_date', 'content', 'is_hidden')

    def save(self, commit=True):
        super().save(commit=commit)
