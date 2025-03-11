from django.shortcuts import render
from django.views.generic import TemplateView
from .models import EmployeeData
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
# Create your views here.

class HomePageView(TemplateView):
    template_name = "base.html"

class RecordListView(LoginRequiredMixin,ListView):
    model = EmployeeData
    template_name = "home.html"

class RecordDetailView(UserPassesTestMixin, DetailView):
    model = EmployeeData
    template_name = "record_detail.html"

    def test_func(self):
        record = self.get_object()
        return record.created_by == self.request.user
    

class RecordCreateView(LoginRequiredMixin,CreateView):
    model = EmployeeData
    template_name = "record_new.html"
    fields = ["first_name","last_name","email","phone","address","city","province","country"]

    def form_valid(self, form):
        form.instance.created_by = self.request.user  
        return super().form_valid(form)


class RecordUpdateView(UserPassesTestMixin,UpdateView):
    model = EmployeeData
    template_name = "record_edit.html"
    fields = ["first_name","last_name","email","phone","address","city","province","country"]

    def test_func(self):
        record = self.get_object()
        return record.created_by == self.request.user


class RecordDeleteView(UserPassesTestMixin,DeleteView):
    model = EmployeeData
    template_name = "record_delete.html"
    success_url = reverse_lazy("dashboard")

    def test_func(self):
        record = self.get_object()
        return record.created_by == self.request.user