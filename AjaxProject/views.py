from django.shortcuts import render
from .forms import PhotoForm
# let return a Json Response
from django.http import JsonResponse









def photo_add_view(request):
    template_name = 'AjaxProject/index.html'
    form = PhotoForm(request.POST or None, request.FILES or None)
    data ={} #data dictionary is going to be empty initialy if below is valid we can add something to it 
    if request.is_ajax():
        if form.is_valid():
            form.save()
            data['name'] = form.cleaned_data.get('name')
            data['status'] = 'ok'
            return JsonResponse(data)
    context = {'form': form}
    return render(request, template_name, context)
