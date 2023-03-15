from django.shortcuts import render
from django.views import generic
from oscar.core.loading import get_model

# Create your views here.
EmarketHub = get_model('emarketinghub', 'EmarketingHub')

class EmarketingHubListView(generic.ListView):
	model = EmarketHub
	template_name = 'emarketinghub/emarketinghub_list.html'
	context_object_name = 'emarketinghub_list'

class EmarketingHubDetailView(generic.DetailView):
	model = EmarketHub
	template_name = 'emarketinghub/emarketinghub_details.html'
	context_object_name = 'emarketinghub'