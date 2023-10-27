from django import forms


class QuoteForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea, label="Текст цитати")

    class Meta:
        model = Quote
        fields = ["text"]
