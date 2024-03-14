from django.shortcuts import render,redirect
from Newapp.models import productdb,orderdb

# Create your views here.
def product_page(request):
    return render(request,"Product_details.html")
def savedata(request):
    if request.method=="POST":
        na=request.POST.get('pname')
        dn=request.POST.get('dname')
        s=request.POST.get('size')
        c=request.POST.get('colour')
        st=request.POST.get('status')
        obj=productdb(Product_name=na,Description=dn,Size=s,Color=c,Status=st)
        obj.save()
        return redirect(product_page)
def display_product(request):
    data=productdb.objects.all()
    return render(request,"DisplayProduct.html",{'data':data})
def delete_product(request,dataid):
    book=productdb.objects.filter(id=dataid)
    book.delete()
    return redirect(display_product)
def edit_product(request,dataid):
    product=productdb.objects.get(id=dataid)
    return render(request,"Editdetails.html",{'product':product})

def update_product(request,dataid):
    if request.method=="POST":
        b=request.POST.get('pname')
        d=request.POST.get('dname')
        si=request.POST.get('size')
        co=request.POST.get('colour')
        s=request.POST.get('status')
        productdb.objects.filter(id=dataid).update(Product_name=b,Description=d,Size=si,Color=co,Status=s)
        return redirect(display_product)

def orderpage(request):
    return render(request,"Order_details.html")
def saveorderdata(request):
    if request.method == "POST":
        cn = request.POST.get('customer')
        pn = request.POST.get('proname')
        no = request.POST.get('pnumber')
        obj = orderdb(Customer_name=cn,Pro_name=pn,Purchase_no=no)
        obj.save()
        return redirect(orderpage)