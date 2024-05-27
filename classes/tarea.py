#1
class FabricaDeCarros:
   def __init__(self,nombre,marca,ubicacion) -> None:
      self.nombre=nombre
      self.marca=marca
      self.ubicacion=ubicacion
   def fabricar(self, modelo,tipo,ac,controlelec,añofab):
      return Carro(
          modelo=modelo,tipo=tipo,ac=ac,controlelec=controlelec,añofab=añofab,marca=self.marca
       )
class Carro:
   def __init__(self,modelo,tipo,ac,controlelec,añofab,marca):
      self.modelo=modelo
      self.tipo=tipo
      self.ac=ac
      self.controlelec=controlelec
      self.añofab=añofab
      self.marca=marca

fabricaford=FabricaDeCarros(nombre="ccc",marca="ford", ubicacion="vdl")
expedition=fabricaford.fabricar(modelo="expedition", tipo="camioneta", controlelec= True, ac= True, añofab= "2019")
print (expedition.marca)



#2
class Carpeta:
   def __init__(self,nombrec,ubicacionc,carpetas,archivos,) -> None:
      self.nombrec=nombrec
      self.ubicacionc=ubicacionc
      self.carpetas=carpetas
      self.archivos=archivos
class Archivo:
   def __init__(self,extension,narchivo,fcreacion,ubicacion) -> None:
      self.extension=extension
      self.narchivo=narchivo
      self.fcreacion=fcreacion
      self.ubicacion=ubicacion
     

   #3
   # gen_fib.next() [n1=0,n2=1] ->[n1=1, n2=1]
   # gen_fib.next() [n1=1, n2=1] -> [n1=1, n2=2]
   # gen_fib.next() [n1=1, n2=2] -> [n1=2, n2=3]
   # gen_fib.next() [n1=2, n2=3] -> [n1=3, n2=5]
   # gen_fib.next() [n1=3, n2=5] -> [n1=5, n2=8]
   # gen_fib.next() [n1=5, n2=8] -> [n1=8, n2=13]
class GeneradorFibonacci:
   def __init__(self):
      self.n1=0
      self.n2=1
      self.i=10
   def generar(self):
      fib=self.n1+self.n2
      self.n1=self.n2
      self.n2=fib
      self.i=self.i-1
      return fib
   def puedegenerar(self):
      return self.i> 0
    
fib_gen = GeneradorFibonacci()
while fib_gen.puedegenerar():
   print("Fibonacci number: " + str(fib_gen.generar()))
    
#4
class CentalTelefonica:
   def __init__(self,clientes) -> None:
      self.clientes=clientes
   def notificarmensaje(self,mensaje):
      for client in self.clientes:
         client.recibirmensaje(mensaje)
   def registrarcliente(self,cliente):
      self.clientes.append(cliente)
   def removercliente(self,cliente):
      #   filtered_list = []
      #   for reg_client in self.clientes:
      #      if not reg_client.telefono == cliente.telefono:
      #         filtered_list.append(reg_client)
      #   self.clientes = filtered_list
      # clientes -> [clientA, clienteB, clienteC]
      #    enumerate -> 0,     1,       2
      for index, reg_client in enumerate(self.clientes):
         if reg_client.telefono == cliente.telefono:
            self.clientes.pop(index)
class Cliente:
   def __init__(self,nombre,telefono) -> None:
      self.nombre=nombre
      self.telefono=telefono
   def recibirmensaje(self,mensaje):
      print("Mi nombre es " + self.nombre + ", recibi el mensaje: " + mensaje)
    

movistar=CentalTelefonica(clientes=[])
bea=Cliente(nombre="Bea",telefono="04248781207")
mirna=Cliente(nombre="Mirna",telefono="04249204507")
cruz=Cliente(nombre="Cruz",telefono="04248703454")
movistar.registrarcliente(cliente=bea)
movistar.registrarcliente(cliente=mirna)
movistar.registrarcliente(cliente=cruz)
movistar.notificarmensaje(mensaje="Hola amo a Gabriel")
movistar.removercliente(cruz)
movistar.notificarmensaje("Cruz ha salido del grupo")


#5
class TiendaMascota:
   def __init__(self,name, mascotas, clientes) -> None:
      self.mascotas = mascotas
      self.clientes = clientes
      self.name = name
   def registrar_adopcion(self,mascota,cliente):
      tengo_esa_mascota = self.es_mi_mascota(mascota=mascota)
      tengo_ese_cliente = self.es_mi_cliente(cliente=cliente)
      if not tengo_esa_mascota or not tengo_ese_cliente:
         print("No puedes adoptar")
      else:
         mascota.dueño = cliente
         self.remover_mascota(mascota=mascota)

   def remover_mascota(self,mascota):
      filtered_list = []
      for mascota_reg in self.mascotas:
         if mascota.namem == mascota_reg.namem and mascota_reg.especie == mascota.especie and mascota.color == mascota_reg.color:
            continue
         else:
            filtered_list.append(mascota_reg)
      self.mascotas = filtered_list

   def nuevocliente(self,nombrenuevo,numeronuevo):
      nc = Cliente(name=nombrenuevo, num=numeronuevo)
      self.clientes.append(nc)

   def remover_cliente(self,cliente):
      filtered_list = []
      for xcliente in self.clientes:
         if cliente.name == xcliente.name and cliente.num == xcliente.num:
            continue
         else:
            filtered_list.append(xcliente)
         self.clientes = filtered_list
      
   def nuevamascota(self,nraza,ncolor,ndueño,nnamem,nespecie):
      nm=Mascota(raza=nraza, color=ncolor,dueño=ndueño,namem=nnamem,especie=nespecie)
      self.mascotas.append(nm)

   def es_mi_mascota(self, mascota) -> bool:
      es_mi_mascota = False
      for mascota_reg in self.mascotas:
         if mascota.namem == mascota_reg.namem and mascota_reg.especie == mascota.especie and mascota.color == mascota_reg.color:
            es_mi_mascota = True
      return es_mi_mascota
   def es_mi_cliente(self, cliente) -> bool:
      es_mi_cliente = False
      for cliente_reg in self.clientes:
         if cliente.name == cliente_reg.name and cliente.num == cliente_reg.num:
            es_mi_cliente = True
      return es_mi_cliente
       

class Cliente:
   def __init__(self,name,num) -> None:
      self.name=name
      self.num=num
   
      
class Mascota:
   def __init__(self,raza,color,dueño,namem,especie) -> None:
      self.raza=raza
      self.color=color
      self.dueño=dueño
      self.namem=namem
      self.especie=especie




