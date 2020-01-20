from django.urls import path

from . import views

app_name='polls'

urlpatterns = [
    path("berkinkalbi",views.berkinkalbi,name="berk"),
    path("anasayfa", views.anasayfa, name="anasayfa"),
    path("urunlerimiz", views.urunlerimiz, name="ezgi"),
    path("iletisim", views.iletisim, name="iletisim"),
    path("test", views.test, name="test"),
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]