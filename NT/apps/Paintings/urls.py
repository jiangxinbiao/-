
from django.conf.urls import url,include
from Paintings.views import PaintingView,CommentsView,Labelview,IndexView
from rest_framework import routers

"""全自动生成url"""
router = routers.DefaultRouter()
router.register(r'Painting',PaintingView)

urlpatterns = [
    url(r'^Comments/',CommentsView.as_view(),name='Comments'),
    url(r'^Labels/',Labelview.as_view(),name='Labels'),
    url(r'^Painting/$',PaintingView.as_view(),name='Painting'),
    # url(r'^(?P<version>[v1|v2]+)/',include(router.urls))
    url(r'^index/',IndexView.as_view(), name='index'),
]