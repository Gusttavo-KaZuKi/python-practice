import time

produtos = ['banana', 'maca', 'melao', 'abacaxi']
preco = [2, 5, 20, 17]
minimo = 15


# for i, produto in enumerate(produtos):
#     if preco[i] < minimo:
#         print(preco[i], produto)
        

# for i, produto in enumerate(produtos):
#     print(i, produto)
    
    
# for i, produto in enumerate(produtos):
#     print(i, preco[i])
        

# for produto in produtos:
#     if produto == 'maca':
#         continue
#     print(produto)
    
    
# for produto in produtos:
#     if produto == 'banana':
#         continue
#     elif produto == 'melao':
#         break
#     print(produto)
        
        
# for produto in produtos:
#     if produto == 'maca':
#         break
#     print(produto)


# for i in range(10, -1, -1):
#     print(i)
#     time.sleep(1)
# print('Os fogos começaram!!!')


#     range(começo da contagem, final da contagem, intervalo)


# for i in range(1, 50):
#     if i % 2 == 0:
#         print(i, end=' ')
# print('Acabou')


# num = 0
# for i in range(1, 500):
#     if i % 2 == 1:
#         if i % 3 == 0:
#             num += i            
# print('A soma de todos os números ímpares múltiplos de 3, no intervalo de 1 a 500 é de {}'.format(num))


# user_num = int(input('Digite um número: '))
# for i in range(1, 11):
#     print('{}x{} = {}'.format(i, user_num, i*user_num))


num = 0
cont = 0
for i in range(6):
    user_num = int(input('Digite um número: '))
    if user_num % 2 == 0:
        num += user_num
        cont += 1
print('Você informou {} números pares e a soma de todos os números foi de: {}'.format(cont, num))