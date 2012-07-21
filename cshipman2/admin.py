from django.contrib import admin
from models import Vessel, Operation, Port, Voyage, Bunker, Vport, Income, Expense
from blog.models import Post

admin.site.register(Vessel)
admin.site.register(Post)
admin.site.register(Operation)
admin.site.register(Port)
admin.site.register(Vport)
admin.site.register(Voyage)
admin.site.register(Income)
admin.site.register(Expense)
admin.site.register(Bunker)