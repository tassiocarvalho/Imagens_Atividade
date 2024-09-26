
### Processamento e Análise de Imagens para Estimativa de Uso de Energia

Este projeto utiliza imagens de satélite noturnas para estimar o uso de energia em diferentes regiões do mundo. O processamento das imagens é realizado em etapas que incluem o cálculo da área por pixel, a análise das intensidades luminosas e a determinação de percentuais de uso de energia por região. A seguir estão as etapas detalhadas:

#### 1. Cálculo da Área por Pixel

Cada imagem representa uma região geográfica com uma área conhecida, expressa em quilômetros quadrados. O primeiro passo é calcular a área correspondente a cada pixel da imagem, considerando suas dimensões. Isso é feito dividindo a área total da região pelo número total de pixels da imagem (calculado multiplicando a largura pela altura). O valor obtido representa a área de cada pixel, o que será usado posteriormente para ponderar as intensidades luminosas.

#### 2. Análise das Intensidades Luminosas

As imagens são convertidas para arrays NumPy contendo os níveis de cinza de cada pixel. A soma das intensidades de todos os pixels de uma imagem fornece uma medida aproximada da quantidade de luz visível naquela região à noite. Este valor é utilizado como proxy para o consumo de energia elétrica, com a premissa de que áreas mais iluminadas tendem a ter maior consumo de energia.

#### 3. Cálculo da Intensidade Ponderada

A intensidade luminosa de cada região é ponderada pela área de cada pixel, gerando um valor ponderado de intensidade. Essa abordagem permite relacionar a quantidade de luz com a área geográfica, corrigindo distorções causadas pelo tamanho da região representada. A soma dessas intensidades ponderadas fornece uma estimativa total para o mundo, que serve como base para calcular a participação percentual de cada região.

#### 4. Cálculo dos Percentuais de Uso de Energia

Com a intensidade ponderada de cada região e o valor total mundial, calcula-se o percentual estimado de uso de energia para cada local. O percentual de cada região é obtido dividindo-se sua intensidade ponderada pela intensidade total mundial e multiplicando por 100. Esses percentuais são armazenados e posteriormente visualizados por meio de gráficos de barras e gráficos de pizza, oferecendo uma representação clara da distribuição de energia entre as regiões.
