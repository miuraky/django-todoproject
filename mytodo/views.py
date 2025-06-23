from django.shortcuts import render

# Create your views here.
from django.views import View # クラスベースビューを継承するのに必要
from .models import Task
from .form import TaskForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404



# Create your views here.
class IndexView(View):
    def get(self, request):
        # todoリストを取得
        todo_list = Task.objects.all().order_by('complete', 'start_date')
        context = {"todo_list": todo_list}

        # テンプレートをレンダリング
        return render(request, "mytodo/index.html", context)


# ビュークラスをインスタンス化
index = IndexView.as_view()


class AddView(View):
    def get(self, request):
        # テンプレートのレンダリング処理
        form  = TaskForm()  # 空のフォームを生成
        return render(request, "mytodo/add.html", {'form': form})

    def post(self, request, *args, **kwargs):
        # 登録処理
        # 入力データをフォームに渡す
        form = TaskForm(request.POST)
        # 入力データに誤りがないかチェック
        is_valid = form.is_valid()

        # データが正常であれば
        if is_valid:
            # モデルに登録
            form.save()
            return redirect('/')

        # データが正常じゃない
        return render(request, 'mytodo/add.html', {'form': form})
        
add = AddView.as_view()

class Update_task_complete(View):
    def post(self, request, *args, **kwargs):
        task_id = request.POST.get('task_id')

        task = Task.objects.get(id=task_id)
        task.complete = not task.complete
        task.save()

        return redirect('/')
    
update_task_complete = Update_task_complete.as_view()

class EditView(View):
    def get(self, request, task_id):
        task = Task.objects.get(id=task_id)
        form = TaskForm(instance=task)
        return render(request, 'mytodo/edit.html', {'form': form})

    def post(self, request, task_id):
        task = Task.objects.get(id=task_id)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'mytodo/edit.html', {'form': form})

edit = EditView.as_view()

class DeleteConfirmView(View):
    def get(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        form = TaskForm(instance=task) 
        return render(request, 'mytodo/delete.html', {'task': task, 'form': form})
    

class DeleteView(View):
    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return redirect('index')
    


