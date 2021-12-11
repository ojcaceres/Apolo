from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("PlanAnual", api.PlanAnualViewSet)
router.register("Base", api.BaseViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("paa/PlanAnual/", views.PlanAnualListView.as_view(), name="paa_PlanAnual_list"),
    path("paa/PlanAnual/create/", views.PlanAnualCreateView.as_view(), name="paa_PlanAnual_create"),
    path("paa/PlanAnual/detail/<int:pk>/", views.PlanAnualDetailView.as_view(), name="paa_PlanAnual_detail"),
    path("paa/PlanAnual/update/<int:pk>/", views.PlanAnualUpdateView.as_view(), name="paa_PlanAnual_update"),
    path("paa/Base/", views.BaseListView.as_view(), name="paa_Base_list"),
    path("paa/Base/create/", views.BaseCreateView.as_view(), name="paa_Base_create"),
    path("paa/Base/detail/<int:pk>/", views.BaseDetailView.as_view(), name="paa_Base_detail"),
    path("paa/Base/update/<int:pk>/", views.BaseUpdateView.as_view(), name="paa_Base_update"),
)
