import warehouse
from django.contrib import admin

from .models import (Item,Unit,Warehouse,
                     ProcurementOrder,POItem,
                    #  MrItem,MaterialRequisition,
                     inventoryItem,MRSItem,
                    #  MaterialIssueRequest,MaterialReceiptSheet
                    PackingList,PLItem
)
# Register your models here.
admin.site.register(Item)
admin.site.register(Unit)
admin.site.register(Warehouse)
admin.site.register(ProcurementOrder)
admin.site.register(POItem)

admin.site.register(MRSItem)
# admin.site.register(MaterialRequisition)
# admin.site.register(MaterialIssueRequest)
# admin.site.register(MaterialReceiptSheet)
admin.site.register(PackingList)
admin.site.register(PLItem)
@admin.register(inventoryItem)
class inventoryAdmin(admin.ModelAdmin):
    list_display = ['item','project','warehouse','incoming','outgoing','remaining','total_in_all_warehouse_project','total_in_all']
    list_display_links = ['item','project','warehouse','incoming','outgoing','remaining']
    