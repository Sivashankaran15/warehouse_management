from django.shortcuts import render, redirect, get_object_or_404
from .models import WarehouseQ, WarehouseT, WarehouseY,WarehouseZ, CommonTracking, OutTimeTracking, WarehouseA0,WarehouseN,WarehouseU,WarehouseG,WarehouseX,WarehouseJ,WarehouseV,WarehouseH,WarehouseR,WarehouseHR,WarehouseA,WarehouseC,WarehouseK
from django.utils import timezone
from django.db import transaction
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect
from django.contrib.auth import logout


VALID_USERNAME = "doozyamr"
VALID_PASSWORD = "amr@2024"

def block2block(request):
    return render(request, 'block2block.html')

def custom_logout_view(request):
    logout(request)
    return redirect('login')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            request.session['logged_in'] = True
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def home(request):
    if not request.session.get('logged_in'):
        return redirect('login')

    warehouse_q_total = WarehouseQ.objects.count()
    warehouse_t_total = WarehouseT.objects.count()
    warehouse_y_total = WarehouseY.objects.count()
    warehouse_z_total = WarehouseZ.objects.count()
    
    warehouse_a0_total = WarehouseA0.objects.count()
    warehouse_n_total = WarehouseN.objects.count()
    warehouse_u_total = WarehouseU.objects.count()
    warehouse_g_total = WarehouseG.objects.count()
    
    warehouse_x_total = WarehouseX.objects.count()
    warehouse_j_total = WarehouseJ.objects.count()
    warehouse_v_total = WarehouseV.objects.count()
    
    warehouse_h_total = WarehouseH.objects.count()
    warehouse_r_total = WarehouseR.objects.count()
    warehouse_hr_total = WarehouseHR.objects.count()
    
    warehouse_a_total = WarehouseA.objects.count()
    warehouse_c_total = WarehouseC.objects.count()
    warehouse_k_total = WarehouseK.objects.count()
    
    warehouse_q_status = WarehouseQ.objects.filter(product_status=True).count()
    warehouse_t_status = WarehouseT.objects.filter(product_status=True).count()
    warehouse_y_status = WarehouseY.objects.filter(product_status=True).count()
    warehouse_z_status = WarehouseZ.objects.filter(product_status=True).count()
    warehouse_a0_status = WarehouseA0.objects.filter(product_status=True).count()
    warehouse_n_status = WarehouseN.objects.filter(product_status=True).count()
    warehouse_u_status = WarehouseU.objects.filter(product_status=True).count()
    warehouse_g_status = WarehouseG.objects.filter(product_status=True).count()
    warehouse_x_status = WarehouseX.objects.filter(product_status=True).count()
    warehouse_j_status = WarehouseJ.objects.filter(product_status=True).count()
    warehouse_v_status = WarehouseV.objects.filter(product_status=True).count()
    warehouse_h_status = WarehouseH.objects.filter(product_status=True).count()
    warehouse_r_status = WarehouseR.objects.filter(product_status=True).count()
    warehouse_hr_status = WarehouseHR.objects.filter(product_status=True).count()
    warehouse_a_status = WarehouseA.objects.filter(product_status=True).count()
    warehouse_c_status = WarehouseC.objects.filter(product_status=True).count()
    warehouse_k_status = WarehouseK.objects.filter(product_status=True).count()
    
    context = {
        'warehouse_q_status': warehouse_q_status,
        'warehouse_t_status': warehouse_t_status,
        'warehouse_y_status': warehouse_y_status,
        'warehouse_z_status': warehouse_z_status,
        'warehouse_a0_status': warehouse_a0_status,
        'warehouse_n_status': warehouse_n_status,
        'warehouse_u_status': warehouse_u_status,
        'warehouse_g_status': warehouse_g_status,
        'warehouse_x_status': warehouse_x_status,
        'warehouse_j_status': warehouse_j_status,
        'warehouse_v_status': warehouse_v_status,
        'warehouse_h_status': warehouse_h_status,
        'warehouse_r_status': warehouse_r_status,
        'warehouse_hr_status': warehouse_hr_status,
        'warehouse_a_status': warehouse_a_status,
        'warehouse_c_status': warehouse_c_status,
        'warehouse_k_status': warehouse_k_status, 
        
        'warehouse_q_total': warehouse_q_total,
        'warehouse_t_total': warehouse_t_total,
        'warehouse_y_total': warehouse_y_total,
        'warehouse_z_total': warehouse_z_total,
        'warehouse_a0_total': warehouse_a0_total,
        'warehouse_n_total': warehouse_n_total,
        'warehouse_u_total': warehouse_u_total,
        'warehouse_g_total': warehouse_g_total,
        'warehouse_x_total': warehouse_x_total,
        'warehouse_j_total': warehouse_j_total,
        'warehouse_g_total': warehouse_g_total,
        'warehouse_x_total': warehouse_x_total,
        'warehouse_j_total': warehouse_j_total,        
        'warehouse_v_total': warehouse_v_total,
        'warehouse_h_total': warehouse_h_total,
        'warehouse_r_total': warehouse_r_total,   
        'warehouse_hr_total': warehouse_hr_total,        
        'warehouse_a_total': warehouse_a_total,
        'warehouse_c_total': warehouse_c_total,
        'warehouse_k_total': warehouse_k_total,      
    
    }
    return render(request, 'home.html', context)

def product_status(request):


    warehouse_q_total = WarehouseQ.objects.count()
    warehouse_t_total = WarehouseT.objects.count()
    warehouse_y_total = WarehouseY.objects.count()
    warehouse_z_total = WarehouseZ.objects.count()
    warehouse_a0_total = WarehouseA0.objects.count()
    warehouse_n_total = WarehouseN.objects.count()
    warehouse_u_total = WarehouseU.objects.count()
    warehouse_g_total = WarehouseG.objects.count()
    warehouse_x_total = WarehouseX.objects.count()
    warehouse_j_total = WarehouseJ.objects.count()
    warehouse_v_total = WarehouseV.objects.count()
    warehouse_h_total = WarehouseH.objects.count()
    warehouse_r_total = WarehouseR.objects.count()
    warehouse_hr_total = WarehouseHR.objects.count()
    warehouse_a_total = WarehouseA.objects.count()
    warehouse_c_total = WarehouseC.objects.count()
    warehouse_k_total = WarehouseK.objects.count()
    
    warehouse_q_status = WarehouseQ.objects.filter(product_status=True).count()
    warehouse_t_status = WarehouseT.objects.filter(product_status=True).count()
    warehouse_y_status = WarehouseY.objects.filter(product_status=True).count()
    warehouse_z_status = WarehouseZ.objects.filter(product_status=True).count()
    warehouse_a0_status = WarehouseA0.objects.filter(product_status=True).count()
    warehouse_n_status = WarehouseN.objects.filter(product_status=True).count()
    warehouse_u_status = WarehouseU.objects.filter(product_status=True).count()
    warehouse_g_status = WarehouseG.objects.filter(product_status=True).count()
    warehouse_x_status = WarehouseX.objects.filter(product_status=True).count()
    warehouse_j_status = WarehouseJ.objects.filter(product_status=True).count()
    warehouse_v_status = WarehouseV.objects.filter(product_status=True).count()
    warehouse_h_status = WarehouseH.objects.filter(product_status=True).count()
    warehouse_r_status = WarehouseR.objects.filter(product_status=True).count()
    warehouse_hr_status = WarehouseHR.objects.filter(product_status=True).count()
    warehouse_a_status = WarehouseA.objects.filter(product_status=True).count()
    warehouse_c_status = WarehouseC.objects.filter(product_status=True).count()
    warehouse_k_status = WarehouseK.objects.filter(product_status=True).count()
    
    context = {
        'warehouse_q_status': warehouse_q_status,
        'warehouse_t_status': warehouse_t_status,
        'warehouse_y_status': warehouse_y_status,
        'warehouse_z_status': warehouse_z_status,
        'warehouse_a0_status': warehouse_a0_status,
        'warehouse_n_status': warehouse_n_status,
        'warehouse_u_status': warehouse_u_status,
        'warehouse_g_status': warehouse_g_status,
        'warehouse_x_status': warehouse_x_status,
        'warehouse_j_status': warehouse_j_status,
        'warehouse_v_status': warehouse_v_status,
        'warehouse_h_status': warehouse_h_status,
        'warehouse_r_status': warehouse_r_status,
        'warehouse_hr_status': warehouse_hr_status,
        'warehouse_a_status': warehouse_a_status,
        'warehouse_c_status': warehouse_c_status,
        'warehouse_k_status': warehouse_k_status, 
        
        'warehouse_q_total': warehouse_q_total,
        'warehouse_t_total': warehouse_t_total,
        'warehouse_y_total': warehouse_y_total,
        'warehouse_z_total': warehouse_z_total,
        'warehouse_a0_total': warehouse_a0_total,
        'warehouse_n_total': warehouse_n_total,
        'warehouse_u_total': warehouse_u_total,
        'warehouse_g_total': warehouse_g_total,
        'warehouse_x_total': warehouse_x_total,
        'warehouse_j_total': warehouse_j_total,
        'warehouse_g_total': warehouse_g_total,
        'warehouse_x_total': warehouse_x_total,
        'warehouse_j_total': warehouse_j_total,        
        'warehouse_v_total': warehouse_v_total,
        'warehouse_h_total': warehouse_h_total,
        'warehouse_r_total': warehouse_r_total,   
        'warehouse_hr_total': warehouse_hr_total,        
        'warehouse_a_total': warehouse_a_total,
        'warehouse_c_total': warehouse_c_total,
        'warehouse_k_total': warehouse_k_total,      
    
    }
    return render(request, 'product_status.html', context)

def available_slots(request, warehouse_name):
    if warehouse_name == 'Q':
        available_slots = WarehouseQ.objects.filter(product_status=False)
    elif warehouse_name == 'T':
        available_slots = WarehouseT.objects.filter(product_status=False)
    elif warehouse_name == 'Y':
        available_slots = WarehouseY.objects.filter(product_status=False)
    elif warehouse_name == 'Z':
        available_slots = WarehouseZ.objects.filter(product_status=False)
    elif warehouse_name == 'A0':
        available_slots = WarehouseA0.objects.filter(product_status=False)
    elif warehouse_name == 'N':
        available_slots = WarehouseN.objects.filter(product_status=False)
    elif warehouse_name == 'U':
        available_slots = WarehouseU.objects.filter(product_status=False)
    elif warehouse_name == 'G':
        available_slots = WarehouseG.objects.filter(product_status=False)
    elif warehouse_name == 'X':
        available_slots = WarehouseX.objects.filter(product_status=False)
    elif warehouse_name == 'J':
        available_slots = WarehouseJ.objects.filter(product_status=False)
    elif warehouse_name == 'V':
        available_slots = WarehouseV.objects.filter(product_status=False)
    elif warehouse_name == 'H':
        available_slots = WarehouseH.objects.filter(product_status=False)
    elif warehouse_name == 'R':
        available_slots = WarehouseR.objects.filter(product_status=False)
    elif warehouse_name == 'HR':
        available_slots = WarehouseHR.objects.filter(product_status=False)
    elif warehouse_name == 'A':
        available_slots = WarehouseA.objects.filter(product_status=False)
    elif warehouse_name == 'C':
        available_slots = WarehouseC.objects.filter(product_status=False)
    elif warehouse_name == 'K':
        available_slots = WarehouseK.objects.filter(product_status=False)
    else:
        available_slots = []

    slots = [{'id': slot.id} for slot in available_slots]
    return JsonResponse({'available_slots': slots})

   
def transfer_product(request):
    if request.method == 'POST':
        from_warehouse = request.POST['from_warehouse']
        to_warehouse = request.POST['to_warehouse']
        product_name = request.POST['product_name']
        slot_id = request.POST['slot_id']

        transfer_successful = False

        if not request.session.get('logged_in'):
            return redirect('login')

        if from_warehouse == 'A':
            to_warehouse_model = get_warehouse_model(to_warehouse)
            available_slot = to_warehouse_model.objects.filter(id=slot_id).first()
            if available_slot:
                available_slot.product_status = True
                available_slot.product_name = product_name
                available_slot.save()
                CommonTracking.objects.create(
                    warehouse_name=to_warehouse,
                    in_time=timezone.now(),
                    product_status=True,
                    product_name=product_name,
                )
            else:
                messages.error(request, f'Selected slot {slot_id} is not available in Warehouse {to_warehouse}.')
        else:
            from_warehouse_model = get_warehouse_model(from_warehouse)
            to_warehouse_model = get_warehouse_model(to_warehouse)

            with transaction.atomic():
                product = from_warehouse_model.objects.filter(product_status=True).first()
                available_slot = to_warehouse_model.objects.filter(id=slot_id).first()
                if product and available_slot:
                    available_slot.product_status = True
                    available_slot.product_name = product_name
                    available_slot.save()
                    CommonTracking.objects.create(
                        warehouse_name=to_warehouse,
                        in_time=timezone.now(),
                        product_status=True,
                        product_name=product_name,
                    )

                    product.product_status = False
                    product.product_name = None
                    product.save()

                    tracking_entry = CommonTracking.objects.filter(
                        warehouse_name=from_warehouse,
                        id=product.id
                    ).first()
                    if tracking_entry:
                        tracking_entry.out_time = timezone.now()
                        tracking_entry.save()
                    transfer_successful = True

                    OutTimeTracking.objects.create(
                        warehouse_name=from_warehouse,
                        out_time=timezone.now(),
                        product_status=False
                    )

                else:
                    if not product:
                        messages.error(request, f'No available product in Warehouse {from_warehouse} to transfer.')
                    if not available_slot:
                        messages.error(request, f'Selected slot {slot_id} is not available in Warehouse {to_warehouse}.')

        if transfer_successful:
            return redirect('success')
        else:
            return redirect('home')

    return redirect('home')

def edit_products(request):
    warehouse_q = WarehouseQ.objects.all()
    warehouse_t = WarehouseT.objects.all()
    warehouse_y = WarehouseY.objects.all()
    warehouse_z = WarehouseZ.objects.all()
    warehouse_a0 = WarehouseA0.objects.all()
    warehouse_n = WarehouseN.objects.all()
    warehouse_u = WarehouseU.objects.all()
    warehouse_g = WarehouseG.objects.all()
    warehouse_x = WarehouseX.objects.all()
    warehouse_j = WarehouseJ.objects.all()
    warehouse_v = WarehouseV.objects.all()
    warehouse_h = WarehouseH.objects.all()
    warehouse_r = WarehouseR.objects.all()
    warehouse_hr = WarehouseHR.objects.all()
    warehouse_a = WarehouseA.objects.all()
    warehouse_c = WarehouseC.objects.all()
    warehouse_k = WarehouseK.objects.all()    
    
    context = {
        'warehouse_q': warehouse_q,
        'warehouse_t': warehouse_t,
        'warehouse_y': warehouse_y,
        'warehouse_z': warehouse_z,
        'warehouse_a0': warehouse_a0,
        'warehouse_n': warehouse_n,
        'warehouse_u': warehouse_u,
        'warehouse_g': warehouse_g,
        'warehouse_x': warehouse_x,
        'warehouse_j': warehouse_j,
        'warehouse_v': warehouse_v,
        'warehouse_h': warehouse_h,
        'warehouse_r': warehouse_r,
        'warehouse_hr': warehouse_hr,
        'warehouse_a': warehouse_a,
        'warehouse_c': warehouse_c,
        'warehouse_k': warehouse_k,    
    }
    return render(request, 'edit_products.html', context)

def edit_product_status(request, warehouse, product_id):
    warehouse_model = get_warehouse_model(warehouse)
    product = get_object_or_404(warehouse_model, id=product_id)

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'set_to_0':
            product.product_status = False
            product.product_name = None  # Reset product name
        elif action == 'set_to_1':
            product.product_status = True
            product.product_name = request.POST.get('product_name')
        product.save()
        return redirect('edit_products')

    return render(request, 'edit_products.html', {'warehouse_q': WarehouseQ.objects.all(),
                                                  'warehouse_t': WarehouseT.objects.all(),
                                                  'warehouse_y': WarehouseY.objects.all(),
                                                  'warehouse_z': WarehouseZ.objects.all(),
                                                  'warehouse_a0': WarehouseA0.objects.all(),
                                                  'warehouse_n': WarehouseN.objects.all(),
                                                  'warehouse_u': WarehouseU.objects.all(),
                                                  'warehouse_g': WarehouseG.objects.all(),
                                                  'warehouse_x': WarehouseX.objects.all(),
                                                  'warehouse_j': WarehouseJ.objects.all(),
                                                  'warehouse_v': WarehouseV.objects.all(),
                                                  'warehouse_h': WarehouseH.objects.all(),
                                                  'warehouse_r': WarehouseR.objects.all(),     
                                                  'warehouse_hr': WarehouseHR.objects.all(),
                                                  'warehouse_a': WarehouseA.objects.all(),
                                                  'warehouse_c': WarehouseC.objects.all(),
                                                  'warehouse_k': WarehouseK.objects.all()                                             
                                                  })

def transfer_products(request, from_warehouse, to_warehouse):
    if request.method == 'POST':
        if not request.session.get('logged_in'):
            return redirect('login')

        from_model = get_warehouse_model(from_warehouse)
        to_model = get_warehouse_model(to_warehouse)
        product_id = request.POST['source_product_id']
        dest_slot_id = request.POST['dest_slot_id']

        try:
            with transaction.atomic():
                product = from_model.objects.get(id=product_id, product_status=True)
                dest_slot = to_model.objects.get(id=dest_slot_id, product_status=False)

                # Transfer product
                dest_slot.product_status = True
                dest_slot.product_name = product.product_name
                dest_slot.save()

                # Update source product status
                product.product_status = False
                product.product_name = None
                product.save()

                # Update tracking
                CommonTracking.objects.create(
                    warehouse_name=to_warehouse,
                    in_time=timezone.now(),
                    product_status=True,
                    product_name=product.product_name
                )
                OutTimeTracking.objects.create(
                    warehouse_name=from_warehouse,
                    out_time=timezone.now(),
                    product_status=False
                )

                return redirect('success')

        except from_model.DoesNotExist:
            messages.error(request, f'Product with ID {product_id} not found in Warehouse {from_warehouse}.')
        except to_model.DoesNotExist:
            messages.error(request, f'Slot with ID {dest_slot_id} not available in Warehouse {to_warehouse}.')
        except Exception as e:
            messages.error(request, f'Error occurred: {e}')
        return redirect('home')
    return redirect('home')

def get_products(request, source, destination):
    if source not in [' Q', 'T', 'Y','Z','A0','N','U','G','X','J','V','H','R',"HR","A","C","K"] or destination not in ['Q', 'T', 'Y','Z','A0','N','U','G','X','J','V','H','R',"HR","A","C","K"]:
        return JsonResponse({'source_products': [], 'dest_slots': []})
    source_model = get_warehouse_model(source)
    dest_model = get_warehouse_model(destination)
    source_products = source_model.objects.filter(product_status=True).values('id', 'product_name')
    dest_slots = dest_model.objects.filter(product_status=False).values('id')
    return JsonResponse({'source_products': list(source_products), 'dest_slots': list(dest_slots)})

def get_warehouse_model(warehouse_name):
    if warehouse_name == 'Q':
        return WarehouseQ
    elif warehouse_name == 'T':
        return WarehouseT
    elif warehouse_name == 'Y':
        return WarehouseY
    elif warehouse_name == 'Z':
        return WarehouseZ
    elif warehouse_name == 'A0':
        return WarehouseA0
    elif warehouse_name == 'N':
        return WarehouseN
    elif warehouse_name == 'U':
        return WarehouseU
    elif warehouse_name == 'G':
        return WarehouseG
    elif warehouse_name == 'X':
        return WarehouseX    
    elif warehouse_name == 'J':
        return WarehouseJ
    elif warehouse_name == 'V':
        return WarehouseV
    elif warehouse_name == 'H':
        return WarehouseH    
    elif warehouse_name == 'R':
        return WarehouseR   
    elif warehouse_name == 'HR':
        return WarehouseHR      
    elif warehouse_name == 'A':
        return WarehouseA
    elif warehouse_name == 'C':
        return WarehouseC         
    elif warehouse_name == 'K':
        return WarehouseK      
    else:
        raise ValueError("Invalid warehouse name")

def success(request):
    return render(request, 'success.html')
