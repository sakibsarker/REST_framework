from django.urls import path
from . import views
from rest_framework_simplejwt.views import(
    TokenObtainPairView,TokenRefreshView
)
urlpatterns = [
    path('',views.enpoint),
    path('advocates/',views.advocate_list,name='advocates'),
    path('advocates/<str:username>/',views.AdvocateDetails.as_view()),
    # path('advocates/<str:username>/',views.advocate_details)
    path('companis/',views.Companis_List,name='companis'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]