
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
    

    cheese = []
    

    merkit = [
        '^', 
        '*', 
        '/', 
        '+',
        '-'
    ]


    karhu = teksti

    for a in merkit:

        karhu = karhu.split(a)

        for i in range(len(karhu)-1):

            karhu.insert(i*2+1,a)

        karhu = ' '.join(karhu)
        

    karhu = karhu.split(' ')

    for n in range(len(merkit)):
        cheese.append([])
    
        for m in range(len(karhu)):
            if merkit[n] == karhu[m]:
                
                cheese[n].append(m)
                
    

    
    for i in range(len(cheese[0])-1,-1,-1):
        karhu[cheese[0][i]-1] = float(karhu[cheese[0][i]-1])**float(karhu[cheese[0][i]+1])
        del karhu[cheese[0][i]:cheese[0][i]+2]
    
        
    


 
    for c in range(len(cheese[1])+len(cheese[2])):         
        
        if '*' in karhu and '/' in karhu:
            if karhu.index('*') < karhu.index('/'):
                duh = karhu.index('*')
            else: duh = karhu.index('/')
        elif '*' not in karhu:
            duh = karhu.index('/')
        else:
            duh = karhu.index('*')
        

        if karhu[duh] == '*':
            karhu[duh-1] = float(karhu[duh-1]) * float(karhu[duh+1])  
            del karhu[duh:duh+2]
        elif karhu[duh] == '/':
            karhu[duh-1] = float(karhu[duh-1]) / float(karhu[duh+1])  
            del karhu[duh:duh+2]


    for d in range(len(cheese[3])+len(cheese[4])):

        if '+' in karhu and '-' in karhu:
            if karhu.index('+') < karhu.index('-'):
                duf = karhu.index('+')
            else: duf = karhu.index('-')
        elif '+' not in karhu:
            duf = karhu.index('-')
        else:
            duf = karhu.index('+')


        if karhu[duf] == '+':
            karhu[duf-1] = float(karhu[duf-1]) + float(karhu[duf+1])  
            del karhu[duf:duf+2]
        elif karhu[duf] == '-':
            karhu[duf-1] = float(karhu[duf-1]) - float(karhu[duf+1])  
            del karhu[duf:duf+2]
    if float(karhu[0])==int(karhu[0]):
        print(int(karhu[0]))
    else: print(float(karhu[0]))



  
                
            




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