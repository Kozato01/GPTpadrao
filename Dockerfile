# Use uma imagem base do Python 3.11.4 slim
FROM python:3.11.4-slim

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

RUN apt update
RUN apt install -y build-essential gcc

# Copie apenas os arquivos necessários para a pasta 'workspaces'
COPY requirements.txt workspaces/
COPY script.py workspaces/
COPY gpt.py workspaces/
COPY .env workspaces/
COPY prompts workspaces/prompts
COPY layout workspaces/layout
COPY utils workspaces/utils

#unstructured[all-docs]==0.10.29

RUN pip install --no-cache-dir -r workspaces/requirements.txt \
    && pip install --index-url=https://pkgs.dev.azure.com/azure-sdk/public/_packaging/azure-sdk-for-python/pypi/simple/ azure-search-documents==11.4.0a20230509004


# Exponha a porta em que o Streamlit será executado (por padrão, a porta 8501)
EXPOSE 8501

# Comando para iniciar a aplicação Streamlit
CMD ["streamlit", "run", "workspaces/gpt.py"]
