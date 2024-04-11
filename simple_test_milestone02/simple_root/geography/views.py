from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Area, Attraction
from django.urls import reverse_lazy

class geography_home(ListView):
    template_name = 'geography/home.html'
    queryset = Area.objects.all()
    context_object_name = 'areas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['attractions'] = Attraction.objects.all()
        return context
    
class AreaList(ListView):
    model = Area
    template_name = 'geography/area_list.html'

class AttractionList(ListView):
    model = Attraction
    template_name = 'geography/attraction_list.html'

class AreaUpdate(UpdateView):
    model = Area
    template_name = "geography/area_update_form.html"
    fields = ["area_name", "area_type", "image"]
    success_url = reverse_lazy('arealist')

class AreaDelete(DeleteView):
    model = Area
    template_name = "geography/area_delete_form.html"
    success_url = reverse_lazy("arealist")

class AreaCreate(CreateView):
    model = Area
    template_name = 'geography/area_create_form.html'
    fields = ["area_name", "area_type", "image"]
    success_url = reverse_lazy('arealist')

class AreaDetail(DetailView):
    model = Area
    template_name = 'geography/area_detail.html'

class AttractionUpdate(UpdateView):
    model = Attraction
    template_name = 'geography/attraction_update_form.html'
    fields = ['area', "attraction_name", "image"]
    success_url = reverse_lazy('attractionlist')

class AttractionDelete(DeleteView):
    model = Attraction
    template_name = 'geography/attraction_delete_form.html'
    success_url = reverse_lazy("attractionlist")

class AttractionCreate(CreateView):
    model = Attraction
    template_name = 'geography/attraction_create_form.html'
    fields = ['area', "attraction_name", "image"]
    success_url = reverse_lazy('attractionlist')

class AttractionDetail(DetailView):
    model = Attraction
    template_name = 'geography/attraction_detail.html'
