from django.conf.urls import url
from app2 import views

urlpatterns = [
    url(r'^questions/$', views.question_list),
    url(r'^questions/new/$', views.addQuestion),
    url(r'^greetings',views.Greeting.as_view()),

]