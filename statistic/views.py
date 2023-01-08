from typing import Any, Dict
from django.views.generic import TemplateView
import datetime
from main.models import PartUnit

class IndexPage(TemplateView):
    template_name = 'statistic/index.html'
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        queryset = PartUnit.objects.all()
        
        sales = {date: 0 for date in set(map(lambda item: str(item.sale_date.date()), queryset))}
        for el in queryset:
            sales[str(el.sale_date.date())] += el.sell_price
        margin = sum(map(lambda item: item.sell_price - item.buy_price, queryset))

        context['sale_date'] = list(sales.keys())
        context['sale_values'] = list(sales.values())
        context['margin'] = margin
        print(context)
        return context

class SalesView(TemplateView):
    template_name = 'statistic/sales.html'
    

class MarginView(TemplateView):
    template_name = 'statistic/margin.html'