from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import MyLogoutView

urlpatterns = [
    path('', views.main, name='main'),
    path('post/<int:id>', views.post, name='post'),
    path('contacts', views.contacts, name='contacts'),
    path('about us', views.about_us, name='about us'),
    path('category/<str:c>', views.category, name='cats'),
    path('search', views.search, name='search'),
    path('create', views.create, name='create'),
    path('comments/<int:post_id>', views.comment_and_post_details, name='comments'),
    path('newsletter', views.newsletter, name='newsletter'),
    path('login', LoginView.as_view(), name='blog_login'),
    # path('logout', LogoutView.as_view(), name='blog_logout'),
    path('logout', MyLogoutView.as_view(), name='blog_logout'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('registration', views.registration, name='registration'),
    path('profile/update', views.update_profile, name='update_profile'),
]