#入力フォームに入力した内容を登録するためフォームを受け取れるようにしておく
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo_bord

# Create your views here.

def myapp_index(request):
    #HTMLのフォームアクションgetで指定したinput name="words"を取得
    msg =  request.GET.get('words')

    #データベースからデータを削除する
    delete_text = request.POST.getlist('delete_text')

    if delete_text:
        Todo_bord.objects.all().delete()

    #このurlに来た時に自動で送られてしまうので分岐
    if msg is None:
        data_list = Todo_bord.objects.order_by('-id')
        contexts = {
            'result_list': data_list,
        }
        return render(request,'myapp/index.html',contexts)

    else:
        #画像ファイル
        image_file = request.FILES.get('files')
        #データベースの読み出し　データベースに変数msgを保存している
        message_data = Todo_bord()
        message_data.new_message = msg
        message_data.image_url = image_file
        message_data.save()
        data_list = Todo_bord.objects.order_by('-id')
        contexts = {
            'result_list':data_list,
        }

        return render(request,'myapp/index.html',contexts)
