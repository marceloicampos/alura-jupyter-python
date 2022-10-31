from collections import namedtuple

name = input('Qual o seu nome ? ')
age = input('Qual a sua idade ? ')
weight = input('Qual o seu peso ? ')
print('Nome: ', name, ' Idade: ', age, ' Peso: ', weight)
p = input('Digite Primeiro Número de 0 a 9: ')
s = input('Digite Segundo Número de 0 a 9: ')
print(f'A soma de {s} + {p} é igual a:', int(p)+int(s))
print('Hello {}'.format(name))

coordenadas = [-23.588254, -46.632477]
coordenadas[1] = -5.0
print(coordenadas)
print(type(coordenadas))
marcelo_coordenadas = (-23.588254, -46.632477)
print(marcelo_coordenadas)
print(type(marcelo_coordenadas))
print(id(marcelo_coordenadas))  # TUPLAS DIFERENTES
marcelo_coordenadas += (-5,)
print(marcelo_coordenadas)
print(id(marcelo_coordenadas))  # TUPLAS DIFERENTES
minha_tupla = ([1, 2, 3], ['a', 'b', 'c'])
print(minha_tupla)
print(id(minha_tupla))  # TUPLAS IGUAIS, MAS CONTEÚDOS DIFERENTES
minha_tupla[1].append('d')
print(minha_tupla)
print(id(minha_tupla))  # TUPLAS IGUAIS, MAS CONTEÚDOS DIFERENTES
maps_x_y = ('coordenação', ['1', '2'])
print(maps_x_y)
maps_z_w = namedtuple('coordenação', ['z', 'w'])
maps_tuple = maps_z_w(1, 2)
print(maps_tuple)
print(maps_tuple[0])
print(maps_tuple.z)
print(maps_tuple[1])
print(maps_tuple.w)
telefones = ['1234-5678', '9999-9999', '8765-4321', '8877-7788']
contato = ('Yan', '1234-5678')
print(telefones)
print(contato)
contatos_lista = [('Yan', '1234-5678'), ('Pedro', '9999-9999'),
                  ('Ana', '8765-4321'), ('Marina', '8877-7788')]
print(contatos_lista)
print(contatos_lista[3][1])
contatos_dicinario = {'Yan': '1234-5678'}
print(type(contatos_dicinario))
contatos_dict = {'Yan': '1234-5678', 'Pedro': '9999-9999',
                 'Ana': '8765-4321', 'Marina': '8877-7788'}
print(type(contatos_dict))
print(contatos_dict['Ana'])
print(contatos_dict.get('João', 'Contato não encontrado'))
print('Yan' in contatos_dict)
print('9999-9999' in contatos_dict)
print('9999-9999' in contatos_dict.values())
contatos_dict['João'] = '8887-7778'
print(contatos_dict)
del contatos_dict['Marina']
print(contatos_dict)
meus_contatos_novo = {nome: '9' + contatos_dict[nome] for nome in contatos_dict}
print(meus_contatos_novo)
valores = meus_contatos_novo.values()
print(valores)
valores = meus_contatos_novo.values()
print(valores)
meus_contatos_novo['Yan'] = '91122-3344'
print(valores)
