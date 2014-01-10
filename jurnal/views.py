from django.shortcuts import render_to_response, get_object_or_404
from jurnal.models import *
from django.template.context import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


MONTH_NAMES = ('', 'January', 'Feburary', 'March', 'April', 'May', 'June', 'July',
               'August', 'September', 'October', 'November', 'December')


def create_archive_data(obss):
    archive_data = []
    count = {}
    mcount = {}
    for obs in obss:
        year = obs.date.year
        month = obs.date.month
        if year not in count:
            count[year] = 1
            mcount[year] = {}
        else:
            count[year] += 1
        if month not in mcount[year]:
            mcount[year][month] = 1
        else:
            mcount[year][month] += 1
    for year in sorted(count.iterkeys(), reverse=True):
        archive_data.append({'isyear': True,
                             'year': year,
                             'count': count[year],})
        for month in sorted(mcount[year].iterkeys(), reverse=True):
            archive_data.append({'isyear': False,
                                 'yearmonth': '%d/%02d' % (year, month),
                                 'monthname': MONTH_NAMES[month],
                                 'count': mcount[year][month],})
    return archive_data


def index(request):
    if request.user.is_authenticated():
        return render_to_response('index.html', {'user': request.user})
    else:
        return render_to_response('index.html')


@login_required
def journal(request, year=None, month=None):
    obss = Obs.objects.order_by('-date')
    if year is not None:
        obss = obss.filter(date__year=year)
        if month is not None:
            obss = obss.filter(date__month=int(month))

    ar_obs = Obs.objects.all()
    archive = create_archive_data(ar_obs)
    return render_to_response('journal.html', {'obss': obss, 'user': request.user,
                                               'archive_counts': archive})


def contact(request):
    if request.user.is_authenticated():
        user = request.user
        return render_to_response('contact.html', {'user': user})
    else:
        return render_to_response('contact.html')


def about(request):
    if request.user.is_authenticated():
        user = request.user
        return render_to_response('about.html', {'user': user})
    else:
        return render_to_response('about.html')


def auth(request):
    state = "Please log in below..."
    username = ''
    if request.POST:
        username = request.POST.get('login')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                obss = Obs.objects.all()
                # return render_to_response('journal.html', {'state': state, 'obss': obss, 'user': user},
                #                           context_instance=RequestContext(request))
                return HttpResponseRedirect('journal.html', {'state': state, 'obss': obss, 'user': user})
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."

    return render_to_response('auth.html', {'state': state, 'username': username},
                              context_instance=RequestContext(request))


def logx(request):  # logout
    logout(request)
    state = 'You are logged out'
    return render_to_response('index.html', {'state': state},
                              context_instance=RequestContext(request))