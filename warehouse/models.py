from django.db import models
from django.db.models import Sum
from django.conf import settings
from django.urls import reverse
# Create your models here.

class Category(models.Model):
    name = models.CharField("Category Name",max_length=50)
    created = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
        verbose_name='ثبت شده توسط',null=True,on_delete=models.SET_NULL,
        related_name='categories')
    
    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
    def __str__(self) -> str:
        return f'{self.name}'
class Cluster(models.Model):
    name = models.CharField("Name",max_length=50)
    created = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
        verbose_name='ثبت شده توسط',null=True,on_delete=models.SET_NULL,
        related_name='clusters')
    
    class Meta:
        verbose_name = "Cluster"
        verbose_name_plural = "Clusters"
    def __str__(self) -> str:
        return f'{self.name}'
class PipeLine(models.Model):
    name = models.CharField("Name",max_length=50)
    created = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
        verbose_name='ثبت شده توسط',null=True,on_delete=models.SET_NULL,
        related_name='pipelines')
    
    class Meta:
        verbose_name = "Pipe Line"
        verbose_name_plural = "Pipe Lines"
    def __str__(self) -> str:
        return f'{self.name}'

class Item(models.Model):
    name = models.CharField("Item Description",max_length=10)
    created = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    class Meta:
        verbose_name = "کالا"
        verbose_name_plural = "کالا ها"
    def __str__(self) -> str:
        return f'{self.name}'

class Unit(models.Model):
    name = models.CharField("Unit Name",max_length=10)
    abrv = models.CharField("Abriviation",max_length=10)
    created = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
        verbose_name='Created By',null=True,on_delete=models.SET_NULL,
        related_name='units')
    class Meta:
        verbose_name = "واحد"
        verbose_name_plural = "واحد ها"
    def __str__(self) -> str:
        return f'{self.abrv}'
    def save(self,*args,**kwargs):
        self.abrv = str(self.abrv).upper()
        super().save(*args, **kwargs)
    def get_edit_url(self):
        return reverse('unit_edit',kwargs={'id':self.id})

class WarehouseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related('created_by')

class Warehouse(models.Model):
    name = models.CharField("Name",max_length=40)
    address = models.TextField("Address",blank=True,null=True)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL,verbose_name='Warehouse Keepers',blank=True,limit_choices_to={'warehouse_keeper':True},related_name='whs')
    created = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
        verbose_name='Created By',null=True,on_delete=models.SET_NULL,
        related_name='warehouses')
    
    objects = WarehouseManager()
    class Meta:
        verbose_name = "انبار"
        verbose_name_plural = "انبارها"
    def __str__(self) -> str:
        return self.name
    def get_edit_url(self):
        return reverse('warehouse_edit',kwargs={'id':self.id})

class Project(models.Model):
    name = models.CharField("Project Name",max_length=40)
    number = models.CharField("Project Number",max_length=40)
    created = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
        verbose_name='Created By',null=True,on_delete=models.SET_NULL,
        related_name='projects')
    
    objects = WarehouseManager()
    class Meta:
        verbose_name = "پروژه"
        verbose_name_plural = "پروژه ها"
    def __str__(self) -> str:
        return self.name
    def get_edit_url(self):
        return reverse('project_edit',kwargs={'id':self.id}) #TODO

class MrNumberManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related('created_by','project')

class MrNumber(models.Model):
    project = models.ForeignKey(Project,verbose_name='Project',on_delete=models.CASCADE,related_name='mr_numbers')
    number = models.CharField("MR Number",max_length=40)
    created = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
        verbose_name='Created By',null=True,on_delete=models.SET_NULL,
        related_name='mr_numbers')
    
    objects = MrNumberManager()
    class Meta:
        verbose_name = "شماره MR"
        verbose_name_plural = "شماره های MR"
    def __str__(self) -> str:
        return self.number
    def get_edit_url(self):
        return reverse('mr_number_edit',kwargs={'id':self.id}) #TODO


# class MaterialRequisitionManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().select_related('created_by','project','category')

# class MaterialRequisition(models.Model):
#     number = models.CharField('MR Number',max_length=200)
#     date = models.DateField('Approved Date',blank=True)
#     project = models.ForeignKey(Project,verbose_name='Project',null=True,blank=True,
#         on_delete=models.SET_NULL,related_name='mr')
#     created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
#         verbose_name='ثبت شده توسط',null=True,on_delete=models.SET_NULL,
#         related_name='mr')
#     category = models.ForeignKey(Category,verbose_name='category',related_name='mr',blank=True,null=True,on_delete=models.SET_NULL)
#     created = models.DateTimeField(auto_now=False,auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True,auto_now_add=False)
#     objects = MaterialRequisitionManager()
#     class Meta:
#         verbose_name = "درخواست مواد"
#         verbose_name_plural = "درخواست های مواد"
#         ordering = ['-created']
#     def __str__(self) -> str:
#         return self.number
#     def get_edit_url(self):
#         return reverse('mr_edit',kwargs={'id':self.id}) #TODO

# class MrItemManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().select_related('mr','unit','item','cluster','pipeline')
# class MrItem(models.Model):
#     mr = models.ForeignKey(MaterialRequisition,related_name='items',on_delete=models.CASCADE)
#     number = models.PositiveIntegerField('Item Number')
#     tag_number = models.CharField('Size',max_length=200,blank=True)
#     item = models.ForeignKey(Item,related_name='mritems',on_delete=models.CASCADE,verbose_name='Item Description')
#     unit = models.ForeignKey(Unit,on_delete=models.SET_NULL,null=True,related_name='items',verbose_name='Unit')
#     quantity = models.DecimalField('Quantity',max_digits=10,decimal_places=3)
#     cluster = models.ForeignKey(Cluster,blank=True,null=True,on_delete=models.SET_NULL,verbose_name="cluster")
#     pipeline = models.ForeignKey(PipeLine,blank=True,null=True,on_delete=models.SET_NULL,verbose_name="pipe line")
#     created = models.DateTimeField(auto_now=False,auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True,auto_now_add=False)
#     objects = MrItemManager()
#     class Meta:
#         verbose_name = "قلم درخواست  مواد"
#         verbose_name_plural = "اقلام درخواست های مواد"
#     def __str__(self) -> str:
#         return self.item.name

class ProcurementOrderManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related('created_by','project')

class ProcurementOrder(models.Model):
    project = models.ForeignKey(Project,verbose_name='Project',null=True,blank=True,
        on_delete=models.SET_NULL,related_name='pos')
    number = models.CharField('PO Number',max_length=200)
    date = models.DateField('Date Confirmed',blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
        verbose_name='ثبت شده توسط',null=True,on_delete=models.SET_NULL,
        related_name='pos')
    company = models.CharField('Seller (Company Name)',max_length=100)
    created = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)

    objects = ProcurementOrderManager()
    class Meta:
        verbose_name = "سفارش خرید"
        verbose_name_plural = "سفارش های خرید"
        ordering = ['-created']
    def __str__(self) -> str:
        return self.number
    def get_edit_url(self):
        return reverse('po_edit',kwargs={'id':self.id})

class POItemManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related('po','unit','item','cluster','pipeline','mr_number')
class POItem(models.Model):
    po = models.ForeignKey(ProcurementOrder,related_name='items',on_delete=models.CASCADE)
    number = models.PositiveIntegerField('PO Item No.')
    item = models.ForeignKey(Item,related_name='poitems',on_delete=models.CASCADE,verbose_name='Item Description')
    unit = models.ForeignKey(Unit,on_delete=models.SET_NULL,null=True,related_name='poitems',verbose_name='Unit')
    quantity = models.DecimalField('Quantity',max_digits=10,decimal_places=3)
    cluster = models.ForeignKey(Cluster,blank=True,null=True,on_delete=models.SET_NULL,verbose_name="cluster",related_name='poitems')
    pipeline = models.ForeignKey(PipeLine,blank=True,null=True,on_delete=models.SET_NULL,verbose_name="pipe line",related_name='poitems')
    mr_number = models.ForeignKey(MrNumber,on_delete=models.SET_NULL,blank=True,null=True,verbose_name='MR Number',related_name='poitems')

    created = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    objects = POItemManager()
    class Meta:
        verbose_name = "قلم سفارش خرید"
        verbose_name_plural = "اقلام سفارش خرید"
    def __str__(self) -> str:
        return f'{self.number}. {self.item.name}, {self.unit}, {self.cluster or " "}, {self.pipeline or " "} : ({self.quantity})'

class PackingListManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related('project','po','created_by')
class PackingList(models.Model):
    project = models.ForeignKey(Project,verbose_name='Project',null=True,blank=True,
        on_delete=models.SET_NULL,related_name='pls')
    number = models.CharField('Packing List Number',max_length=200)
    po = models.ForeignKey(ProcurementOrder,related_name='pls',on_delete=models.CASCADE,verbose_name='PO Number')
    company = models.CharField('شرکت فروشنده کالا',max_length=100)
    date = models.DateField('Sent Date',blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
        verbose_name='ثبت شده توسط',null=True,on_delete=models.SET_NULL,
        related_name='pls')
    created = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    objects = PackingListManager()
    class Meta:
        verbose_name = "بارنامه"
        verbose_name_plural = "بارنامه ها"
        ordering = ['-created']
    def __str__(self) -> str:
        return self.number
    def get_edit_url(self):
        return reverse('pl_edit',kwargs={'id':self.id}) 
    
    def save(self,*args,**kwargs):
        self.company = self.po.company
        super().save(*args,**kwargs)
class PLItemManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related('pl','po_item')
class PLItem(models.Model):
    pl = models.ForeignKey(PackingList,related_name='items',on_delete=models.CASCADE)
    quantity = models.DecimalField('Quantity',max_digits=10,decimal_places=3)
    po_item = models.ForeignKey(POItem,on_delete=models.CASCADE,related_name='plitems',verbose_name='PO Item No.')
    created = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    
    objects = PLItemManager()
    class Meta:
        verbose_name = "قلم  بارنامه"
        verbose_name_plural = "اقلام بارنامه"
    def __str__(self) -> str:
        return f'{self.po_item.item.name}, {self.po_item.unit}, {self.po_item.cluster or " "}, {self.po_item.pipeline or " "} : {self.quantity}'
class Condition(models.Model):
    name = models.CharField('Condition',max_length=20)
    created = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
        verbose_name='ثبت شده توسط',null=True,on_delete=models.SET_NULL,
        related_name='conditions')
    class Meta:
        verbose_name = "Condition"
        verbose_name_plural = "Conditions"
        ordering = ['-created']
    def __str__(self) -> str:
        return self.name

class MRSManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related('project','mr','po','pl','created_by')
    
class MaterialReceiptSheet(models.Model):
    project = models.ForeignKey(Project,verbose_name='Project',null=True,blank=True,
        on_delete=models.SET_NULL,related_name='mrs')
    number = models.CharField('MRS Number',max_length=200)
    po = models.ForeignKey(ProcurementOrder,related_name='mrs',on_delete=models.CASCADE,verbose_name='PO Number')
    pl = models.ForeignKey(PackingList,related_name='mrs',on_delete=models.CASCADE,verbose_name='Packing List Number')
    warehouse = models.ForeignKey(Warehouse,related_name='mrs',on_delete=models.CASCADE,verbose_name='Warehouse')
    vendor = models.CharField('Vendor',max_length=100)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
        verbose_name='ثبت شده توسط',null=True,on_delete=models.SET_NULL,
        related_name='mrs')
    created = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    objects = PackingListManager()
    class Meta:
        verbose_name = "Material Receipt Sheet"
        verbose_name_plural = "Material Receipt Sheets"
        ordering = ['-created']
    def __str__(self) -> str:
        return self.number
    def get_edit_url(self):
        return reverse('mrs_edit',kwargs={'id':self.id}) #TODO

class MRSItemManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related('mrs','pl_item','condition','pl_item__po_item','pl_item__po_item__unit','pl_item__po_item__cluster','pl_item__po_item__pipeline')
class MRSItem(models.Model):
    mrs = models.ForeignKey(MaterialReceiptSheet,related_name='items',on_delete=models.CASCADE)
    pl_item = models.ForeignKey(PLItem,on_delete=models.CASCADE,verbose_name='PO Item Num',related_name='mrsitems')
    quantity = models.DecimalField('Quantity',max_digits=10,decimal_places=3)
    condition = models.ForeignKey(Condition,related_name='mrsitems',verbose_name='Condition',on_delete=models.CASCADE,default=1)
    loc = models.CharField('loc',max_length=10,null=True,blank=True)
    warehouse = models.ForeignKey(Warehouse,related_name='mrsitems',on_delete=models.CASCADE,verbose_name='Warehouse')

    created = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    objects = MRSItemManager()
    class Meta:
        verbose_name = "MRS Item"
        verbose_name_plural = "MRS Items"
    def __str__(self) -> str:
        
        # return "hi"
        return f'{self.pl_item.po_item.item.name}, {self.pl_item.po_item.unit}, {self.pl_item.po_item.cluster or " "}, {self.pl_item.po_item.pipeline or " "} : {self.quantity}, {self.condition}'
    def save(self,*args,**kwargs):
        if self._state.adding:
            self.warehouse = self.mrs.warehouse
        super().save(*args,**kwargs)
        iv,created = inventoryItem.objects.get_or_create(
            project = self.mrs.project,
            warehouse = self.warehouse,
            item = self.pl_item.po_item.item,
            condition=self.condition,
            unit = self.pl_item.po_item.unit,
            cluster = self.pl_item.po_item.cluster if self.pl_item.po_item.cluster else None,
            pipeline = self.pl_item.po_item.pipeline if self.pl_item.po_item.pipeline else None,
            )
        if created:
            iv.incoming = self.quantity
        else:
            iv.incoming = MRSItem.objects.filter(
                mrs__project=self.mrs.project,
                warehouse = self.warehouse,
                pl_item__po_item__item = self.pl_item.po_item.item,
                condition=self.condition,
                pl_item__po_item__unit = self.pl_item.po_item.unit,
                pl_item__po_item__cluster = self.pl_item.po_item.cluster if self.pl_item.po_item.cluster else None,
                pl_item__po_item__pipeline = self.pl_item.po_item.pipeline if self.pl_item.po_item.pipeline else None,
                ).aggregate(total=Sum('quantity'))['total']
        iv.mrs_items.add(self)
        iv.save()
    def delete(self):
        self.quantity = 0
        self.save()
        super().delete()
class InventoryItemManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related('project','warehouse','item','unit','condition','cluster','pipeline').prefetch_related('mrs_items','mir_items')

class inventoryItem(models.Model):
    project = models.ForeignKey(Project,verbose_name='Project',null=True,blank=True,
        on_delete=models.SET_NULL,related_name='ivitems')
    warehouse = models.ForeignKey(Warehouse,related_name='ivitems',on_delete=models.CASCADE,verbose_name='Warehouse')
    item = models.ForeignKey(Item,related_name='ivitems',on_delete=models.CASCADE,verbose_name='Item Description')
    condition = models.ForeignKey(Condition,related_name='ivitems',verbose_name='Condition',on_delete=models.CASCADE,default=1)
    cluster = models.ForeignKey(Cluster,blank=True,null=True,on_delete=models.SET_NULL,verbose_name="cluster",related_name='ivitems')
    pipeline = models.ForeignKey(PipeLine,blank=True,null=True,on_delete=models.SET_NULL,verbose_name="pipe line",related_name='ivitems')
    incoming = models.DecimalField('incoming',max_digits=10,decimal_places=3,default=0)
    outgoing = models.DecimalField('outgoing',max_digits=10,decimal_places=3,default=0)
    remaining = models.DecimalField('remaining',max_digits=10,decimal_places=3,default=0)
    unit = models.ForeignKey(Unit,blank=True,null=True,on_delete=models.SET_NULL,verbose_name="unit",related_name='ivitems')
    objects = InventoryItemManager()
    total_in_all_warehouse_project = models.DecimalField('total_in_all_warehouse_project',max_digits=10,decimal_places=3,default=0)
    total_in_all = models.DecimalField('total_in_all',max_digits=10,decimal_places=3,default=0)
    mrs_items= models.ManyToManyField(MRSItem,verbose_name='MRS Items')
    mir_items = models.ManyToManyField('MIRItem',verbose_name='MIR Items')

    created = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)

    class Meta:
        verbose_name = "inventory Item"
        verbose_name_plural = "inventory Item"
    def save(self,*args,**kwargs):
        self.remaining = self.incoming - self.outgoing
        super().save(*args,**kwargs)
        
        inventoryItem.objects.filter(item=self.item,project=self.project,condition=self.condition,unit=self.unit).update(
             total_in_all_warehouse_project=inventoryItem.objects.filter(item=self.item,project=self.project,condition=self.condition,unit=self.unit).aggregate(total=Sum('remaining'))['total'])
        inventoryItem.objects.filter(item=self.item,condition=self.condition).update(
             total_in_all=inventoryItem.objects.filter(item=self.item,condition=self.condition,unit=self.unit).aggregate(total=Sum('remaining'))['total'])
                
        
    def __str__(self) -> str:
        return self.item.name

class MIRManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related('project','warehouse','created_by','po','pl','mrs')

class MaterialIssueRequest(models.Model):
    project = models.ForeignKey(Project,verbose_name='Project',null=True,blank=True,
        on_delete=models.SET_NULL,related_name='mirs')
    number = models.CharField('MIR Number',max_length=200)
    po = models.ForeignKey(ProcurementOrder,related_name='mir',on_delete=models.CASCADE,verbose_name='PO Number')
    pl = models.ForeignKey(PackingList,related_name='mir',on_delete=models.CASCADE,verbose_name='Packing List Number')
    mrs = models.ForeignKey(MaterialReceiptSheet,related_name='mir',on_delete=models.CASCADE,verbose_name='MRS Num.')
    warehouse = models.ForeignKey(Warehouse,related_name='mirs',on_delete=models.CASCADE,verbose_name='Origin(From)')
    issue_date = models.DateField('Issue Date',blank=True)
    required_date = models.DateField('Required Date',blank=True)
    client_department = models.CharField("Client Department",max_length=100)
    sent_to_warehouse = models.BooleanField("sent to warehouse",default=False)
    sent_to_location = models.BooleanField("sent to location",default=False)
    location = models.CharField("Destination",max_length=100,blank=True)
    dest_warehouse = models.ForeignKey(Warehouse,related_name='mirs_dest',on_delete=models.CASCADE,verbose_name='Destination(To)',blank=True,null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
        verbose_name='ثبت شده توسط',null=True,on_delete=models.SET_NULL,
        related_name='mirs')
    created = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    transfer = models.BooleanField('Transfered',default=False)
    objects = MIRManager()
    class Meta:
        verbose_name = "Material Issue Request"
        verbose_name_plural = "Material Issue Requests"
        ordering = ['-created']
    def __str__(self) -> str:
        return self.number
    def get_edit_url(self):
        return reverse('mir_edit',kwargs={'id':self.id}) 
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        if self.sent_to_location:
            items = self.items.all()
            for item in items:
                iv,created = inventoryItem.objects.get_or_create(
                    project = self.project,
                    warehouse = self.warehouse,
                    item = item.mrs_item.pl_item.po_item.item,
                    condition=item.mrs_item.condition,
                    unit = item.mrs_item.pl_item.po_item.unit,
                    cluster = item.mrs_item.pl_item.po_item.cluster if item.mrs_item.pl_item.po_item.cluster else None,
                    pipeline = item.mrs_item.pl_item.po_item.pipeline if item.mrs_item.pl_item.po_item.pipeline else None,
                )
                iv.outgoing = MIRItem.objects.filter(mir__project=self.project,
                                                 mir__warehouse = self.warehouse,
                                                 mrs_item = item.mrs_item,
                                                 cluster=item.cluster,
                                                 pipeline=item.pipeline
                                                 ).aggregate(total=Sum('quantity'))['total']
                iv.mir_items.add(item)
                iv.save()
                
                
                

class MIRItemManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related('mir','mrs_item','cluster','pipeline','mrs_item__mrs__pl','mrs_item__mrs__pl__po')
class MIRItem(models.Model):
    mir = models.ForeignKey(MaterialIssueRequest,related_name='items',on_delete=models.CASCADE)
    # pl_item = models.ForeignKey(PLItem,on_delete=models.CASCADE,verbose_name='PO Item Num',related_name='miritems')
    mrs_item = models.ForeignKey(MRSItem,on_delete=models.CASCADE,verbose_name='PO Item Num',related_name='miritems')
    quantity = models.DecimalField('Quantity',max_digits=10,decimal_places=3)
    remarks = models.CharField('remakrs',max_length=200,null=True,blank=True)
    cluster = models.ForeignKey(Cluster,blank=True,null=True,on_delete=models.SET_NULL,verbose_name="cluster",related_name='miritems')
    pipeline = models.ForeignKey(PipeLine,blank=True,null=True,on_delete=models.SET_NULL,verbose_name="pipe line",related_name='miritems')
    created = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    objects = MIRItemManager()
    class Meta:
        verbose_name = "MIR Item"
        verbose_name_plural = "MIR Items"
    def __str__(self) -> str:
        return f'{self.mrs_item}'
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
