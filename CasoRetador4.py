Catalogo_productos=["Maíz grano","Pepino", "Tomate verde"]
id_productos=["1","2","3"]

precio_maíz=float(285.55)
precio_pepino=float(334.72)
precio_tomate=float(129.00)

número_cajas=input("introduce el número de cajas: ")

ID_CLIENTE=input("Introduce el ID del producto : ")

precio_para_cajas_maíz=int(número_cajas)*(precio_maíz)
precio_para_cajas_pepino=int(número_cajas)*(precio_pepino)
precio_para_cajas_tomate=int(número_cajas)*(precio_tomate)

if ID_CLIENTE == "1":
  print("El producto es: Maíz grano")
  print("el precio por caja es de",(precio_maíz))
  print("el total a pagar es de:",(precio_para_cajas_maíz))
  
elif ID_CLIENTE== "2":
  print("El producto es: Pepino")
  print("el precio por caja es de",(precio_pepino))
  print("el total a pagar es de:",(precio_para_cajas_pepino))

elif ID_CLIENTE=="3":
  print("El producto es: Tomate Verde")
  print("el precio por caja es de",(precio_tomate))
  print("el total a pagar es de:",(precio_para_cajas_tomate))