from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("question", views.question, name="question"),
    path("register", views.register, name="register"),
    path("logout", views.logout_request, name="log_out"),
    path("notes", views.notes, name="notes"),
    path("student_stats", views.student_stats, name="student_stats"),
    path("first", views.first, name="first"),
    path("second", views.second, name="second"),
    path("third", views.third, name="third"),
    path("fourth", views.fourth, name="fourth"),
    path("fifth", views.fifth, name="fifth")
]

