import os
from time import sleep

def varia_tam_amostra(intervalo, tamanho, algoritmo):
    for i in range(1,tamanho,intervalo):

        for e in range(1,5):
            print('java –cp bin MedidorDeOrdenacao '+str(algoritmo)+' '+str(i)+
                      ' 1400000 > varia-tam-amostra/'+str(algoritmo)+'/'+
                      str(algoritmo)+'_tamanho_'+str(i)+'_teste_'+str(e)+'.txt')
            os.system('java –cp bin MedidorDeOrdenacao '+str(algoritmo)+' '+str(i)+
                      ' 1400000 > varia-tam-amostra/'+str(algoritmo)+'/'+
                      str(algoritmo)+'_tamanho_'+str(i)+'_teste_'+str(e)+'.txt')
            sleep(2)

varia_tam_amostra(1,5,'quick')
