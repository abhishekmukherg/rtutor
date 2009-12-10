"""
Forms for tutoring
"""

from django import forms


__all__ = ['ScrapeForm']


class ScrapeForm(forms.Form):

    """Form for scraping information from a url"""

    url = forms.URLField(verify_exists=True)

