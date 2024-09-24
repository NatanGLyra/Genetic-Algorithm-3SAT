import os

def ajustar_arquivo(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        #infile = infile[:-2]
        for line in infile:
            # Quebra a linha em uma lista de valores separados por espaço
            valores = line.strip().split()
            # Remover o último valor se ele for zero e estiver isolado
            if valores:
                # and valores[-1] == '0'
                if (valores[-1] == '0'):
                    valores = valores[:-1]
                if (len(valores)>0 and valores[0] == 'p'):
                    nova_linha = ''.join(valores[-2])
                    outfile.write(nova_linha + '\n')
                    nova_linha = ''.join(valores[-1])
                    outfile.write(nova_linha)
                    continue
                if (len(valores)>0 and valores[0] == 'c'):
                    continue
                if (len(valores)>0 and valores[0] == '%'):
                    continue
                nova_linha = ' '.join(valores)
                if len(nova_linha)>0:
                    outfile.write('\n' + nova_linha)

caminho_pasta = './uf20-91'

for nome_arquivo in os.listdir(caminho_pasta):
    caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)
    if os.path.isfile(caminho_arquivo):  # Verifica se Ã© um arquivo
        nome_arquivo = nome_arquivo.replace(".cnf", ".txt")
        ajustar_arquivo(caminho_arquivo, "./ajustados/"+nome_arquivo)