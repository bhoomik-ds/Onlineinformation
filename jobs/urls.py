from django.urls import path
from . import views
from .views import job_list, notification_list

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/', views.job_detail, name='job_detail'),
    path('jobs/', job_list, name='job_list'),
    path('notifications/', notification_list, name='notification_list'),
]
def get_absolute_url(self):
        return reverse('job_detail', args=[str(self.pk)])

"""path('results/', result_list, name='result_list'),
 path('contact/', views.contact, name='contact'),"""