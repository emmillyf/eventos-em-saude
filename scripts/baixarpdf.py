from zipfile import ZipFile
import requests
import os

def baixar_Pdf(pdf_url, arquivo):
    response = requests.get(pdf_url, arquivo)
    # Faz uma requisição para a URL, baixa o arquivo e o armazena em 'response'
    with open(arquivo, 'wb') as f:
        f.write(response.content)
    print(f"Arquivo baixado: {arquivo}")

def compactar_Pdf(arquivos_pdf, pasta_zip):
    with ZipFile(pasta_zip, 'w') as zipf:
        for pdf in arquivos_pdf:
            zipf.write(pdf, os.path.basename(pdf))
    print(f"Arquivo compactado: {pasta_zip}")
