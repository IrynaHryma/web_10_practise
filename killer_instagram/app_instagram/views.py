from django.shortcuts import render



#Create your view here
def main(request):
    return render(request,"app_instagram/index.html",context={'title':'Web_10 IrynaHryme!'})


def upload(request):
    return render(request,"app_instagram/upload.html",context={'title':'Web_10 IrynaHryme!'})


def pictures(request):
    return render(request,"app_instagram/pictures.html", context={'title':'Web_10 IrynaHryme!'})
