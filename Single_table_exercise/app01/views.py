from django.shortcuts import render,redirect,HttpResponse
from app01 import models
from django.forms import ModelForm

class UserInfoModelForm(ModelForm):
    class Meta:
        model=models.UserInfo
        fields='__all__'
from utils.pager import Pagination
def UserInfo(request):

    obj = models.UserInfo.objects.all()
    pager_obj = Pagination(request.GET.get('page', 1), len(obj), request.path_info,request.GET)
    obj=obj[pager_obj.start:pager_obj.end]
    html = pager_obj.page_html()
    return render(request, 'userinfo.html', {'obj': obj, "page_html": html})
def user_add(request):
   if request.method=="GET":
       form=UserInfoModelForm()
       return render(request,"user_add.html",{'form':form})
   else:
       form=UserInfoModelForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect("/userinfo/")
       else:
           return render(request, "user_add.html", {'form': form})
def user_edit(request,nid):
    obj_edit = models.UserInfo.objects.filter(id=nid).first()
    if not obj_edit:
        return HttpResponse('数据不存在')
    if request.method == "GET":
        form = UserInfoModelForm(instance=obj_edit)
        return render(request, "user_edit.html", {'form': form})
    else:
        form = UserInfoModelForm(data=request.POST,instance=obj_edit)
        if form.is_valid():
            form.save()
            return redirect("/userinfo/")
        else:
            return render(request, "user_edit.html", {'form': form})



