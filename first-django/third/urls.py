from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.list, name='list'),
    path('create/', views.create, name='restaurant-create'),
    path('update/', views.update, name='restaurant-update'),
    # path('detail/', views.detail, name='restaurant-detail'),
    # path('delete/', views.delete, name='restaurant-delete'),
    path('restaurant/<int:id>/delete/', views.delete, name='restaurant-delete'),
# 삭제 시 비밀번호 입


    path('review/list/', views.review_list, name='review-list'),
    path('restaurant/<int:id>/', views.detail, name='restaurant-detail'),  # detail 의 주소를 재정의
    path('restaurant/<int:restaurant_id>/review/create/', views.review_create, name='review-create'),
    path('restaurant/<int:restaurant_id>/review/delete/<int:review_id>', views.review_delete, name='review-delete'),
]
