#!/usr/bin/env python
# coding: utf-8

# #### Pegar a Cotação Atual de Todas as Moedas 

# In[ ]:


import requests
import json

cotacoes = requests.get('https://economia.awesomeapi.com.br/json/all')
dic_cotacoes = cotacoes.json()
print(dic_cotacoes)


# #### Qual foi a última cotação do Dólar, do Euro e do BitCoin? (Sua resposta vai dar diferente do gabarito, porque estamos rodando o código em momentos diferentes, mas o seu código deve ser o mesmo/parecido)

# In[ ]:


cotacoes = requests.get('https://economia.awesomeapi.com.br/json/all')
dic_cotacoes = cotacoes.json()

print('Dolar: {}'.format(dic_cotacoes['USD']['bid']))
print('Euro: {}'.format(dic_cotacoes['EUR']['bid']))
print('BitCoin: {}'.format(dic_cotacoes['BTC']['bid']))


# #### Pegar a cotação dos últimos 30 dias do dólar (Sua resposta vai dar diferente do gabarito, porque estamos rodando o código em momentos diferentes, mas o seu código deve ser o mesmo/parecido)

# In[ ]:


cotacoes_dolar = requests.get(' https://economia.awesomeapi.com.br/json/daily/USD-BRL/100')
dic_cotacoes = cotacoes_dolar.json()

dic_USD_BRL_30 = [float(item['bid']) for item in dic_cotacoes]
print(dic_USD_BRL_30)


# #### Pegar as cotações do BitCoin de Jan/20 a Out/20

# In[ ]:


cotacoes_btc = requests.get('https://economia.awesomeapi.com.br/json/daily/BTC-BRL/200?start_date=20200101&end_date=20201031')
cotacoes_btcdic = cotacoes_btc.json()
dic = [float(item['bid']) for item in cotacoes_btcdic]
dic.reverse()
print(dic)


# #### Gráfico com as cotações do BitCoin

# In[ ]:


import matplotlib.pyplot as plt

plt.figure(figsize=(15,5))
plt.plot(dic)
plt.show()


# In[ ]:




