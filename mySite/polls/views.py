from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader

from polls.models import Poll

"""
def index(request):
    latest_poll_list = Poll.objects.order_by('-publication_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_poll_list': latest_poll_list,
        })
    return HttpResponse(template.render(context))
    """

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-publication_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)

def detail(request, poll_id):
    return HttpResponse("<br><font size='12' face='verdana'>You're looking at poll %s.</font>" % poll_id)

    """try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render(request, 'polls/detail.html', {'poll': poll})"""

def results(request, poll_id):
    return HttpResponse("<br><font size='12' face='verdana'>You're looking at the results of poll %s.</font>" % poll_id)

def vote(request, poll_id):
    return HttpResponse("<br><font size='12' face='verdana'>You're voting on poll %s.</font>" % poll_id)
