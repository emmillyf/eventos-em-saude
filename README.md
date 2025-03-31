<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Projeto de Web Scraping para baixar e compactar PDFs de um site governamental.">
</head>
<body>
    <h1>🕷️ Teste de Web Scraping</h1>
    
   <h3>📌 Descrição do Projeto</h3>
 <p>Este projeto realiza <strong>Web Scraping</strong> para acessar um site governamental, baixar arquivos PDF e compactá-los em um único arquivo ZIP. A solução foi desenvolvida em <strong>Python</strong> utilizando <strong>Selenium</strong> para automação do navegador e <strong>requests</strong> para download dos arquivos.</p>
    
   <h3>🚀 Funcionalidades</h3>
<ul>
<li>Acessar a página: <a href="https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos" target="_blank">ANS - Atualização
        do Rol de Procedimentos</a></li>
   <li>Localizar e baixar os anexos <strong>I e II</strong> no formato PDF</li>
   <li>Compactar os arquivos baixados em um único arquivo ZIP</li>
</ul>

<h3>🛠️ Tecnologias Utilizadas</h3>
<ul>
<li><strong>Python 3</strong></li>        
<li>Bibliotecas:
            <ul>
                <li><code>Selenium</code> (Automação de navegador)</li>
                <li><code>Webdriver-manager</code> (Gerenciar drivers) 
                <li><code>Requests</code> (Download de arquivos)</li>
                <li><code>Zipfile</code> (Compactação dos PDFs)</li>
            </ul>
        </li>
</ul>
<h3>📦 Dependências</h3>
<pre><code>pip install selenium requests webdriver-manager</code></pre>
<p>Ou instale a partir do arquivo de requisitos:</p>
<pre><code>pip install -r requirements.txt</code></pre>

<h3>📖 Como Executar</h3>
    <ol>
        <li><strong>Clone o repositório:</strong></li>
      <pre><code>git clone https://github.com/emmillyf/eventos-em-saude.git
</code></pre>
        <li><strong>Instale as dependências:</strong></li>
        <pre><code>pip install -r requirements.txt</code></pre>
        <li><strong>Execute o script:</strong></li>
        <pre><code>python scripts/main.py</code></pre>
    </ol>
    <p>Os arquivos PDF serão baixados no diretório <code>downloads/</code> e compactados em <code>anexos.zip</code>.</p>

 <hr>
<p>Feito por <strong>Emmilly Gomes</strong></p>
</body>
</html>
