from django.urls import path

from web.views.chart_view import Chart
from web.views.home_views import Home
from web.views.receipt_view import Receipt

app_name = 'conf'
urlpatterns = [
    path('', Home.as_view(), name='farhad'),
    path('receipt/', Receipt.as_view(), name='receipt'),
    path('chart/', Chart.as_view(), name='chart'),

]
