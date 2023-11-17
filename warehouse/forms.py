from django import forms
from .models import (Item,Warehouse,Unit,Project,
                    #  MaterialRequisition,MrItem,
                    POItem,ProcurementOrder,
                    PackingList,PLItem,
                    MaterialReceiptSheet,MRSItem,
                    Condition,
                    MaterialIssueRequest,MIRItem,
                    Category,Cluster,PipeLine,
                    MrNumber
    )
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
from django.forms import inlineformset_factory
from django.contrib.auth import get_user_model
class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = ['name','address','users']

class UnitForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields = ['name','abrv']
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name',]

class ClusterForm(forms.ModelForm):
    class Meta:
        model = Cluster
        fields = ['name',]
class PipeLineForm(forms.ModelForm):
    class Meta:
        model = PipeLine
        fields = ['name',]

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name','number']

class MrNumberForm(forms.ModelForm):
    class Meta:
        model = MrNumber
        fields = ['number','project']

class ProcurementOrderForm(forms.ModelForm):
    class Meta:
        model = ProcurementOrder
        fields = ['project','number','date','company',]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'] = JalaliDateField(label='PO Date', 
            widget=AdminJalaliDateWidget 
        )

class POItemForm(forms.ModelForm):
    class Mata:
        model = POItem
        fields = ['number','item','unit','quantity','pipeline','cluster','mr_number']
    def __init__(self, *args, **kwargs):
        units = kwargs.pop('units',None)
        pipes = kwargs.pop('pipes',None)
        clusters = kwargs.pop('clusters',None)
        po = kwargs.pop('po',None)
        # print(items)
        super().__init__(*args, **kwargs)
        if units:
            item_choices = [("","---------")]
            unit_choices = [("","--------")]+[(item.id, item.__str__()) for item in units]
            pipe_choices = [("","--------")]+[(item.id, item.__str__()) for item in pipes]
            cluster_choices = [("","--------")]+[(item.id, item.__str__()) for item in clusters]
            self.fields['unit'].choices = unit_choices
            self.fields['item'].choices = item_choices
            self.fields['cluster'].choices = cluster_choices
            self.fields['pipeline'].choices = pipe_choices
        if po:
            self.fields['mr_number'].queryset = self.fields['mr_number'].queryset.filter(project=po.project)
        if self.instance.pk:
            item_choices = [(self.instance.item.id,self.instance.item.name)]
            self.fields['item'].choices = item_choices
        
        # if self.instance.pk:
        #     mritems = self.instance.po.mr.items.all().values_list('id','number')
        #     self.fields['number'].widget = forms.Select(choices=mritems)
        #     # self.fields['number'].choices = mritems
        # else:
        #     self.fields['number'].widget = forms.Select()


POItemFromSet = inlineformset_factory(
    ProcurementOrder,POItem,form=POItemForm,extra=2,
    can_delete=True,can_delete_extra=True,
    fields=['number','item','unit','quantity','cluster','pipeline','mr_number']
)

class PackingListForm(forms.ModelForm):
    class Meta:
        model = PackingList
        fields = ['project','number','po','date',        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['po'].queryset = self.fields['po'].queryset.filter(project=self.instance.project)
        self.fields['date'] = JalaliDateField(label='Packing List Date', 
            widget=AdminJalaliDateWidget 
        )

class PLItemForm(forms.ModelForm):
    class Mata:
        model = PLItem
        fields = ['po_item','quantity']
    def __init__(self, *args, **kwargs):
        po = kwargs.pop('po',None)
        super().__init__(*args, **kwargs)
        if po:
            poitems = [("","--------")]+[(item.id, item.__str__()) for item in po.items.all()]
            self.fields['po_item'].choices = poitems
        
        

PLItemFromSet = inlineformset_factory(
    PackingList,PLItem,form=PLItemForm,extra=2,
    can_delete=True,can_delete_extra=True,
    fields=['po_item','quantity']
)

class MaterialReceiptSheetForm(forms.ModelForm):
    class Meta:
        model = MaterialReceiptSheet
        fields = ['project','number','po','pl','warehouse']
    def __init__(self,user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)
        if self.user:
            whs = user.whs.all()
            self.fields['warehouse'].queryset = whs

        if self.instance.pk:
            self.fields['po'].queryset = self.fields['po'].queryset.filter(project=self.instance.project)
            self.fields['pl'].queryset = self.fields['pl'].queryset.filter(po=self.instance.po)

class MRSItemForm(forms.ModelForm):
    class Mata:
        model = MRSItem
        fields = ['pl_item','quantity','condition','loc']
    def __init__(self, *args, **kwargs):
        pl = kwargs.pop('pl',None)
        super().__init__(*args, **kwargs)
        if pl:
            poitems = [("","--------")]+[(item.id, item.__str__()) for item in pl.items.all()]
            self.fields['pl_item'].choices = poitems
        

MRSItemFromSet = inlineformset_factory(
    MaterialReceiptSheet,MRSItem,form=MRSItemForm,extra=2,
    can_delete=True,can_delete_extra=True,
    fields=['pl_item','quantity','condition','loc']
)

class ConditionForm(forms.ModelForm):
    class Meta:
        model = Condition
        fields = ['name',]

class MaterialIssueRequestForm(forms.ModelForm):
    class Meta:
        model = MaterialIssueRequest
        fields = ['project','number','po','pl','mrs','warehouse','issue_date','required_date','client_department','location']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['po'].queryset = self.fields['po'].queryset.filter(project=self.instance.project)
            self.fields['pl'].queryset = self.fields['pl'].queryset.filter(po=self.instance.po)
            self.fields['mrs'].queryset = self.fields['mrs'].queryset.filter(pl=self.instance.pl)
        self.fields['issue_date'] = JalaliDateField(label='Issue Date', 
            widget=AdminJalaliDateWidget 
        )
        self.fields['required_date'] = JalaliDateField(label='Required Date', 
            widget=AdminJalaliDateWidget 
        )

class MIRItemForm(forms.ModelForm):
    class Mata:
        model = MIRItem
        fields = ['mrs_item','quantity','remarks','cluster','pipeline']
    def __init__(self, *args, **kwargs):
        mrs = kwargs.pop('mrs',None)
        super().__init__(*args, **kwargs)
        if mrs:
            poitems = [("","--------")]+[(item.id, item.__str__()) for item in mrs.items.all()]
            self.fields['mrs_item'].choices = poitems

MIRItemFromSet = inlineformset_factory(
    MaterialIssueRequest,MIRItem,form=MIRItemForm,extra=2,
    can_delete=True,can_delete_extra=True,
    fields=['mrs_item','quantity','remarks','cluster','pipeline']
)