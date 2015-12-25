from django.shortcuts import render,render_to_response
from django.http import  HttpResponse,Http404,HttpResponseRedirect
import datetime
from django.core.mail import  send_mail
from mysite.forms import ContactForm
from django.contrib import auth
from books.models import Book
# Create your views here.
def hello(request):
    return render(request, 'hello.html')
def current_datetime(request):
    current_date = datetime.datetime.now()
    return render(request, 'curent_datetime.html',locals())
def hours_ahead(request,offset):
    try:
        hour_offset=int(offset)
    except ValueError:
        raise Http404()
    next_time=datetime.datetime.now()+ datetime.timedelta(hours = hour_offset)
    return render(request, 'hours_ahead.html',locals())

def search(request):
    errors=[]
    if 'q' in request.GET :
        q=request.GET['q']
        if not q:
            errors.append('Input search request.')
        elif len(q)>20:
            errors.append('Input not more 20 symbols.')
        else:
            books=Book.objects.filter(title__icontains=q)
            return render(request,'search_result.html',{'books': books, 'query': q})

    return render(request,'search_form.html', {'errors': errors})
def contact(request):
    errors=[]
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            send_mail(
            cd['subject'],
            cd['message'],
            cd.get('email', 'noreply@example.com'),
            ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form=ContactForm(initial={'subject':'I like your site'})

    return render(request, 'contact_form.html',{'form': form})

