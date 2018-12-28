from django.urls import path
from .views import PasteCreate, PasteDetail, PasteList, PasteDelete, PasteUpdate

urlpatterns = [
    path(r'', PasteCreate.as_view(), name='create'),
    path(r'paste/<int:pk>', PasteDetail.as_view(), name='pastebin_paste_detail'),
    path(r'pastes/', PasteList.as_view(), name='pastebin_paste_list'),
    path(r'paste/delete/<int:pk>', PasteDelete.as_view(), name='pastebin_paste_delete'),
    path(r'paste/edit/<int:pk>', PasteUpdate.as_view(), name='pastebin_paste_edit'),
]
# url is '' which will be matched with the incoming request and forwarded to the corresponding view
# view is PasteCreate.as_view()
# the scope goes into views.py