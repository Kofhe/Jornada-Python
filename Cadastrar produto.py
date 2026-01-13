# 1 - Entrar no sistema da empresa
# pip install pyautogui - permite automatizar tarefas repetitivas no computador
# 2 - Fazer o login com usuario e senha
# 3 - Abrir a base de dados de produtos
# 4 - Cadastrar 1 produto
# 5 - Repetir o passo 4 até acabar a lista de produtos

import pyautogui
import time # o time será usado para fazer pausas no código

pyautogui.PAUSE = 0.5 # tempo de espera entre as ações
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

#abrir o navegador
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# 1 - Entrar no sistema da empresa
pyautogui.write(link) #ou pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login') 
pyautogui.press('enter')

#fazer um tempo de espera para a página carregar
time.sleep(3)

# 2 - Fazer o login com usuario e senha
pyautogui.click(x=779, y=408) # clicar no campo usuario
pyautogui.write('testepython@gmail.com') # escrever o usuario
pyautogui.press('tab') # ir para o campo senha ou pyautogui.click(x=764, y=510) com o time.sleep(5)  # Tempo para o usuário posicionar o cursor e print(pyautogui.position())  # Imprime a posição atual do cursor
pyautogui.write('Testepython123') # escrever a senha
pyautogui.click(x=964, y=574) # clicar no botão entrar
time.sleep(3) # esperar a página carregar

# 3 - Abrir a base de dados de produtos
#instalar pandas pip install pandas openpyxl, importar pandas no codigo.py e ler o excel
import pandas
#Foi criado a tabela para o programa conseguir ler os dados
tabela = pandas.read_csv('produtos.csv')
print(tabela)

for linha in tabela.index: # para cada linha na tabela faça: e index significa o número da linha
# 4 - Cadastrar 1 produto
    pyautogui.click(x=775, y=285) # clicar no menu produtos

    #codigo
    #o str serve para transformar o valor em texto
    #o loc significa localizar o valor na tabela
    codigo = str(tabela.loc[linha, 'codigo']) # pegar o código do produto da tabela
    pyautogui.write(codigo) # escrever o código do produto
    pyautogui.press('tab') # ir para o campo descrição

    #colocou o nome da colunna por que é mais fácil de identificar em vez de colocar manual o nome do produto

    #marca
    marca = str(tabela.loc[linha, 'marca'])
    pyautogui.write(marca) # escrever a marca
    pyautogui.press('tab') # ir para o próximo campo
    
    #tipo
    tipo = str(tabela.loc[linha, 'tipo'])
    pyautogui.write(tipo) # escrever o tipo do produto
    pyautogui.press('tab') # ir para o próximo campo
    
    #categoria
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria) # categoria
    pyautogui.press('tab') # ir para o próximo campo

    #preço_unitario
    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco_unitario) # preço_unitario  
    pyautogui.press('tab') # ir para o próximo campo
    
    # custo
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo) # custo
    pyautogui.press('tab') # ir para o próximo campo
    
    # obs
    obs = str(tabela.loc[linha, 'obs']) 
    pyautogui.write(obs) # obs

    pyautogui.click('x=891, y=946') # ir para o botão salvar
    #depois testar o salvar com tab 
    #pyautogui.press('tab')
    #pyautogui.click('enter') # clicar no botão salvar
    
pyautogui.scroll(5000)  

# 5 - Repetir o passo 4 até acabar a lista de produtos  
