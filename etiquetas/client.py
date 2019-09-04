import Pyro4

uri = input("URI Object? ").strip()
answer = raw_input("Want a new ticket? [yes/no] ").strip()
gerar_ticket = Pyro4.Proxy(uri)
while(answer == "yes"):
    print(gerar_ticket.new_ticket())
    answer = raw_input("Want a new ticket? [Yes/No] ").strip()