from django.shortcuts import render

# Create your views here.
def photo_list(request):
    return render(request, 'photos/photo_list.html')

def photo_detail(request, pk):
    return render(request, 'photos/photo_detail.html', {'pk': pk})