'''
como fritar batata frita

escrevendo o passo a passo:

1: recorte a casca da batata
2: lave a batata
3: corte a batata em pedaços
4: coloque na air fryer
5: espere 20 a 25 minutos a 200°C

agora simplifique:

'''
import time
import time
import time
import time
import time
import time
import time
import time
import time
import time
import time

# o import time (e a quantidade de quantos tem) deixa em cada print, um time de 5 segundos.

def fritar_batata_frita(porção):
    print('\n','-' * 35)
    print('\n🍟 Fritando Batata - Sistema Simples - em sessão do usuário 👤 🍟\n') #teste de desenvolvedor.
    time.sleep(2)
    print("1. Pegue a batata, uma faca e uma airfryer.")
    time.sleep(5)
    print("2. Descasque a batata com a faca.")
    time.sleep(5)
    print("3. Lave a batata na água.")
    time.sleep(5)
    print("4. corte a batata em vários pedaços em formato retângulo.")
    time.sleep(5)
    print("5. com os pedaços cortados, abra a airfryer e coloque os pedaços.")
    time.sleep(5)
    print("6. jogue um pouco de sal na panela da airfryer com as batatas dentro.")
    time.sleep(5)
    print("7. feche a airfryer e coloque a 200°C")
    time.sleep(5)
    print("8. espere 20 a 25 minutos.")
    time.sleep(5)
    print("9. quando pronto, abra a airfryer e pegue com cuidado a batata frita.")
    time.sleep(5)
    print("10. pronto, pode comer :)")
    time.sleep(5)
    
    
    if porção.lower() == 'uma porção':
        resultado = 'batata frita com porção pequena!'
    
    elif porção.lower() == 'duas porções':
        resultado = 'batata frita com porção média!.'
 
    else:
        resultado = 'batata frita com porção grande!' 
    
    return resultado
print('-' * 35 , '\n') #teste de desenvolvedor.
porcao_escolhida = input('Antes do tutorial, quantas porções você quer colocar? uma porção, duas porções ou três porçôes? R: ')
porcao_escolhida = fritar_batata_frita(porcao_escolhida)
print(f'\nmeu lanche vai ser : {porcao_escolhida}\n')
print('-' * 35 , '\n')