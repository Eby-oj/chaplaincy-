from django.shortcuts import render
from .models import Text
from .models import Prayer
from .models import Knowledge
from .models import Healing
from .models import Marriage
from .models import Novels


#create views here

def text(request):
	book = Text.objects.all()
	return render(request, 'text.html',context={'book':book})


def prayer(request):
	book = Prayer.objects.all()
	return render(request, 'prayer.html',context={'book': book})

def knowledge(request):
	book = Knowledge.objects.all()
	return render(request, 'knowledge.html',context={'book':book})

def searchbar(request):
	print('wcqc')
	book = Text.objects.filter(title=request.GET['search'])
	book = Prayer.objects.filter(title=request.GET['search'])
	book = Knowledge.objects.filter(title = request.GET['search'] )
	book = Healing.objects.filter(title=request.GET['search'])
	book = Marriage.objects.filter(title=request.GET['search'])
	book = Novels.objects.filter(title=request.GET['search'])
	return render(request, 'searchbar.html',context={'book':book})

def healing(request):
	book = Healing.objects.all()
	return render(request, 'healing.html',context={'book':book})

def marriage(request):
	book = Marriage.objects.all()
	return render(request, 'marriage.html',context={'book':book})

def novels(request):
	book = Novels.objects.all()
	return render(request, 'novels.html',context={'book':book})

# def download(request, path):
	# filename = 'ExcelTemplate.xslx'
	# file_path = os.path.join(settings.MEDIA_ROOT, path)
	# if os.path.exists(file_path):
	# with open(file_path, 'rb') as fh:
	# response = HttpResponse(fh.read(), content_type=(
	# 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet/adminupload'))
	# response['Content-Disposition'] = "attachment; filename=%s" % filename
	# return response
	# raise Http404