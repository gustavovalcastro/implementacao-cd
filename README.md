# implementacao-cd
Implementação de projeto que contém conceitos estudados na disciplina de Computação Distribuída.

Neste trabalho implementamos um algoritmo para realizar processamento de imagens em um Sistema Distribuído, focamos no desenvolvimento de pré-processamento de imagens, ou, Data Augmentation.

Para implementação utilizamos a biblioteca Dask, decidimos utiliza-la devido a suas capacidades de implementar algoritmos distribuídos, também utilizamos a biblioteca OpenCV para desenvolver os métodos de Data Augmentation que podem ser realizados pelo sistema, estes métodos são listados abaixo:

- brigthnessIncrease: Aumenta o brilho na Imagem em 60
- brigthnessDecrease: Reduz o brilho da imagem em 60
- contrastIncrease: Aumenta o contraste em 1.5
- contrastDecrease: Reduz o contraste em 0.5
- resize: Muda as dimensões da Imagem para 320x320
- randomNoise: Adiciona ruido na imagem
- gaussianBlur: Aplica um filtro de Gaussian na imagem, resultando em um borrão/desfoque
- flipHorizontal: Transformação horizontal da imagem
- flipVertical: Transformação vertical da Imagem
- heavySharpening: Este método aplica um kernel a imagem, neste código o kernel é aplicado 500 para aumentar o tempo de processamento do programa

As dependências do código são listadas em: requirements.txt

Para testarmos o sistema utilizamos um mini servidor que pode suportar múltiplas maquinas virtuais, nas quais o processamento de imagens é feito, e obtivemos os seguintes resultados para 21 imagens:
1 nó - 28 segundos
2 nós - 16 segundos
3 nós - 11 segundos
4 nós - 10 segundos

Percebemos que ao aumentas de 3 para 4 nós não houve uma mudança significativa no tempo de processamento, isso se dá devido ao fato de que os 4 nos precisam acessar o disco simultaneamente para gravar as imagens, portanto o IO se torna um gargalo neste sistema.
