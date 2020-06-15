from django import forms
from django.forms import formset_factory
from p_library.models import Author, Book, Friend


class AuthorForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Author
        fields = '__all__'


class BookForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput)
    description = forms.CharField(widget=forms.TextInput)
    class Meta:
        model = Book
        fields = '__all__'


class FriendForm(forms.ModelForm):
    Full_name = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Friend
        fields = '__all__'

