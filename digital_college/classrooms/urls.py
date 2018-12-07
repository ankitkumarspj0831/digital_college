from django.urls import path, include
from . import views
from after_login import views as login_view

app_name = 'classroom'

urlpatterns = [
    path('', login_view.after_login, name='after_login'),
    path('<str:class_name>/', views.class_home, name='class_home'),
    path('<str:class_name>/quiz/', include('quiz.urls', namespace='quiz')),
    # path('<str:class_name>/assignment',include('assignment.urls')),
    path('<str:class_name>/slides/', include('slides.urls', namespace='slides')),
    path('<str:class_name>/forum/', include('forum.urls', namespace='class_forum')),
    path('<str:class_name>/members/', views.members, name="members"),
    # path('<str:class_name>/report',include('report.urls')),
]
