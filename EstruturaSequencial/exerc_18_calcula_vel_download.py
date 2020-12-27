# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a
# velocidade de um link de Internet (em Mbps), calcule e
# informe o tempo aproximado de download do arquivo usando este link (em minutos).
print()
tam_download = float(input('Qual o tamnho do download em MB ? '))
vel_download = int(input('Qual a velocidade da sua conexão para download? '))
tempo_dowload = tam_download / (vel_download/8)
tempo_minutos = tempo_dowload/60
print(f'Seu download será concluido em {tempo_minutos} minutos')
