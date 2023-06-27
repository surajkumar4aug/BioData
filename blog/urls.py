from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, LikeViewSet, UserViewSet,OtpViewset,item_list
#from django.contrib.auth import vie
from .views import SignInView, ProtectedView

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments',CommentViewSet)
router.register(r'likes', LikeViewSet)
router.register(r'users', UserViewSet)
router.register(r'otp', OtpViewset)
#router.register(r'auth',include('django.contrib.auth.urls'),basename='auth')

urlpatterns = [
    path('', include(router.urls)),
    path('auth',include('rest_framework.urls')),
    path('test',item_list,name='test'),
    path('api/signin/', SignInView.as_view(), name='signin'),
    path('api/protected/', ProtectedView.as_view(), name='protected'),
]