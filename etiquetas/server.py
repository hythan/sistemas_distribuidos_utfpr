import Pyro4

ticket = 0
@Pyro4.expose
class GeraEtiqueta(object):

    def new_ticket(self):
        global ticket
        ticket += 1
        return "Etiqueta {0}".format(ticket)

daemon = Pyro4.Daemon()
uri = daemon.register(GeraEtiqueta)

print("Ready. Object uri =", uri)
daemon.requestLoop()