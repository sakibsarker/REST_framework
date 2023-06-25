from django.urls import path
from . import views
urlpatterns = [
    path('',views.enpoint),
    path('advocates/',views.advocate_list,name='advocates'),
    path('advocates/<str:username>/',views.AdvocateDetails.as_view()),
    # path('advocates/<str:username>/',views.advocate_details)
    path('companis/',views.Companis_List,name='companis'),

]