from django.contrib import admin
from .models import Text
from .models import Prayer
from .models import Knowledge
from .models import Healing
from .models import Marriage
from .models import Novels

# Register your models here.
admin.site.register(Text)
admin.site.register(Prayer)
admin.site.register(Knowledge)
admin.site.register(Healing)
admin.site.register(Marriage)
admin.site.register(Novels)
