from django.urls import path

from . import views

app_name = 'docs'
urlpatterns = [
    path('', views.list_docs, name='index'),
    path('<int:doc_id>', views.view_doc, name='view_doc'),
    path('<int:doc_id>/authors/', views.view_doc_authors, name='view_doc_authors')
]
