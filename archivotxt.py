with open("quijote.txt", encoding="utf-8", mode="rt") as archi, open("quijoteej1.txt", encoding="utf-8", mode="wt") as salida:
    for renglon in archi:
        if len(renglon.strip())==0:
            renglonVacio=True

        if not renglonVacio:
            salida.write(renglon)
#pq no m abre el archivo quijote.txt??
#despues de eso creo que el resto esta bien
#(si abriera el archivo obvio)