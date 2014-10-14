import django_tables2 as tables
# from .models import Person
from .models import Produto
from django_tables2.utils import A
from django.utils.safestring import mark_safe
from django.utils.html import escape

data = [
    {"name": "Bradley"},
    {"name": "Stevie"},
]


# class PersonTable(tables.Table):
#     class Meta:
#         model = Person
#         attrs = attrs = {"class": "paleblue"}
class MyColumn(tables.Column): 
    empty_values = list('www.google.com') 
    def render(self, value, record): 
        return mark_safe('<button id="%s" class="btn btn-info">Submit</button>' % escape(record.id))

class ProdutoTable(tables.Table):
    # name = tables.Column(verbose_name="User")
    # edit = tables.LinkColumn('people_detail', args=[A('pk')])
    submit = MyColumn()
    class Meta:
        model = Produto
        attrs = attrs = {"class": "paleblue"}
        sequence = ("title", "description", "price")
        exclude = ("id",)
        www = tables.URLColumn()

# table = ProdutoTable(Produto.objects.all())
# table.columns['title'].header
# u'Model Verbose Name'