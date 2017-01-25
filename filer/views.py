import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from filer.models import FileLog


@login_required
def home(request):
    user = request.user
    today = datetime.datetime.now()
    files = list(FileLog.objects.filter(start_datetime__day=today.day).order_by('start_datetime'))
    current_time = datetime.timedelta(0)

    day_finished = True
    if files:
        if not files[-1].finish_datetime:
            current_time = today - files[-1].start_datetime
            day_finished = False

    log_times = [filer.finish_datetime-filer.start_datetime for filer in files if filer.finish_datetime]

    for log_time in log_times:
        current_time += log_time

    current_time = str(current_time).split(':')
    current_hours = current_time[0]
    current_minutes = current_time[1]
    return render(request, 'home.html', locals())
