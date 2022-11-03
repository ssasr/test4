from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
def hello_view(request):
    age=18
    my_dict={"name":"shiva",'age':age,"tr":age>=21}
    return render(request,"testapp/hello.html",my_dict)
