#!/usr/bin/env python
# coding: utf-8

# ### O que precisamos:
# 
# - Quase sempre você precisa de uma conta para consumir uma API. Algumas APIs são abertas, como a https://docs.awesomeapi.com.br/api-de-moedas , mas em muitos casos vamos precisar ter uma conta ativa para consumir a API
# 

# #### Pegar a Cotação Atual de Todas as Moedas 

# In[9]:


import requests
import json

cotacoes = requests.get('https://economia.awesomeapi.com.br/json/all')
cotacoes_dic = cotacoes.json()
#print (cotacoes_dic)


# #### Qual foi a última cotação do Dólar, do Euro e do BitCoin? 

# In[10]:


print('Dólar: {}'.format(cotacoes_dic['USD']['bid']))
print('Euro: {}'.format(cotacoes_dic['EUR']['bid']))
print('BitCoin: {}'.format(cotacoes_dic['BTC']['bid']))


# #### Pegar a cotação dos últimos 30 dias do dólar (Sua resposta vai dar diferente do gabarito, porque estamos rodando o código em momentos diferentes, mas o seu código deve ser o mesmo/parecido)

# In[11]:


cotacoes_dolar30d = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/30')
cotacoes_dolar_dic = cotacoes_dolar30d.json()
#print(cotacoes_dolar_dic[0]['bid'])
lista_cotacoes_dolar = [float (item['bid'])for item in cotacoes_dolar_dic]
print (lista_cotacoes_dolar)


# #### Pegar as cotações do BitCoin de Jan/20 a Out/20

# In[12]:


cotacoes_bt = requests.get('https://economia.awesomeapi.com.br/json/daily/BTC-BRL/200?start_date=20200101&end_date=20201031')
cotacoes_bt_dic = cotacoes_bt.json()
#print(cotacoes_bt_dic)
lista_cotacoes_bt = [float (item['bid'])for item in cotacoes_bt_dic]
#reverter a lista 
lista_cotacoes_bt.reverse()
#print(lista_cotacoes_bt)
#print(len(lista_cotacoes_bt))


# #### Gráfico com as cotações do BitCoin

# In[14]:


import matplotlib.pyplot as plt

plt.figure(figsize=(15, 5))
plt.plot(lista_cotacoes_bt)
plt.show()

