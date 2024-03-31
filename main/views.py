from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage
from django.views.generic import DetailView, FormView, ListView
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import PostModel


def index(request):
    if request.user.is_authenticated:
        return render(request, 'index.html', {'user': request.user})
    else:
        return HttpResponseRedirect('/')
    
    
def header(request):
    template = loader.get_template("header.html")
    return HttpResponse(template.render({}, request))

def home(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render({}, request))

def footer(request):
    template = loader.get_template("footer.html")
    return HttpResponse(template.render({}, request))

def notfound(request):
    template = loader.get_template("notfound.html")
    return HttpResponse(template.render({}, request))

def notification(request):
    template = loader.get_template("notification.html")
    return HttpResponse(template.render({}, request))

def profile(request):
    template = loader.get_template("profile.html")
    return HttpResponse(template.render({}, request))

def search(request):
    template = loader.get_template("search.html")
    return HttpResponse(template.render({}, request))

def setting(request):
    template = loader.get_template("setting.html")
    return HttpResponse(template.render({}, request))

@xframe_options_exempt
def ok_to_load_in_a_frame(request):
    return HttpResponse("This page is safe to load in a frame on any site.")

def index(req):
    message = EmailMessage(
        subject='this is subject',
        body='this is body',
        to=['magacao741@gmail.com'],
    )
    message.send()
    return render(req, 'index.html')


def contactFn(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        email = req.POST.get('email')
        title = req.POST.get('title')
        message = req.POST.get('message')
        emailMessage = EmailMessage(
            subject='お問い合わせがありました',
            body='name: {0}\nemail: {1}\ntitle: {2}\nmessage: {3}'.format(
                name, email, title, message),
            to=['magacado741@gmail.com'],
        )
        emailMessage.send()
        return HttpResponseRedirect('/main/thanks/')
    return render(req, 'contactFn.html')


def thanks(req):
    return HttpResponse('thank you for your message')


class ContactView(FormView):
    template_name = 'contact.html'
    success_url = 'home.html'
    form_class = ContactForm

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']
        emailMessage = EmailMessage(
            subject='お問い合わせがありました',
            body='name: {0}\nemail: {1}\ntitle: {2}\nmessage: {3}'.format(
                name, email, title, message),
            to=['magacado741@gmail.com'],
        )
        emailMessage.send()
        return super().form_valid(form)

def memo_list(request):
    username = request.user.username
    user_memos = PostModel.objects.filter(title=username)
    return render(request, 'memo_list.html', {'memos': user_memos})

def delete_memo(request, memo_id):
    memo = PostModel.objects.get(pk=memo_id)
    memo.delete()
    return redirect('memo_list')
    
class ListClass(ListView):
    template_name = 'search.html'
    model = PostModel

class FormClass(CreateView):
    template_name = 'home.html'
    model = PostModel
    fields = ('title','memo')
    success_url = reverse_lazy('list')


    
