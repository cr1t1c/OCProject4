from django import forms

from . import models

class BookForm(forms.ModelForm):
    edit_review = forms.BooleanField(widget=forms.HiddenInput(), initial=True)

    class Meta:
        model = models.Book
        fields = ['title', 'description', 'image']

class ReviewForm(forms.ModelForm):

    rating = forms.ChoiceField(choices=[(i, i) for i in range(1,6)],
                               widget=forms.RadioSelect())
    edit_review = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Review
        fields = ['headline', 'rating', 'body']



class DeleteForm(forms.Form):
    delete_form = forms.BooleanField(widget=forms.HiddenInput, initial=True)