from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View
from .models import Archive
from .forms import UploadFileForm
from user.login_check import LoginRequiredMixin, login_required

# Create your views here.

# List archives
class TechArchivesListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        try:
            archive = Archive.objects.filter(classify='tech')[:1]
            type = archive[0].classify
        except:
            return render(request, 'user/404.html')

        context = {
            'techarchives': Archive.objects.filter(classify='tech'),
            'type': type
        }

        return render(request, 'archive/tech.html', context)

class ADMArchivesListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        try:
            archive = Archive.objects.filter(classify='ADM')[:1]
            type = archive[0].classify
        except:
            return render(request, 'user/404.html')

        context = {
            'ADMarchives': Archive.objects.filter(classify='ADM'),
            'type': type
        }
        return render(request, 'archive/ADM.html', context)


class GAArchivesListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        try:
            archive = Archive.objects.filter(classify='GA')[:1]
            type = archive[0].classify
        except:
            return render(request, 'user/404.html')

        context = {
            'GAarchives': Archive.objects.filter(classify='GA'),
            'type': type
        }
        return render(request, 'archive/GA.html', context)


# content
@login_required
def content(request):
    id = request.GET.get('id', -1)
    try:
        archive = Archive.objects.get(id=id)
        archive.read_count += 1
        archive.save()
    except ObjectDoesNotExist as e:
        print('This archive does not exist.')
    context = {
        'title': archive.title,
        'location': '/static/archives_store/' + archive.title + '.pdf',
    }
    print(context['location'])
    return render(request, 'archive/content.html', context)



# delete
@login_required
def delete(request):
    id = request.GET.get('id', -1)
    try:
        archive = Archive.objects.get(id=id)
        type = archive.classify
        archive.delete()
    except ObjectDoesNotExist as e:
        print('This archive does not exist.')
        return render(request, 'user/404.html')

    if type == "tech":
        return redirect('archive:TECH-archives')
    if type == "GA":
        return redirect('archive:GA-archives')
    if type == "ADM":
        return redirect('archive:ADM-archives')



# update
@login_required
def update_techarchive(request):
    id = request.GET.get('id', -1)

    context = {}

    return render(request, 'archive/update.html', context)



@login_required
def update_GAarchive(request):
    pass

@login_required
def update_ADMarchive(request):
    pass


@login_required
def modify(request):
    pass



# upload
@login_required
def upload(request):
    type = request.GET.get('type', '')

    context = {}
    context['type'] = type
    # add subclass here

    return render(request, 'archive/upload.html', context)


@login_required
def add(request):
    type = request.POST.get('archivetype')
    time = request.POST.get('archivecreatetime')
    title = request.POST.get('archivetitle')

    file = request.FILES['archivefile']

    handle_upload_file(file, str(file))

    Archive.objects.create(title=title, author=time, classify=type)

    if type == "tech":
        return redirect('archive:TECH-archives')
    if type == "GA":
        return redirect('archive:GA-archives')
    if type == "ADM":
        return redirect('archive:ADM-archives')


def handle_upload_file(file, filename):
    path = '/root/Archive_Management/static/archives_store/'
    with open(path+filename,'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)