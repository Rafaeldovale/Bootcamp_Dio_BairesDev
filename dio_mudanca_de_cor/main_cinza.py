def converte_para_cinza(input, output):
    try:
        with open(input, 'rb') as arquivo_entrada:
            cabecalho = arquivo_entrada.read(54)
            
            largura = int.from_bytes(cabecalho[18:22], 'little')
            altura = int.from_bytes(cabecalho[22:26], 'little')
            
            pixels_dados = arquivo_entrada.read()

        pixels_cinza = bytearray()

        for i in range(0, len(pixels_dados), 3):
            azul = pixels_dados[i]
            verde = pixels_dados[i + 1]
            vermelho = pixels_dados[i + 2]
            
            luminancia = int(0.299 * vermelho + 0.587 * verde + 0.114 * azul)
            
            pixels_cinza.append(luminancia)
            pixels_cinza.append(luminancia)
            pixels_cinza.append(luminancia)

        with open(output, 'wb') as arquivo_saida:
            arquivo_saida.write(cabecalho)
            arquivo_saida.write(pixels_cinza)

        print(f"Imagem convertida e salva com sucesso: {output}")

    except FileNotFoundError:
        print(f"Erro: O arquivo não encontrado '{input}'")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


converte_para_cinza('gato.bmp', 'gato_cinza.bmp')