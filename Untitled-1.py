correo = "hola@gmail.com"

if '@' in correo:
    if '.' in correo:
        x = correo.split("@",1)
        idc = x[0]
        x = x[1].split(".",1)
        dom = x[0]
        tipdom = x[1]
    else: print("direccion invalida")
else: print("direccion invalida")
