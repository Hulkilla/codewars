import numpy as np

string = "01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17"

def stat(strg):
    if strg == '':
        return ''
    else: 
        lista = strg.split(sep = ", ")
        numeros, segundos = [], []

        for i in range(len(lista)):
            numeros.append(lista[i].split(sep = "|"))
            for j in range(len(numeros[i])):
                numeros[i][j] = int(numeros[i][j])

        for i in range(len(numeros)):
            segundos.append(numeros[i][0] * 3600 + numeros[i][1] * 60 + numeros[i][2])


        rango = max(segundos) - min(segundos)
        mean = int(np.average(segundos))
        median = int(np.median(segundos))

        def segundos_horas(segundos):
            horas = int(segundos / 3600)
            segundos -= horas*3600
            minutos = int(segundos/60)
            segundos -= minutos*60
            return f"{horas:02d}|{minutos:02d}|{segundos:02d}"


        return(f"Range: {segundos_horas(rango)} Average: {segundos_horas(mean)} Median: {segundos_horas(median)}")

print(stat(string))