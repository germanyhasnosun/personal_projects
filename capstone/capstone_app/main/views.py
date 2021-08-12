from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from main.models import meta_data
from django.core import serializers
from main.forms import ImageForm
from django.db.models import Avg 
import json
from main.cancer_screening.cancer_screening import analyze_photo
from django.contrib.auth.decorators import login_required

# Create your views here.

def homepage(request):
    template = "homepage/homepage.html"
    content = {}

    return render(request, template, content)

@login_required(login_url='/user/login')
def risk_group(request):
    template = "risk_group/risk_group.html"
    content = {}

    return render(request, template, content)


def get_risk_data(request, data_type):
    content = {}
    if data_type == 'age':
        data = meta_data.objects.values('age_integer').annotate(result=Avg('outcome_integer')).order_by('age_integer')
        labels = []
        values = []
        for i in data:
            labels.append(i['age_integer'])
            values.append(round(i['result'] * 100,2) )
        content['labels'] = labels
        content['values'] = values
    
    elif data_type == 'gender':
        data = meta_data.objects.values('sex_integer').annotate(result=Avg('outcome_integer')).order_by('sex_integer')
        labels = []
        values = []
        for i in data:
            if i['sex_integer'] == 0:
                labels.append('Female')
            elif i['sex_integer'] == 1:
                labels.append('Male')
            else:
                labels.append('Unkown')
            values.append(round(i['result'] * 100,2) )
        content['labels'] = labels
        content['values'] = values   

    elif data_type == 'location':
        data = meta_data.objects.values('location').annotate(result=Avg('outcome_integer')).order_by('location')
        labels = []
        values = []
        for i in data:
            labels.append(i['location'])
            values.append(round(i['result'] * 100,2) )
        content['labels'] = labels
        content['values'] = values  

        print(content)

    return HttpResponse(json.dumps(content))


def about_us(request):
    template = "about_us/about_us.html"
    content = {}

    return render(request, template, content)

@login_required(login_url='/user/login')
def cancer_screening(request):
    template = "cancer_screening/cancer_screening.html"
    content = {}
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance

            photo_outcome = analyze_photo(img_obj)
            content['result'] = photo_outcome
            content['form'] = form
            content['img_obj'] = img_obj



            return render(request, template, content)

    else:
        form = ImageForm()
        content['form'] = form

    return render(request, template, content)