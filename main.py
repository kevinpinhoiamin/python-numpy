import numpy as np
import time
# Importando para do pacote
# from numpy import arange

# Lista com tamanho determinado
print(np.arange(10))

# Criar array numpy a partir de uma lista
km = np.array([1000, 2300, 4987, 1500])
print(km)
print(type(km))
print(km.dtype)

# Criar array numpy a partir de dados externos
km = np.loadtxt(fname='data/carros-km.txt', dtype=int)
print(km)
print(km.dtype)

# Arrays com duas dimensões
dados = [
    ['Rodas de liga', 'Travas elétricas', 'Piloto automático', 'Bancos de couro', 'Ar condicionado', 'Sensor de estacionamento', 'Sensor crepuscular', 'Sensor de chuva'],
    ['Central multimídia', 'Teto panorâmico', 'Freios ABS', '4 X 4', 'Painel digital', 'Piloto automático', 'Bancos de couro', 'Câmera de estacionamento'],
    ['Piloto automático', 'Controle de estabilidade', 'Sensor crepuscular', 'Freios ABS', 'Câmbio automático', 'Bancos de couro', 'Central multimídia', 'Vidros elétricos']
]
Acessorios = np.array(dados)
print(Acessorios)
print(km.shape)
print(Acessorios.shape)

# Comparando desempenho com listas
np_array = np.arange(1000000)
py_list = list(range(1000000))

start_time = time.time()
for _ in range(100):
    np_array *= 2
print("--- {} seconds ---".format(time.time() - start_time))

start_time = time.time()
for _ in range(100):
    py_list = [x * 2 for x in py_list]
print("--- {} seconds ---".format(time.time() - start_time))

# Operações aritiméticas com arrays numpy
km = np.array([44410., 5712., 37123., 0., 25757.])
anos = np.array([2003, 1991, 1990, 2019, 2006])

idade = 2019 - anos
print(idade)

# Operações entre arrays
km_media = km / idade
print(km_media)

print(44410 / (2019 - 2003))
print(5712 / (2019 - 1991))

# Operaçoes com arrays com duas dimensões
dados = np.array([km, anos])
print(dados)
print(dados.shape)
print(dados[0])
print(dados[1])
km_media = dados[0] / (2019 - dados[1])
print(km_media)

# Indexação
contador = np.arange(10)
print(contador)
print(contador[0])
item = 6
index = item - 1
print(contador[index])
print(contador[-1])
print(dados[0])
print(dados[1])
print(dados[1][2])
print(dados[1, 2])

# Fatiamento
print(contador[1:4])
print(contador[1:8:2])
print(contador[::2])
print(contador[1::2])
print(dados)
print(dados[:, 1:3])
print(dados[:, 1:3][0] / (2019 - dados[:, 1:3][1]))

# Indexação com array booleano
print(contador)
print(contador > 5)
print(contador[contador > 5])
print(dados)
print(dados[1] > 2000)
print(dados[:, dados[1] > 2000])
print(dados[:, dados[1] > 2000][0] / (2019 - dados[:, dados[1] > 2000][1]))

# Atributos e métodos de arrays numpy
print(dados)
print(dados.shape)
print(dados.ndim)
print(dados.size)
print(dados.dtype)
print(dados.T)
print(dados.transpose())

print(dados.tolist())
print(contador)
print(contador.reshape((5, 2)))
print(contador.reshape((5, 2), order='C'))
print(contador.reshape((5, 2), order='F'))
km = [44410., 5712., 37123., 0., 25757.]
anos = [2003, 1991, 1990, 2019, 2006]
info_carros = km + anos
print(info_carros)
print(np.array(info_carros).reshape((2, 5)))
print(np.array(info_carros).reshape((5, 2), order='F'))
dados_new = dados.copy()
print(dados_new)
dados_new.resize((3, 5), refcheck=False)
print(dados_new)
dados_new[2] = dados_new[0] / (2019 - dados_new[1])
print(dados_new)

# Estatísticas com arrays numpy
anos = np.loadtxt(fname='data/carros-anos.txt', dtype=int)
km = np.loadtxt(fname='data/carros-km.txt')
valor = np.loadtxt(fname='data/carros-valor.txt')
print(anos.shape)
dataset = np.column_stack((anos, km, valor))
print(dataset)
print(dataset.shape)
print(np.mean(dataset, axis=0))
# print(np.mean(dataset, axis=1))
print(np.mean(dataset[:, 1]))
print(np.mean(dataset[:, 2]))
print(np.std(dataset[:, 2]))
print(dataset.sum(axis=0))
print(dataset[:, 1].sum(axis=0))
print(np.sum(dataset, axis=0))
print(np.sum(dataset[:, 2], axis=0))
