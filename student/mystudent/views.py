from django.shortcuts import render, redirect
from django.views.generic import DeleteView, UpdateView, ListView, DetailView, CreateView
from django.urls import reverse_lazy, reverse
from .forms import StudentForm
from .models import Student
# Create your views here.

class StudentCreateView(CreateView):
    form_class= StudentForm
    template_name= 'mystudent/studentform.html'
    def form_valid(self, form):
        # form= StudentForm
        name=form.cleaned_data['name']
        roll= form.cleaned_data['roll']
        email= form.cleaned_data['email']
        studentform= Student(
            name= name,
            roll= roll,
            email= email
        )
        studentform.save()
        return redirect('/')
    success_url= '/'


class StudentListView(ListView):
    model= Student
    template_name= 'mystudent/studentlist.html'
    context_object_name= 'students'
    

class StudentDetailView(DetailView):
    model= Student
    template_name= 'mystudent/studentdetail.html'

class StudentUpdateView(UpdateView):
    model= Student
    form_class= StudentForm
    template_name= 'mystudent/studentupdate.html'
    def get_success_url(self):
        return reverse('student-detail', kwargs={'pk': self.object.pk})
    
class StudentDeleteView(DeleteView):
    model= Student
    template_name= 'mystudent/delete.html'
    success_url= '/'
    