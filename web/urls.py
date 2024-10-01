from django.urls import path

from web.views import Home

app_name = 'conf'
urlpatterns = [
    path('', Home.as_view(), name='farhad'),

]
