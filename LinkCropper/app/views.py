from django.shortcuts import render, get_object_or_404, redirect
from .models import ReddirectAnonymous, ReddirectId, CounterFolder, ReddirectUser
from urllib.parse import urlparse
from django.urls import reverse
from django.http import HttpResponse
from .forms import BootstrapCreateLinkForm, BootstrapCreateNameLinkForm
from django.contrib.auth.decorators import login_required

def home(request):

    data = {
            'title':'Home Page',
            'form': BootstrapCreateLinkForm()
        }

    if request.user.is_authenticated:
        data['userForm'] = BootstrapCreateNameLinkForm()
        data['hostname'] = request.get_host()
        data['userlist'] = ReddirectUser.objects.filter(user=request.user)

    return render(
        request,
        'app/index.html',
        data
    )


def createNewLink(request):
    if request.method != "POST":
        return HttpResponse(404)

    url = request.POST.get("url")

    try:
        reddir = ReddirectAnonymous.objects.get(url=url)
        return render(
            request,
            'app/linkcreated.html',
            {
                'title':'Success',
                'link': request.build_absolute_uri(reverse('reddir', args=[reddir.id.folder, reddir.id.linkid]))
            }
        )

    except ReddirectAnonymous.DoesNotExist:
        folder = str(urlparse(url).hostname).split('.')[-2]

        id = ReddirectId(folder = folder)
        id.linkid = getNewIdFolder(folder)
        id.save()

        reddir = ReddirectAnonymous()
        reddir.id = id 
        reddir.url = url
        reddir.save()

        return render(
            request,
            'app/linkcreated.html',
            {
                'title':'Success',
                'link': request.build_absolute_uri(reverse('reddir', args=[folder, id.linkid]))
            }
        )


@login_required
def createNewNamedLink(request):
    if request.method != "POST":
        return HttpResponse(404)

    url = request.POST.get("url")
    name = request.POST.get("name")

    try:
        # TODO: Сделать вывод сообщения о существовании этого имени
        reddir = ReddirectUser.objects.get(name=name)
        return render(
            request,
            'app/linkcreated.html',
            {
                'title':'Success',
                'link': request.build_absolute_uri(reverse('reddir', args=[reddir.id.folder, reddir.id.linkid]))
            }
        )

    except ReddirectUser.DoesNotExist:

        reddir = ReddirectUser()
        reddir.url = url
        reddir.name = name
        reddir.user = request.user
        reddir.save()

        return render(
            request,
            'app/linkcreated.html',
            {
                'title':'Success',
                'link': request.build_absolute_uri(reverse('reddirName', args=[name,]))
            }
        )



def reddirectLink(request, folder:str, linkid:int):
    reddir = get_object_or_404(ReddirectAnonymous, id__folder=folder, id__linkid=linkid)
    
    return redirect(reddir.url)

def reddirectNameLink(request, name:str):
    reddir = get_object_or_404(ReddirectUser, name=name)
    return redirect(reddir.url)




def getNewIdFolder(folder:str):
       folderObj = CounterFolder.objects.get_or_create(folder=folder)[0]
       folderObj.count += 1
       folderObj.save()
       return folderObj.count