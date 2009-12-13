# Copyright (C) 2009 Abhishek Mukherjee <abhishek.mukher.g@gmail.com>
#
# This file is part of rtutor.
#
# rtutor is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# rtutor is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with rtutor.  If not, see <http://www.gnu.org/licenses/>.

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

