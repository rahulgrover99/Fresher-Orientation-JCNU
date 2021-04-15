"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from orientation.views import index, TaskViewSet, \
    ProjectMentorViewSet, UserViewSet, ProjectMenteeViewSet, MentorMenteeViewSet, get_mentees, get_users, get_projects

router = DefaultRouter()
router.register("tasks", TaskViewSet)
router.register("project_mentors", ProjectMentorViewSet)
router.register("users", UserViewSet)
router.register("project_mentees", ProjectMenteeViewSet)
router.register("mentor_mentees", MentorMenteeViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('openapi/', get_schema_view(
            title="Orientation-Django-App",
            description="API for all things …",
            version="1.0.0"
        ), name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),

    # path('project/', project),
    # path('user/', user),
    # path('create_project_mentor/', project_mentor),
    # path('create_project_mentee/', project_mentee),
    # path('create_mentor_mentee/', mentor_mentee),

    path('query_get_mentees/<mentor_id>', get_mentees),
    path('query_get_projects/<mentor_id>', get_projects),
    path('query_get_users/<project_id>', get_users)
]

urlpatterns += router.urls