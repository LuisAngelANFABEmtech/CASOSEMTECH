Cemento=input("ingresa el tamaño de la carga de cemento en kg :")
         
Yeso= input("ingresa la carga de Yeso en KG: ")

CARGATOTAL=(int(Cemento)+(int(Yeso)))

print("La carga total del envío es de: ",(CARGATOTAL),"kilos")


CARGA_MÁXIMA_CAMIÓN=int(3254)

Envío= CARGATOTAL <= CARGA_MÁXIMA_CAMIÓN and CARGATOTAL >= (CARGA_MÁXIMA_CAMIÓN/2)

print("Puede realizarse el envío: ",(Envío))