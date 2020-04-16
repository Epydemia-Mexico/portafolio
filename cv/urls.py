from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from dashboard.views import Index, SkillsView, EducationView, WorkExperienceView

urlpatterns = [
    path('admin/', admin.site.urls),
    #  Siempre que usemos clases basadas en vista debemos utilizar el método .as_view() de la clase.
    path('', Index.as_view()),
    path('habilidades', SkillsView.as_view(), name='habilidades'),
    path('educacion', EducationView.as_view(), name='edu'),
    path('trabajos', WorkExperienceView.as_view(), name='works'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
