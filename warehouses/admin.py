from django.contrib import admin
from .models import WarehouseQ, WarehouseT, WarehouseY,WarehouseZ, CommonTracking, OutTimeTracking, WarehouseA0,WarehouseN,WarehouseU,WarehouseG,WarehouseX,WarehouseJ,WarehouseV,WarehouseH,WarehouseR,WarehouseHR,WarehouseA,WarehouseC,WarehouseK

@admin.register(WarehouseQ)
class WarehouseQAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_status')

@admin.register(WarehouseT)
class WarehouseTAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_status')

@admin.register(WarehouseY)
class WarehouseYAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_status')

@admin.register(WarehouseZ)
class WarehouseZAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_status')

@admin.register(WarehouseA0)
class WarehouseA0Admin(admin.ModelAdmin):
    list_display = ('id', 'product_status')    

@admin.register(WarehouseN)
class WarehouseNAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_status')
    
@admin.register(WarehouseU)
class WarehouseUAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_status')
    
@admin.register(WarehouseG)
class WarehouseGAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_status')

@admin.register(WarehouseX)
class WarehouseXAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_status')
            
@admin.register(WarehouseJ)
class WarehouseJAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_status')      
    
@admin.register(WarehouseV)
class WarehouseVAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_status')  

@admin.register(WarehouseH)
class WarehouseHAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_status')    

@admin.register(WarehouseR)
class WarehouseRAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_status')     

@admin.register(WarehouseHR)
class WarehouseHRAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_status')            

@admin.register(WarehouseA)
class WarehouseAAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_status')
      
@admin.register(WarehouseC)
class WarehouseCAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_status')
    
@admin.register(WarehouseK)
class WarehouseKAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_status')    
                    
@admin.register(CommonTracking)
class CommonTrackingAdmin(admin.ModelAdmin):
    list_display = ('id', 'warehouse_name', 'in_time', 'product_status')
    
    
@admin.register(OutTimeTracking)
class OutTimeTrackingAdmin(admin.ModelAdmin):
    list_display = ('id','out_time','warehouse_name','product_status')
