
def syt(knumerot):

    numerot = knumerot.split(';')

    try:

        while float(numerot[0]) % float(numerot[1]) != 0:

            tempnumero = float(numerot[1])
            numerot[1] = float(numerot[0]) % float(numerot[1])
            numerot[0] = tempnumero
        
        print(numerot[1])
        
    except: print("\nJotain meni rikki!")



def root(numerot):

    a = numerot.split(';')

    print(float(a[0])**(1/float(a[1])))



def plusmiinus(teksti):
    

    kirjaimet = [kirjain for kirjain in teksti]
    
    for i in kirjaimet:
        
        match i:
            case '+':
                luku = teksti.split('+')
                for i in range(len(luku)-1):
                    luku[i+1] = float(luku[i])+float(luku[i+1])
                print(luku[-1])
                break
            case '-':
                luku = teksti.split('-')
                for i in range(len(luku)-1):
                    luku[i+1] = float(luku[i])-float(luku[i+1])
                print(luku[-1])
                break
            case '*':
                luku = teksti.split('*')
                for i in range(len(luku)-1):
                    luku[i+1] = float(luku[i])*float(luku[i+1])
                print(luku[-1])
                break
            case '/':
                luku = teksti.split('/')
                for i in range(len(luku)-1):
                    luku[i+1] = float(luku[i])/float(luku[i+1])
                print(luku[-1])
                break
            case '^':
                luku = teksti.split('^')
                for i in range(len(luku)-1, 0, -1):
                    luku[i-1] = float(luku[i-1])**float(luku[i])
                print(luku[0])
                break
            
        
    if len(luku) == 1:
        print("\nJotain meni rikki!")

                
            




def main():

    while True:

        lista = {
            'syt' : '\nSuurin yhteinen tekijä, syt(a;b)',
            'sqrt' : 'Neliöjuuri, sqrt(x)',
            'root' : 'Juuri, root(x;n)',
        }

        kauha = input('\n')
        if kauha == 'POIS':
            break
        elif kauha == 'APUA':
            for i in lista:
                print(lista[i])
        else:
            try:

                
                if any(i in kauha for i in lista):
                
                    juhku = kauha.split('(')
                    juhis = juhku[1].split(')')[0]           
            
                    match juhku[0]:
                        case 'syt':
                            syt(juhis)
                        case 'sqrt':
                            print(float(juhis)**0.5)
                        case 'root':
                            root(juhis)
                else: plusmiinus(kauha)

                
                    
                

            except: print("\nJotain meni rikki!")
        
print("Kirjoita 'POIS' poistuaksesi.\n'APUA' komennolla näet komennot.\n")
main()