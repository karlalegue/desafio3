tabla_codones={           
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A", "CGU": "R",
    "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "AAU": "N", "AAC": "N", "GAU": "D", "GAC": "D", "UGU": "C",
    "UGC": "C", "CAA": "Q", "CAG": "Q", "GAA": "E", "GAG": "E",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G", "CAU": "H",
    "CAC": "H", "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "START",
    "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L",
    "CUG": "L", "AAA": "K", "AAG": "K", "AUG": "M", "UUU": "F",
    "UUC": "F", "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S",
    "AGC": "S", "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "UGG": "W", "UAU": "Y", "UAC": "Y", "GUU": "V", "GUC": "V",
    "GUA": "V", "GUG": "V", "UAG": "STOP", "UGA": "STOP", "UAA": "STOP"}
    
menu =int(input ("1. Para leer archivo Fasta y generar secuencia de proteina, ingrese 1\n2. Para obtener estadísticas de la secuencia, ingrese 2. \n3. Para generar diagrama de relación de aminoácido, ingrese 3.\n4.Para salir, ingrese 4: "))


##Paso 1##
while menu !=4: 
    if menu == 1: 
        archivo =open(input ("Ingrese el nombre de su archivo: "))
        nombre = archivo.readline()
        lineas =archivo.read()
        lineaslimpia = ""
        codon_inicio = ["A", "U", "G"]
        lineas= lineas.replace ("T", "U")
        print (lineas)
        i = 0
        while i < len(lineas):
            if lineas[i]=='I':
                while lineas[i]!='F':
                    i = i + 1
            else:
                lineaslimpia = lineaslimpia + lineas[i]
            i= i + 1
        print (lineaslimpia)

        codones = ""
        i = 0
        while i< len(lineaslimpia)-2:
            if codon_inicio [0]==lineaslimpia[i] and codon_inicio [1] == lineaslimpia[i+1] and codon_inicio [2]== lineaslimpia[i+2]: 
                while i< len(lineaslimpia)-2:
                    codones = codones + lineaslimpia[i:i+3]
                    i = i + 3
            i = i + 1
        print(codones)

        sequence_proteina = ""
        for i in range (0, len(codones),3):
            codon = codones[i]+codones[i+1]+codones[i+2]
            sequence_proteina= sequence_proteina+tabla_codones[codon]
        print (sequence_proteina)
    menu =int(input ("1. Para leer archivo Fasta y generar secuencia de proteina, ingrese 1\n2. Para obtener estadísticas de la secuencia, ingrese 2. \n3. Para generar diagrama de relación de aminoácido, ingrese 3.\nPara salir, ingrese 4: "))
    if menu == 2: 
        #Nuumero y porcentaje de nucleotidos (A,C,U,G) por secuencia valida.
        total_nucleotidos= 0
        nucleotido_A= 0
        nucleotido_C = 0
        nucleotido_U = 0
        nucleotido_G = 0
        for i in codones:
            if i== "A":
                nucleotido_A= nucleotido_A+1
            elif i== "C":
                nucleotido_C= nucleotido_C+1
            elif i== "U":
                nucleotido_U = nucleotido_U+1
            elif i== "G":
                nucleotido_G = nucleotido_G+1

            total_nucleotidos = (nucleotido_A+nucleotido_C+nucleotido_U+nucleotido_G)
            porcentaje_A= (nucleotido_A*100)/total_nucleotidos
            porcentaje_C = (nucleotido_C*100)/total_nucleotidos
            porcentaje_U = (nucleotido_U*100)/total_nucleotidos
            porcentaje_G = (nucleotido_G*100)/total_nucleotidos
        print ("La cantidad de nucleotidos A es de", nucleotido_A, "y su porcentaje es de",(porcentaje_A), "%" "\nLa cantidad de nucleotidos C es de", nucleotido_C, "y su porcentaje es de", (porcentaje_C), "%" "\nLa cantidad de nucleotidos U es de", nucleotido_U, "y su porcentaje es de",(porcentaje_U), "%" "\nLa cantidad de nucleotidos G es de", nucleotido_G, "y su porcentaje es de", (porcentaje_G), "%" "\nLa cantidad total de nucleotidos es de", total_nucleotidos)
        ###Numero y porcentaje de codones por secuencia válida
        codones_encontrados = 0
        i = 0
        while i< len(codones)-2:
            codones_encontrados = codones_encontrados +1 
            i = i +3
        porcentaje_codones_encontrados = 100/ (codones_encontrados)
        print ("La cantidad de codones encontrados es", codones_encontrados, "y su porcentaje es", porcentaje_codones_encontrados)
        ##NUMERO DE AMINOACIDOS##
        polares_sin_carga = 0 
        polares_con_carga_positiva= 0
        polares_con_carga_negativa = 0
        apolares = 0
        for i in codones:  
            if i == "S" or i == "T" or i == "C" or i == "Y" or i == "N" or i == "Q":
                polares_sin_carga = polares_sin_carga+1
            if i == "H" or i == "R" or i == "K":
                polares_con_carga_positiva = polares_con_carga_positiva +1
            if i == "D" or i == "E":
                polares_con_carga_negativa = polares_con_carga_negativa +1
            if i == "G" or i == "A" or i == "V" or i == "L" or i == "I" or i == "F" or i == "W" or i == "M" or i == "P":
                apolares = apolares+1
        print ("La cantidad de polares sin carga es de", polares_sin_carga,"\nLa cantidad de polares con carga positiva es de", polares_con_carga_positiva,"\nLa cantidad de polares con carga negativa es de", polares_con_carga_negativa,"\nLa cantidad de apolares es de", apolares)
print ("Ha cerrado la sesión")



'''
arch= open ("SEQUENCE_1_PROTEINA", "w")
arch.write (sequence_proteina)
arch.close()
'''





