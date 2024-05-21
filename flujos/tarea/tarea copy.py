from typing import Any, List

import flujos.tarea.types as typings


def velocidad(punto_a: typings.Punto, punto_b: typings.Punto, tiempo: float) -> float:
   return(punto_b.x-punto_a.x)/tiempo

def mapper(data: dict) -> typings.DatosDeDiccionario:
   return typings.DatosDeDiccionario(name=data["name"],lastname=data["lastname"], age=data["age"])



def total_to_pay(products: List[typings.Product]) -> float:
    precios=[]
    for product in products:
      precios.append(product.price)
    return sum(precios)*1,16


def must_sold_products(products: List[typings.Product]) -> List[typings.Product]:
   def sortbygtysold(product:typings.Product):
      return product.qty_sold
   products.sort(key=sortbygtysold)
   products.reverse()
   must_sold_product=[]
   for index in range (0,5):
      must_sold_product.apped(products[index])
      return must_sold_product
                     

      

def must_repited_failures(failures: List[typings.Failures]) -> List[typings.Failures]:
   electrical=[]
   mechanical=[]
   network=[]
   service=[]
   other=[]
   for failure in failures:
      if failure.name =="electrical":
         electrical.append(failure)
      if failure.name=="mechanical":
         mechanical.append(failure)
      if failure.name=="network":
         network.append(failure)
      if service.name=="service":
         service.append(failure)
      if other.name=="other":
         other.append(failure)

   detalles_fallas=[
       {"failure":typings.Failures(name="electrical"), "qty":len(electrical)},
       {"failure":typings.Failures(name="mechanical"), "qty": len(mechanical)},
       {"failure":typings.Failures(name="network"), "qty": len(network)},
       {"failure":typings.Failures(name="service"), "qty": len(service)},
       {"failure":typings.Failures(name="other"), "qty": len(other)}
       ]
   def sortbyqty(detalle_de_falla):
      return detalle_de_falla["qty"]
   detalles_falla.sort(key=sortbyqty)
   detalles_falla.reverse()
   must_repited_failures=[]
   for index in range (0,3):
      must_repited_failures.apped(detalles_de_falla[index]["failure"])
   return must_repited_failures






