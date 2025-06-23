from django.urls import path
from mytodo import views as mytodo
from mytodo.views import DeleteConfirmView, DeleteView


urlpatterns = [
    path("", mytodo.index,name="index"),
    path("add/", mytodo.add,name="add"),
    path("update_task_complete/", mytodo.update_task_complete, name="update_task_complete"),
    path('edit/<int:task_id>/', mytodo.edit, name='edit'),
    # 削除確認ページ
    path('delete_confirm/<int:task_id>/', DeleteConfirmView.as_view(), name='delete_confirm'),
    # 削除実行用POST
    path('delete/<int:task_id>/', DeleteView.as_view(), name='delete'),
]