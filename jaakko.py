
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
        '+', 
        '-', 
        '*', 
        '/',
        '^'
    ]


    karhu = teksti

    for a in merkit:

        karhu = karhu.split(a)

        for i in range(len(karhu)-1):

            karhu.insert(i*2+1,a)

        karhu = ' '.join(karhu)
        

    karhu = karhu.split(' ')

    # for n in range(len(merkit)):
    #     cheese.append(0)
    #     for m in karhu:
    #         if merkit[n] == m:
    #             cheese[n] = int(cheese[n])+1
        
    # print(cheese)
    cheese = karhu.copy()
    
    for b in range(len(karhu),0,-1):

        if karhu[b-1] == '^':

            karhu[b-2] = float(karhu[b-2])**float(karhu[b])

            del karhu[b-1:b+1]
    print(cheese)
    for c in range(len(karhu)):
        
        print(c)
        print(karhu[7])
        if karhu[c] == '*':
            karhu[c-1] = float(karhu[c-1])*float(karhu[c+1])
            del karhu[c:c+2]
        elif karhu[c] == '/':
            karhu[c-1] = float(karhu[c-1])/float(karhu[c+1])
            del karhu[c:c+2]

    print(karhu)



    
    # kameli = []
    
    
    # if '^' in teksti:
    #     jaakko = teksti.split('^')
        
    
    # jaettui = []

    # for i in jaakko:
       
        

    #     tuomas = []
        
    #     for a in merkit:
            
    #         if a in i:
    #             tuomas.append(a)
        

        
    #     # print(tuomas)
    #     # print(len(tuomas))
    #     if len(tuomas) > 0:

    #         kahvi = []

    #         # print(jaettui)
    #         # print(jaakko.index(i))
    #         for b in range(len(tuomas)):

    #             jaettui.append(i.split(tuomas[b]))
    #             jaettui[jaakko.index(i)-1].append(jaettui[jaakko.index(i)-1][1])
    #             jaettui[jaakko.index(i)-1][1] = tuomas[b]
    #         print(jaettui)
            
        
    #         for c in range(len(jaettui)):

    #             kahvi.append(len(jaettui[c][0])) 
    #         # print('j')
    #         # print(kahvi)
            
    #         kameli.append(jaettui[kahvi.index(min(kahvi))][0])
    #         kameli.append(jaettui[kahvi.index(min(kahvi))][1])

    #         if len(jaettui[kahvi.index(min(kahvi))]) > 2:

    #             kameli.append(jaettui[kahvi.index(min(kahvi))][2])
        
    #     else: kameli.append(i)
    
    # print(kameli)

    # kirjaimet = [kirjain for kirjain in teksti]
    
    # print(kirjaimet)

    # for i in kirjaimet:
        
    #     match i:
    #         case '+':
    #             luku = teksti.split('+')
    #             for i in range(len(luku)-1):
    #                 luku[i+1] = float(luku[i])+float(luku[i+1])
    #             print(luku[-1])
    #             break
    #         case '-':
    #             luku = teksti.split('-')
    #             for i in range(len(luku)-1):
    #                 luku[i+1] = float(luku[i])-float(luku[i+1])
    #             print(luku[-1])
    #             break
    #         case '*':
    #             luku = teksti.split('*')
    #             for i in range(len(luku)-1):
    #                 luku[i+1] = float(luku[i])*float(luku[i+1])
    #             print(luku[-1])
    #             break
    #         case '/':
    #             luku = teksti.split('/')
    #             for i in range(len(luku)-1):
    #                 luku[i+1] = float(luku[i])/float(luku[i+1])
    #             print(luku[-1])
    #             break
    #         case '^':
    #             luku = teksti.split('^')
    #             for i in range(len(luku)-1, 0, -1):
    #                 luku[i-1] = float(luku[i-1])**float(luku[i])
    #             print(luku[0])
    #             break
            
        
    # if len(luku) == 1:
    #     print("\nJotain meni rikki!")

                
            




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
            #try:

                
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

                
                    
                

           # except: print("\nJotain meni rikki!")
        
print("Kirjoita 'POIS' poistuaksesi.\n'APUA' komennolla näet komennot.\n")
main()