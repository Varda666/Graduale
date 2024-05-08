from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from users.views import (UserRetrieveView, UserUpdateView,
                         UserCreateView, UserDestroyView, UserListView)

urlpatterns = [
    path('<int:pk>/', UserRetrieveView.as_view(), name='user_detail'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('create/', UserCreateView.as_view(), name='user_create'),
    path('delete/<int:pk>/', UserDestroyView.as_view(), name='user_delete'),
    path('busy/', UserListView.as_view(), name='busy_users_list'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify')
]


