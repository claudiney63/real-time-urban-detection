# Detecção Urbana em Tempo Real
Projeto de detecção e classificação de objetos urbanos usando Visão Computacional. Utiliza modelos como YOLO e MobileNet para identificar pedestres, veículos e sinais em ambientes dinâmicos. Foca em desafios como clima, iluminação e tempo real, com aplicações para cidades inteligentes e segurança.

## Estrutura do Repositório
- **`data/`**: Dados utilizados no projeto (imagens, vídeos, anotações).  
- **`models/`**: Modelos treinados e checkpoints.  
- **`notebooks/`**: Análises e experimentos em Jupyter Notebooks.  
- **`src/`**: Código-fonte principal.  
- **`tests/`**: Testes automatizados.  
- **`results/`**: Resultados obtidos, incluindo imagens e métricas.  
- **`docs/`**: Documentação do projeto.

## Como Configurar o Ambiente

### 1. Criar um Ambiente Virtual
Antes de instalar as dependências, crie um ambiente virtual para isolar o projeto. 

No Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

No Linux/Mac:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Instalar Dependências
Com o ambiente virtual ativo, instale as bibliotecas necessárias:
```bash
pip install -r requirements.txt
```