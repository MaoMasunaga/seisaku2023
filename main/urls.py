from django.urls import path
from main import views
from .views import FormClass, ListClass


urlpatterns = [
    path("", views.index, name="index"),
    path("home.html", FormClass.as_view(), name='form'),
    path("header.html", views.header, name="header"),
    path("footer.html", views.footer, name="footer"),
    path("notfound.html", views.notfound, name="notfound"),
    path("notification.html", views.notification, name="notification"),
    path("profile.html", views.profile, name="profile"),
    path("search.html", ListClass.as_view(), name='list'),
    path("setting.html", views.setting, name="setting"),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('contactFn/', views.contactFn, name='contactFn'),
    path('thanks/', views.thanks, name='thanks'),
    path('contact/home.html', views.home, name='home'),
    path('memo_list.html', views.memo_list, name='memo_list'),
    path('delete/<int:memo_id>/', views.delete_memo, name='delete_memo'),

]


