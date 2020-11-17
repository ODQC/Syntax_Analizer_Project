#Proyecto 2 de Estructuras  de Datos
# Por: Oscar Quesada

varTable= dict()
typeVar = {'void':0,'int':0,'float':0,'string':0}
symbolTable = {'if':0,'while':0,'(':0,')':0,'{':0,'}':0,'=':0,';':0,'+':0,'-':0,'<':0,'>':0,'*':0,'/':0,',':0}


def printElement(element):
    print
    element
def OpenFile():
    linea = 1
    anterior = ""
    file_object = open("Mycode.txt", "r")
    if file_object.mode =="r":
    # reading each line
        for line in file_object:
            linea + 1
        # reading each word
            for word in line.split():
                # verifica si la palabra es numero entero, flotante o string
                if word.isnumeric() or VerifyFloat(word) or VerifyString(word):
                    anterior = word
                #si la palabra anterior es un tipo de variable o la palabra actual ya fue declarada
                elif anterior in typeVar or word in varTable:
                    varTable[word] = 1
              #si la parabra es un tipo de variable
                elif word in typeVar:
                    typeVar[word] = typeVar[word] + 1
               #si la palabra es algún simbolo
                elif word in symbolTable:
                    symbolTable[word] = symbolTable[word] + 1
                else:
                    print("Error en la linea: "+str(linea)+" la variable "+word+" no fue declarada")
                anterior = word
            # displaying the word
           # print(word)
       # for key in list(symbolTable.keys()):
        #    print(key, ":", symbolTable[key])
    else:
        print('no se pudo abrir el archivo')
# verifica que haya igual cantidad de llaves abiertas que cerradas
def VerifySymbols():
    if symbolTable['{'] == symbolTable['}']:

        if symbolTable['('] == symbolTable[')']:
            return True
    else:
        return False
# verifica si un string tiene formato de float
def VerifyFloat(potential_float):
    try:
        float(potential_float)
        return True
    except ValueError:
        return False
# verifica si una para es de tipo string
def VerifyString(word):
    firstChar = word[0]
    lastChar = word[-1]

    if firstChar =='“' and lastChar == '”':
        return True
    else:
        return False

OpenFile()
error = "No se encontró error de sintaxis " if VerifySymbols() else"Error de sintaxis"
print(error)
print(varTable)
print(typeVar)
print(symbolTable)