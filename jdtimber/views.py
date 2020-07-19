from django.shortcuts import render,redirect
from .models import InquiryModel
from .forms import InquiryForm

# Create your views here.
def index(request):
	return render(request,'index.html')

def product(request):
	return render(request,'product.html')

def contact(request):
	context = {
		"form":InquiryForm
	}
	return render(request,'contact.html',context)

def sendinjuiry(request):
	form = InquiryForm(request.POST)

	if form.is_valid():
		inquiry = InquiryModel(name= form.cleaned_data['name'],
			business= form.cleaned_data['business'],
			email= form.cleaned_data['email'],
			phone= form.cleaned_data['phone'],
			address= form.cleaned_data['address'],
			logs= form.cleaned_data['logs'],
			veneers= form.cleaned_data['veneers'],
			decking= form.cleaned_data['decking'],
			boards= form.cleaned_data['boards'],
			flooring= form.cleaned_data['flooring'],
			skirtings= form.cleaned_data['skirtings'],)

		inquiry.save()
	return redirect('index')