import os
import requests
from srclinks import iniciar_driver
from srclinks import encontrar_links
from baixarpdf import baixar_Pdf, compactar_Pdf

def obter_links(driver):
    try:
        # Obtém os links dos PDFs
        pdf_links = encontrar_links(driver)
        if not pdf_links:
            raise ValueError("Nenhum link de PDF encontrado.")
        return pdf_links
    except Exception as e:
        print(f"Erro ao obter os links dos PDFs.")

def baixando_pdfs(pdf_links):
    # Realiza o download dos PDFs e salva 
    arquivos_baixados = []

    for idx, pdf_url in enumerate(pdf_links):
        nomeDoArquivo = os.path.join('downloads', f"anexo {idx+1}.pdf")
        try:
            baixar_Pdf(pdf_url, nomeDoArquivo)
            arquivos_baixados.append(nomeDoArquivo)
        except requests.exceptions.RequestException as e:
            print(f"Erro ao baixar {pdf_url}: {e}")
        except Exception as e:
            print(f"Erro ao salvar o PDF {nomeDoArquivo}: {e}")

    return arquivos_baixados

def compactacao_pdf(arquivos_baixados):
     # Faz a compactação dos arquivos
    if not arquivos_baixados:
        print("Nenhum arquivo para compactar")
        return
     
    try:
        arquivoZip = os.path.join('downloads', 'anexos.zip')
        compactar_Pdf(arquivos_baixados, arquivoZip)
    except Exception as e:
        print(f"Erro ao compactar os arquivos: {e}")

def main(): 
    try:
        # Cria a pasta 'downloads' caso não exista
        if not os.path.exists('downloads'):
            os.makedirs('downloads')
            
        driver = iniciar_driver()
        pdf_links = obter_links(driver)
        arquivos_baixados = baixando_pdfs(pdf_links)
        compactacao_pdf(arquivos_baixados)
    except Exception as e:
     print(f"Erro ao iniciar o WebDriver: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()