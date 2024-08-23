from django.urls import path
from shorts import views

urlpatterns = [
    path('shorts/create/',
         views.create_short.as_view(),
         name='create_short'),
    path('shorts/<int:short_id>/like/',
         views.like_short.as_view(),
         name='like_short'),
    path('shorts/<int:short_id>/comment/',
         views.comment_on_short.as_view(),
         name='comment_on_short'),
    path('shorts/<int:short_id>/share/',
         views.share_short.as_view(),
         name='share_short'),
]