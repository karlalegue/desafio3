archivo =open(input ("Ingrese el nombre de su archivo: "))
nombre = archivo.readline()
lineas =archivo.read()
lineaslimpia = ""
lineas= lineas.replace ("T", "U")


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
    
menu = input ("1. Para leer archivo Fasta y generar secuencia de proteina, ingrese 1\n2. Para obtener estadísticas de la secuencia, ingrese 2. \n3. Para generar diagrama de relación de aminoácido, ingrese 3")

codon_inicio = ["A", "U", "G"]
codon_final = "STOP"

##Paso 1$$
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

## Paso 2

codones = ""
i = 0
while i< len(lineaslimpia)-2:
    if codon_inicio [0]==lineaslimpia[i] and codon_inicio [1] == lineaslimpia[i+1] and codon_inicio [2]== lineaslimpia[i+2]: 
       while i< len(lineaslimpia)-2:
            codones = codones + lineaslimpia[i:i+3]
            i = i + 3
    i = i + 1
print(codones)

##Paso 3
sequence_proteina = ""
for i in range (0, len(codones),3):
    codon = codones[i]+codones[i+1]+codones[i+2]
    sequence_proteina= sequence_proteina+tabla_codones[codon]
print (sequence_proteina)


archivo.close()
'''
arch= open ("SEQUENCE_1_PROTEINA", "w")
arch.write (sequence_proteina)
arch.close()
'''
