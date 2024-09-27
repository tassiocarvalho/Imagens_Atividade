from PIL import Image
import os
import numpy as np
import matplotlib.pyplot as plt  # Importação da biblioteca para gráficos
import pandas as pd  # Importação da biblioteca para tabelas

# Diretório das imagens (mesmo diretório do código + /imagens)
diretorio = os.path.join(os.getcwd(), 'imagens')

# Dicionário com os nomes das imagens e as áreas estimadas, associando cada uma ao respectivo país ou continente
imagens_areas = {
    'Fig0112(1)(top-canada).tif': ('Canadá', 10143500.04),   # km²
    'Fig0112(2)(2nd-from-top-USA).tif': ('Estados Unidos', 9795815.12),   # km²
    'Fig0112(3)(3rd-from-top-Central-Amer).tif': ('América Central', 1015582.74),   # km²
    'Fig0112(4)(4th-from-top-South-Amer).tif': ('América do Sul', 17707475.70),   # km²
    'Fig0113(1)(left-africa-europe).tif': ('África e Europa', 43660425.27),   # km²
    'Fig0113(2)(center-russia).tif': ('Ásia Central', 42124870.31),   # km²
    'Fig0113(3)(right-South-East-Asia).tif': ('Sul da Ásia', 1970036.81),   # km²
    'Fig0113(4)(right-bottom-Australia).tif': ('Austrália', 7803943.11)    # km²
}

# Lista para armazenar as áreas por pixel e os dados das regiões
tabela_dados = []

intensidades_paises = {}
intensidade_total_mundo = 0  # Para armazenar a soma ponderada total do mundo

# Loop para calcular as áreas por pixel de cada imagem
for imagem, (regiao, area) in imagens_areas.items():
    caminho_imagem = os.path.join(diretorio, imagem)
    
    # Verifica se o arquivo de imagem existe
    if not os.path.isfile(caminho_imagem):
        print(f"A imagem {imagem} não foi encontrada no diretório {diretorio}.")
        continue
    
    # Abre a imagem em modo de nível de cinza
    img = Image.open(caminho_imagem).convert('L')
    largura, altura = img.size
    
    # Calcula o número total de pixels (m x n)
    num_pixels = largura * altura
    
    # Calcula a área por pixel
    area_por_pixel = area / num_pixels
    
    # Calcula a soma das intensidades dos pixels
    pixel_array = np.array(img)
    soma_intensidades = np.sum(pixel_array)
    
    # Soma ponderada pela área por pixel
    intensidade_ponderada = soma_intensidades * area_por_pixel
    
    # Acumular a soma ponderada para o mundo
    intensidade_total_mundo += intensidade_ponderada
    
    # Armazenar os dados de cada região na tabela
    tabela_dados.append([regiao, area, num_pixels, area_por_pixel, intensidade_ponderada])

# Verifica se pelo menos uma imagem foi processada
if intensidade_total_mundo == 0:
    print("Nenhuma imagem foi processada. Verifique se as imagens estão no diretório correto.")
else:
    # Criar um DataFrame para exibir os dados
    df = pd.DataFrame(tabela_dados, columns=['Região', 'Área (km²)', 'Número de pixels (MxN)', 'Área por pixel (km²/pixel)', 'Intensidade Ponderada'])
    
    # Calcular a intensidade normalizada
    df['Intensidade Normalizada (%)'] = (df['Intensidade Ponderada'] / intensidade_total_mundo) * 100
    
    # Exibir a tabela
    print("Tabela de valores de cada região por km²/pixel e normalizados:")
    print(df)

    # Exibir a soma total ponderada do mundo (para verificação)
    print(f"\nSoma total ponderada (mundo): {intensidade_total_mundo:.6f}")
    
    # Plotar o gráfico de barras dos percentuais de energia
    plt.figure(figsize=(10, 6))
    plt.bar(df['Região'], df['Intensidade Normalizada (%)'], color='skyblue')
    plt.xlabel('Região')
    plt.ylabel('Percentual estimado de energia (%)')
    plt.title('Uso estimado de energia por região (baseado na intensidade global)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    # Plotar o gráfico de pizza dos percentuais de energia
    plt.figure(figsize=(8, 8))
    
    # Paleta de cores personalizada
    cores = plt.cm.Set3(np.linspace(0, 1, len(df)))
    
    # Criar o gráfico de pizza sem explode e shadow
    plt.pie(df['Intensidade Normalizada (%)'], labels=df['Região'], autopct='%1.1f%%', startangle=140,
            colors=cores, wedgeprops={'edgecolor': 'white'})
    
    plt.title('Distribuição do uso estimado de energia por região', fontsize=14)
    plt.axis('equal')  # Assegura que o gráfico seja um círculo
    plt.tight_layout()
    plt.show()
