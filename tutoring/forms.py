from django import forms

class ScrapeForm(forms.Form):
    url = forms.URLField(verify_exists=True)

