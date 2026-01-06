with open("quijote.txt", encoding="utf-8", mode="rt") as archi, open("quijoteej1.txt", encoding="utf-8", mode="wt") as salida:
    for renglon in archi:
        if len(renglon.strip())==0:
            renglonVacio=True

        if not renglonVacio:
            salida.write(renglon)

# Martu: Fijate qué pasa si ejecutás el programa, ¿qué sucede con el archivo de salida? Rehacer :p!!
