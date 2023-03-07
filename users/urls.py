from django.urls import path
from users.views import user_list, user_detail
from users.views import (
    ProfileListView,
    ProfileDetailView,
    ProfileCreateView,
    ProfileUpdateView,
    ProfileDeleteView,
)

urlpatterns = [
    path("users/", user_list, name="user-list"),
    path("users/<int:pk>/", user_detail, name="user-detail"),
    path("profiles/", ProfileListView.as_view(), name="profile_list"),
    path("profiles/create/", ProfileCreateView.as_view(), name="profile_create"),
    path("profiles/<int:pk>/", ProfileDetailView.as_view(), name="profile_detail"),
    path(
        "profiles/<int:pk>/update/", ProfileUpdateView.as_view(), name="profile_update"
    ),
    path(
        "profiles/<int:pk>/delete/", ProfileDeleteView.as_view(), name="profile_delete"
    ),
]
