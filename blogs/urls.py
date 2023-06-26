from . import views
from blogs import views
from django.shortcuts import render
from .views import search_view,latest_jobs,demo_templates
from django.urls import path, re_path
from django.conf.urls import handler404
from blogs.views import (
    homepage, PostDetail, AboutUsView, contactUsView,page_not_found_view#, PostList
)

def page_not_found_view(request, exception=None):
    return render(request, '404.html', status=404)


urlpatterns = [

  
    path('', homepage, name='home'),
    path('post/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('about/', AboutUsView.as_view(), name='about'),
    path('contact/', contactUsView.as_view(), name='contact'),
    path('search/', search_view, name='search'),
    path('latest-jobs/', latest_jobs, name='latest_jobs'),
    path('demo-templates/', demo_templates, name='demo_templates')
]

handler404 = page_not_found_view

# Catch-all pattern for undefined URLs
urlpatterns += [
    re_path(r'^.*$', page_not_found_view),
]
from blogs import views
from django.urls import path
from django.conf.urls import handler404
from blogs.views import homepage, PostDetail, AboutUsView, contactUsView

# urlpatterns = [
#     path('', homepage, name='home'),
#     path('post/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
#     path('about/', AboutUsView.as_view(), name='about'),
#     path('contact/', contactUsView.as_view(), name='contact'),
#     path('search/', search_view, name='search'),
#     path('latest-jobs/', latest_jobs, name='latest_jobs'),
#     path('<path:undefined>/', views.page_not_found_view, name='page_not_found'),
# ]


