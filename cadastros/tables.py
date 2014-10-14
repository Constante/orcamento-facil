import django_tables2 as tables
# from .models import Person
from .models import Produto
from django_tables2.utils import A

data = [
    {"name": "Bradley"},
    {"name": "Stevie"},
]


# class PersonTable(tables.Table):
#     class Meta:
#         model = Person
#         attrs = attrs = {"class": "paleblue"}

class ProdutoTable(tables.Table):
    # name = tables.Column(verbose_name="User")
    # edit = tables.LinkColumn('people_detail', args=[A('pk')])

    class Meta:
        model = Produto
        attrs = attrs = {"class": "paleblue"}
        sequence = ("title", "description", "price")
        exclude = ("id",)
        www = tables.URLColumn()

# table = ProdutoTable(Produto.objects.all())
# table.columns['title'].header
# u'Model Verbose Name'