from django.urls import path

from .views import IndexView, WorksView, ContactView

urlpatterns = [
    path('', IndexView.as_view()),
    path('index.html', IndexView.as_view()),
    path('works.html', WorksView.as_view()),
    path('contact.html', ContactView.as_view()),
]