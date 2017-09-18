from django.contrib import admin
from .models import Details,News,Projects,Glorys,text_index,video_index,logo_index,pic_index

admin.site.register(Details)
admin.site.register(News)
admin.site.register(Projects)
admin.site.register(Glorys)
admin.site.register(text_index)
admin.site.register(video_index)
admin.site.register(logo_index)
admin.site.register(pic_index)
