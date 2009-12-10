"""
Views for tutoring
"""

import tutoring.forms

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import permission_required


__all__ = ['scrape']


@permission_required(u'tutoring.add_subject')
@permission_required(u'tutoring.add_course')
@permission_required(u'tutoring.add_courselisting')
def scrape(request,
        next_page=None,
        template_name='tutoring/scrape.html'):
    """Scrapes a url

    given the information in the url, it'll fill CourseListing with values
    """
    if request.method == 'POST':
        form = tutoring.forms.ScrapeForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(next_page) # Redirect after POST
    else:
        form = tutoring.forms.ScrapeForm()

    return render_to_response(template_name, {
        'form': form,
    }, context_instance=RequestContext(request))

