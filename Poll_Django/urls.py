"""Poll_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import verify_jwt_token

from polls import api

router = DefaultRouter()
router.register('polls', api.PollAPIViewSet)
router.register('questions', api.QuestionAPIViewSet)
router.register('options', api.OptionAPIViewSet)
router.register('nestedPolls', api.NestedPollAPIViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('web-api/v1/', include(router.urls)),
    path('web-api/v1/token-auth/', obtain_jwt_token),
    path('web-api/v1/token-verify/', verify_jwt_token)
]
