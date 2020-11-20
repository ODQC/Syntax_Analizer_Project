#Proyecto 2 de Estructuras  de Datos
# Por: Oscar Quesada
import re
varTable= dict()
typeVar = {'void':0,'int':0,'float':0,'string':0}
symbolTable = {'return':0, 'if':0,'while':0,'(':0,')':0,'{':0,'}':0,'=':0,';':0,'+':0,'-':0,'<':0,'>':0,'*':0,'/':0,',':0}



def printElement(element):
    print
    element
def OpenFile():
    numline = 0
    anterior = ""
    posterior = ""
    currentFunc = ""
    file_object = open("Mycode.txt", "r")
    if file_object.mode =="r":
    # reading each line
        try:
            for line in file_object:

                li = list(line.split())

                numline += 1
                for word in line.split():
                    pos = li.index(word)

                #print(pos)
                    try:
                        anterior = li[pos-1]
                        posterior = li[pos+1]
                    except IndexError:
                        pass
                # verifica si la palabra es numero entero, flotante o string
                    if isFunction(anterior,posterior):
                        varTable[word] = {'Tipo':'Metodo','Retorno':anterior,'Alcance':'Global'}
                #si la palabra anterior es un tipo de variable o la palabra actual ya fue declarada
                    elif isVar(word) or  word in varTable:
                        pass
                    elif word in typeVar:
                        typeVar[word] = typeVar[word]+1
                    elif anterior in typeVar:
                        insertVar(word,anterior)
                #si la palabra es algún simbolo
                    elif word in symbolTable:
                        symbolTable[word] = symbolTable[word] + 1
                    elif anterior == "return":
                        VerifyReturn(currentFunc,word)

                    else:
                        print("Error en la linea: "+str(numline)+" la variable "+word+" no fue declarada")

        except ValueError:
            print(ValueError)
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
    elif firstChar =="'" and lastChar == "'":
        return True
    else:
        return False

def isFunction(anterior,posterior):
    val = True if posterior == "(" else False
    if anterior == "void" and val:
        return True
    elif anterior == "String" and val:
        return True
    elif anterior == "Float" and val:
        return True
    elif anterior == "int" and val:
        return True
    else:
        return False

def VerifyReturn(meth,word):
    if word in typeVar and VerifySymbols():
       if typeVar[meth]['Retorno'] == typeVar[word]['Retorno']:
           return True
       else:
           print("El metodo retorna una varible de diferente tipo ")
           return False
    else:
        return False
        print("Error de sintaxis")

def insertVar(word,valor):
    if VerifySymbols():
        varTable[word] = {'Tipo': 'Variable', 'Retorno': valor, 'Alcance': 'Global'}
    else:
        varTable[word] = {'Tipo': 'Variable', 'Retorno': valor, 'Alcance': 'Local'}
def isVar(word):
    yes = True
    if word.isnumeric():
        insertVar(word, "int")
    elif VerifyFloat(word):
        insertVar(word, "float")
    elif VerifyString(word):
        insertVar(word, "String")
    else:
        yes = False
    return yes

OpenFile()
error = "No se encontró error de sintaxis " if VerifySymbols() else"Error de sintaxis"
print(error)
print(varTable)
print(typeVar)
print(symbolTable)