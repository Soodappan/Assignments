print("WELCOME TO GST CALCULATER")
originalprice=int(input("enter the original price:"))
netprice=int(input("enter the net price:"))
gst=netprice-originalprice
gstamount=((gst*100)/originalprice)
print(gstamount,)

