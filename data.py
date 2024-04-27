import datetime

def days():
    data_atual = datetime.datetime.now()
    dias_semana = {
        0: 'Segunda-feira',
        1: 'Terça-feira',
        2: 'Quarta-feira',
        3: 'Quinta-feira',
        4: 'Sexta-feira',
        5: 'Sábado',
        6: 'Domingo'
    }
    numero_semana = data_atual.weekday()
    dia_semana = dias_semana[numero_semana]
    dia_mes = data_atual.day
    ano_atual = data_atual.year
    return dia_semana, dia_mes, ano_atual

# Testar a função
dia_semana, dia_mes, ano_atual = days()
print(f"Hoje é, {dia_semana}, e é dia, {dia_mes}, ano {ano_atual}")
print(days())
