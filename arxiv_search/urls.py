from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_results, name='search_results'),
    re_path(r'^paper/(?P<paper_id>[\w.-]+)/$', views.paper_summary, name='paper_summary'),
    re_path(r'^pdf/(?P<paper_id>[\w.-]+)/$', views.pdf_viewer, name='pdf_viewer'),
    re_path(r'^wordcloud/(?P<paper_id>[\w.-]+)/$', views.generate_wordcloud, name='generate_wordcloud'),
    re_path(r'^knowledge-graph/(?P<paper_id>[\w.-]+)/$', views.generate_knowledge_graph, name='generate_knowledge_graph'),
    path('chat/', views.chat, name='chat'),
]