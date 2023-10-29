from django import forms

from .models import Quote, Author, Tag


class QuoteForm(forms.ModelForm):
    quote = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "rows": "5"})
    )
    author = forms.ModelChoiceField(
        queryset=Author.objects.all().order_by("fullname"),
        empty_label="Оберіть автора",
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all().order_by("name"),
        widget=forms.SelectMultiple(
            attrs={
                "size": "12",
            },
        ),
    )

    class Meta:
        model = Quote
        fields = ["quote", "author", "tags"]


class AuthorForm(forms.ModelForm):
    fullname = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                # "placeholder": "Input fullname",
            }
        ),
    )
    born_date = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                #    "placeholder": "Input born date",
            }
        ),
    )
    born_location = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                #    "placeholder": "Input born location",
            }
        ),
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                #    "placeholder": "Input description",
            }
        )
    )

    class Meta:
        model = Author
        fields = ["fullname", "born_date", "born_location", "description"]
