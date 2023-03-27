from django.urls import path
from users.views import user_list, user_detail
from users.views import create_profile, update_profile, delete_profile
from users.views import UserList

urlpatterns = [
    path("users/", user_list, name="user-list"),
    path("users/<int:pk>/", user_detail, name="user-detail"),
    path("profile/", create_profile, name="create_profile"),
    path("profile/<int:pk>/", update_profile, name="update_profile"),
    path("profile/<int:pk>/", delete_profile, name="delete_profile"),
    path("users/list/", UserList.as_view()),
]
