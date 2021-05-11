from woocommerce import API
import time



def log_write(x):
    log = open("log.txt",'a',encoding="utf-8")
    log.write(str(x))
    log.write('\n')
    log.close()

hoy = time.strftime(' %d-%m-%Y', time.localtime())
wcapi = API(
    url="http://frutosare.com.ar/",
    consumer_key="",
    consumer_secret="",
    version="wc/v3"
)


repartidor = input("Nombre del repartidor: ")
numeroPedido = int(input("ingrese numero de pedido: "))
log_write(hoy + " " + repartidor)



while numeroPedido!=-1:
    nombredelarchivo = "planilla " + str(repartidor) + str(hoy) + ".txt"
    #log.write(numeroPedido, '\n')
    try:
        salida = open(nombredelarchivo,'a',encoding="utf-8")
        ordenAObtener = "orders/" + str(numeroPedido)
        order = (wcapi.get(ordenAObtener).json())
        shipping = order["shipping"]

        #address
        print(shipping["address_1"], " ",shipping["address_2"] )
        salida.write(shipping["address_1"])
        salida.write(" ")
        salida.write(shipping["address_2"])
        if( (shipping["state"]) != "C"):
            print(" provincia ", shipping["city"])
            salida.write(" provincia ")
            salida.write(shipping["city"])
            
        salida.write("x")

        # payment
        if (order["payment_method_title"]) == "Contra reembolso":
            print(order["total"])
            salida.write((order["total"]))
        else:
            if(order["payment_method_title"]) == "Paga con el medio de pago que prefieras":
                print("MercadoPago")
                salida.write("MercadoPago")

            else:
                print (order["payment_method_title"])
                salida.write("Transferencia")
        
        salida.write("x")

        # nota
        print("Nota: ",order["customer_note"])
        print(" ")
        salida.write(order["customer_note"])
        salida.write('\n')
        salida.close()
        print("-"*15)
        log_write(numeroPedido)
        numeroPedido = int(input("ingrese numero de pedido: "))
    except ValueError:
        numeroPedido = int(input("ingrese numero de pedido: "))
    except KeyboardInterrupt:
        salida.close()
        break
