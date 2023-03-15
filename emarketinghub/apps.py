from oscar.core.application import OscarConfig
from django.urls import path, re_path
from oscar.core.loading import get_class


class EmarketingHubConfig(OscarConfig):
    # default_auto_field = 'django.db.models.BigAutoField'
    name = 'emarketinghub'
    namespace = 'emarketinghub'

    def ready(self):
        super().ready()
        self.emarket_list_view = get_class('emarketinghub.views', 'EmarketingHubListView')
        self.emarket_detail_view = get_class('emarketinghub.views', 'EmarketingHubDetailView')

    def get_urls(self):
        urls = super().get_urls()
        urls += [
            path('', self.emarket_list_view.as_view(), name='index'),
            re_path(r'^view/(?P<pk>\d+)/$', self.emarket_detail_view.as_view(), name='details')
        ]
        return self.post_process_urls(urls)
