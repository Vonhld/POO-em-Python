from datetime import date                   # Modulo referente à acquisição do dia atual
from lib.mod import MinhaData               # Modulos referente às classes criadas
from lib.mod import DataComemorativa
from lib.mod import DatasComemorativas

data_hoje = date.today()
data = data_hoje.strftime('%d/%m/%Y')

#   K)i) Data atual:
#        Padrão:'%d/%m/%Y' 
hoje = MinhaData(data)

#        Data genérica:
#        Padrão: dia, mês, ano
#dia882008 = MinhaData(8,8,2008)
#print(hoje)
#print(dia882008)

#   K)i) Criação da data comemorativa 'Natal'
natal = DataComemorativa('Natal',25,12,int(data_hoje.strftime('%Y')),True,True)

#   K)ii) Comparação do dia atual com o natal e 'print' do valor
print(hoje.Compara(natal))

#   K)iii) Criação da coleção de datas comemorativas
colecao_datas_comemorativas = DatasComemorativas()

# K)iii) Adicionando natal à coleção
colecao_datas_comemorativas.Adiciona(natal)

# K)iii) 'print' das horas não trabalhadas
print(colecao_datas_comemorativas.HorasNaoTrabalhadas())
