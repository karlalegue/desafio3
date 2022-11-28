archivo =open(input ("Ingrese el nombre de su archivo: "))
lineas =archivo.read()
lineas= lineas.replace ("\n", "")
lineas= lineas.replace ("T", "U")
print (lineas)

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
    
codon_inicio = ["A", "U", "G"]
codon_final = "STOP"

sequence_proteina = ""

for i in range (0, len(lineas),3):
    if codon_inicio [0]==archivo[i] and codon_inicio [1] == archivo[i+1] and codon_inicio [2]== archivo[i+2]: 
        codones = lineas[i:i+3]
        sequence_proteina= sequence_proteina+tabla_codones[codones]
    print (sequence_proteina)



archivo.close()

arch= open ("SEQUENCE_1_PROTEINA", "w")
arch.write (sequence_proteina)
arch.close()

