from django.urls import reverse_lazy
from .models import Student
from django.views.generic import ListView, CreateView, UpdateView

class StudentListView(ListView):
    model = Student

class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('mainpage:student-list')
    fields = ['name']

class StudentUpdateView(UpdateView):
    model = Student
    success_url = reverse_lazy('mainpage:student-list')
    fields = ['name']
