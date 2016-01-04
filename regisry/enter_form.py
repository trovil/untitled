__author__ = 'Kompik'
from django import forms
from django.contrib import auth
from django.contrib.auth.models import User,Group

class EnterForm(forms.Form):
    username = forms.CharField(max_length=9, label='Username')
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(EnterForm, self).clean()
        if not self.errors:
            user = auth.authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
            if user is None:
                raise forms.ValidationError('Please enter the correct username and password')
            self.user = user
        return cleaned_data

    def get_user(self):
        user = self.user
        if not user.groups.filter(name='blog_user'):
            user = User.objects.get(username=user.username)
            g = Group.objects.get(name='blog_user')
            g.user_set.add(user)
        return self.user or None