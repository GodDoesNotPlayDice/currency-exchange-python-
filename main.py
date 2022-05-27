import os
from src.functions import *
paises = currencysFormatter(country,0)
paises_cod = currencysFormatter(country,1)
cod_value = currencysFormatter(country,2)
time = fecha_hoy()
fecha = lambda x : f'{time[2]}/{time[1]}/{time[0]}'
hora = lambda x : f'{time[3]}:{time[4]}'
close = True
date,result,estado = '','',''
conversiones = []
while close:
    try:
        os.system('cls')
        print('#################')
        print(f'Datos...\nPaises Consultados: {date}\nUltima conversion: {result}')
        print(f'Estado de Operacion: {estado}')
        print('#################')
        print("Bienvenido al conversor online (Python)")
        print(f"Fecha de hoy {fecha(time)}, Hora de hoy {hora(time)}.")
        print("1) Buscar codigo de divisa (Busqueda por pais)")
        print("2) Hacer conversion de dos monedas (Comparar dos Monedas, con codigo de divisa)")
        print("3) Ver valores actuales de las monedas (Comparadas con USD, EUR, GBP, JPY, CNY, RUB, INR)")
        print("4) Salir")
        opc = int(input("Porfavor oprime una opcion: "))
        if opc == 1:
            cont = 1
            print("Listas de Paises...")
            for i in paises:
                print(f"{cont}) {i.strip()}")
                cont+=1
            while True:
                pais = int(input("Numero de Pais: "))-1
                validPais = True if not pais < 0 or pais > 268 else False
                date = validCountry(validPais,pais)
                if validPais:
                    estado = 'Consulta de Pais terminado..'
                    break
        elif opc == 2:
            print("Usar codigo de divisas")
            while True:
                try:
                    from_ = str(input('Pais de: ')).upper()
                    to_ = str(input('Destino de: ')).upper()
                    if len(from_) > 3 and len(to_) > 3:
                        estado = "Datos Invalidos, recuerda que el codigo de divisa es de 3 DIGITOS"
                        break
                    else:
                        if not cod_value.count(from_) and cod_value.count(to_):
                            estado = "Un codigo de pais no es valido"
                            break
                        else:
                            value_ = currency_comparing(from_,to_)
                            indexTo_ = cod_value.index(to_)
                            indexFrom_ = cod_value.index(from_)
                            fecha_valor = fechaCurrency(from_,to_)
                            print(f"Actualizacion de los valores: {fecha_valor}")
                            valorActual = f' 1 {from_} = {value_} {to_}'
                            print(f"Valor actual: {valorActual}")
                            while True:
                                try:
                                    cantidad = float(input('Cantidad que desea convertir: '))
                                    op = cantidad * float(value_)
                                    result = f'{round(float((op)),2)} {paises_cod[indexTo_]}'
                                    print(f"Cantidad convetida: {result}")
                                    conversiones.append([historial(indexFrom_,indexTo_,valorActual,op,fecha(time),hora(time),fecha_valor)])
                                    break
                                except ValueError:
                                    print('CANTIDAD VALOR --porfavor ingresar un valor valido')
                            opc_aux = str(input('Desea otra operacion?\n1)Si\nX)No \ (X)Representa cualquier tecla\nOpcion: '))
                            if not opc_aux == '1':
                                estado = 'Operacion de Conversion terminada.'
                                break
                except ValueError:
                     estado = 'Codigos de paises no econtrados'
                     break
        elif opc == 3:
            while True:
                try:
                    print('USD', 'EUR', 'GBP', 'JPY', 'CNY', 'RUB', 'INR')
                    from_ = str(input('Codigo de pais de: ')).upper()
                    if len(from_) > 3:
                        estado = "Datos Invalidos, recuerda que el codigo de divisa es de 3 DIGITOS"
                        break
                    else:
                        if not cod_value.count(from_):
                            estado = "Un codigo de pais no es valido"
                            break
                        else:
                            while True:
                                try:
                                    value_ = float(input(f'Cantidad de {from_}: '))
                                    print('Cargando datos...')
                                    big_currencys = ['USD', 'EUR', 'GBP', 'JPY', 'CNY', 'RUB', 'INR']
                                    g_values = []
                                    for i in big_currencys:
                                        v = value_ * float(currency_comparing(from_,i))
                                        g_values.append(f'Valor de {value_} {from_} es {round(v,2)} {i}')
                                    for i in g_values:
                                        print(i)
                                    break
                                except ValueError:
                                    print('Ingresa un codigo valido')
                            opc_aux = str(input('Desea otra operacion?\n1)Si\nX)No \ (X)Representa cualquier tecla\nOpcion: '))
                            if not opc_aux == '1':
                                estado = 'Consulta de valores terminada...'
                                break
                except ValueError:
                    estado = "Un codigo de pais no es valido o no es encontrado"
                    break
        elif opc == 4:
            close = False
            os.system('cls')
            print("Hasta pronto!...")
            t.sleep(1)
            cont = 3
            while not cont == 0 :
                os.system('cls')
                print(f"la aplicacion se cerrara en {cont} Segundos")
                cont-=1
                t.sleep(1)
            quit()
        else:
            estado = "Opcion invlida"
    except ValueError:
        estado = "VALUE ERROR (MENU - MAIN ) ingrese nuevamente un dato valido "
    except IndexError:
        estado = " (INDEX ERROR - MAIN ) ingrese nuevamente un dato valido "