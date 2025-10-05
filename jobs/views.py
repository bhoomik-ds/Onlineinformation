from django.shortcuts import render, get_object_or_404
from .models import Job
from django.db import connection
from django.db.utils import OperationalError

def table_exists(name):
    return name in connection.introspection.table_names()

def home(request):
    jobs = Job.objects.order_by('-created_at')[:10]
    notifications = []

    if table_exists('notifications_notification'):
        try:
            from notifications.models import Notification
            notifications = Notification.objects.order_by('-created_at')[:5]
        except OperationalError:
            notifications = []

    return render(request, 'jobs/home.html', {
        'jobs': jobs,
        'notifications': notifications,
    })

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'jobs/job_detail.html', {'job': job})

def job_list(request):
    jobs = Job.objects.all().order_by('-created_at')
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def notification_list(request):
    notifications = []
    if table_exists('notifications_notification'):
        try:
            from notifications.models import Notification
            notifications = Notification.objects.order_by('-created_at')
        except OperationalError:
            notifications = []
    return render(request, 'jobs/notification_list.html', {'notifications': notifications})
