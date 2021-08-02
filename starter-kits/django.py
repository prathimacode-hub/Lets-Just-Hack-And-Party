
# For full reference of given code, visit:
# https://docs.djangoproject.com/en/3.2/intro/tutorial01/
    
# file structure

# polls/
#     __init__.py
#     admin.py
#     apps.py
#     migrations/
#         __init__.py
#     models.py
#     tests.py
#     urls.py
#     views.py

# polls/views.py
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# polls/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

# mysite.urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
