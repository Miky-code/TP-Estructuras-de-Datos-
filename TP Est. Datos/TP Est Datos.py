#TP integrador

class servidorcorreo():
    ##- envia y recibe los msj.

    def enviar(self, mensaje, remitente, destinatario):
        pass

    def recibir(self, mensaje, destinatario):
        pass


class Mensaje(): #crear el cuerpo del msj con el destinatario y el remitente.
    def __init__(self, remitente, destinatario, cuerpomsj):
        self._remitente = remitente
        self._destinatario = destinatario
        self._cuerpomsj = cuerpomsj
    def __str__(self): #crear el mensaje con ayuda del metodo str.
        return(f"de {self._remitente} para: {self._destinatario._mail} , mensaje: {self._cuerpomsj}")

class usuario:
    def __init__(self, mail):
        self._mail = mail
        
    def __str__(self):
        return f"usuario: {self._mail}"
    
    def get_mail(self):
        return self._mail
    
    
class carpeta(servidorcorreo):
    def __init__(self):
        self._mensajes = []
        #enviar mensajes : generar el mensaje y printear desde donde lo envio y a quien

    def enviar(self, mensaje, remitente, destinatario):
        self._mensajes.append(mensaje)
        print(f"Enviaste mensaje desde {mensaje._remitente} a {mensaje._destinatario._mail}")

     # recibir mensajes
    def recibir(self, usuario):
        for mensaje in self._mensajes:
            if mensaje._destinatario._mail == usuario._mail:
                print(mensaje)
    
    def listar(self, usuario = None):
        # si el usuario es None, devuelve todos los msj
        if usuario == None:
            return self._mensajes
        else:
            return [mensaje for mensaje in self._mensajes if mensaje._destinatario._mail == usuario._mail]



usuario1 = usuario("carlos@mail.com")
usuario2 = usuario("juan@mail.com")

bandeja = carpeta ()

mensaje1 = Mensaje (usuario1, usuario2, "Hola Juancito")
mensaje2 = Mensaje (usuario2, usuario1, "Que onda Carlitos")
mensaje3 = Mensaje (usuario1, usuario2, "Todo bien y vos?")
mensaje4 = Mensaje (usuario2, usuario1, "Aca andamos amigo")


bandeja.enviar(mensaje1, usuario1, usuario2)
bandeja.enviar(mensaje2, usuario2, usuario1)
bandeja.enviar(mensaje3, usuario1, usuario2)
bandeja.enviar(mensaje4, usuario2, usuario1)

print("Mensajes para Juancito:")
bandeja.recibir(usuario2)

print("**************************")

print("Mensajes para Carlitos:")
bandeja.recibir(usuario1)

print("************listar mensajes*************")

print("Mensajes de Carlos")
for Mensaje in bandeja.listar(usuario1):
    print(Mensaje)

print("Mensajes de Juan")
for Mensaje in bandeja.listar():
    print(Mensaje)


