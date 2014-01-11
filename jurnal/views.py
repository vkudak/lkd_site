from django.shortcuts import render_to_response
from jurnal.models import *
from django.template.context import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from lkd_site.settings import BASE_DIR, MEDIA_URL
import os


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
                             'count': count[year], })
        for month in sorted(mcount[year].iterkeys(), reverse=True):
            archive_data.append({'isyear': False,
                                 'yearmonth': '%d/%02d' % (year, month),
                                 'monthname': MONTH_NAMES[month],
                                 'count': mcount[year][month], })
    return archive_data


def index(request):
    if request.user.is_authenticated():
        return render_to_response('index.html', {'user': request.user})
    else:
        return render_to_response('index.html')


def handle_uploaded_file(f, full_path):
    path, m_file = os.path.split(full_path)
    m_dir = BASE_DIR+MEDIA_URL
    if not os.path.exists(m_dir + path):
        os.makedirs(m_dir + path)
    with open(m_dir + full_path, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


@login_required
def journal(request, year=None, month=None):
    if request.POST:
        #TODO ADD Post fields validation!!!
        obs_date = request.POST.get('obs_date')
        obs_time = request.POST.get('obs_time')
        obs_desc = request.POST.get('obs_decs')
        content = request.FILES['content'].name
        obs_type = request.POST.get('obs_type')
        o = Obs()
        date_time = datetime.strptime(obs_date + ' ' + obs_time, '%Y-%m-%d %H:%M')
        o.date = date_time
        o.description = obs_desc
        o.content = obs_date.replace('-', '/')+'/'+content
        # print o.content
        typ = ObsType.objects.all()
        t = typ.filter(name=obs_type)[0]
        # print t.name
        o.category = t
        o.user = request.user
        o.save()
        handle_uploaded_file(request.FILES['content'], str(o.content))
        obss = Obs.objects.all()
        return HttpResponseRedirect('journal.html', {'obss': obss, 'user': request.user})
    else:
        obss = Obs.objects.order_by('-date')
        if year is not None:
            obss = obss.filter(date__year=year)
            if month is not None:
                obss = obss.filter(date__month=int(month))

        ar_obs = Obs.objects.all()
        archive = create_archive_data(ar_obs)
        types = ObsType.objects.all()
        return render_to_response('journal.html',
                                  {'obss': obss, 'types': types, 'user': request.user, 'archive_counts': archive},
                                  context_instance=RequestContext(request))


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