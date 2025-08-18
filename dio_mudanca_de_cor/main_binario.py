def converte_para_binario(input, output):
    try:
        with open(input, 'rb') as arquivo_entrada:
            cabecalho = arquivo_entrada.read(54)
            
            largura = int.from_bytes(cabecalho[18:22], 'little')
            altura = int.from_bytes(cabecalho[22:26], 'little')
            
            pixels_dados = arquivo_entrada.read()

        limiar = 128
        
        pixel_bin = bytearray()

        for i in range(0, len(pixels_dados), 3):
            azul = pixels_dados[i]
            verde = pixels_dados[i + 1]
            vermelho = pixels_dados[i + 2]
            
            luminancia = int(0.299 * vermelho + 0.587 * verde + 0.114 * azul)
            
            if luminancia > limiar:
                valor_pixel = 255  # Branco
            else:
                valor_pixel = 0    # Preto
            
            pixel_bin.append(valor_pixel)
            pixel_bin.append(valor_pixel)
            pixel_bin.append(valor_pixel)

        with open(output, 'wb') as arquivo_saida:
            arquivo_saida.write(cabecalho)
            arquivo_saida.write(pixel_bin)

        print(f"Imagem binarizada e salva com sucesso!: {output}")

    except FileNotFoundError:
        print(f"Erro: O arquivo não foi encontrado' {input}'")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Exemplo de uso:
converte_para_binario('gato.bmp', 'gato_binario.bmp')