



# Rocketbot Xperience
  
Modulo para trabalhar com formulários do Rocketbot Xperience  

*Read this in other languages: [English](Manual_Xperience.md), [Português](Manual_Xperience.pr.md), [Español](Manual_Xperience.es.md)*
  
![banner](imgs/Banner_Xperience.jpg)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Descrição do comando

### Login NOC
  
Faça login no NOC usando uma das opções, arquivo noc.ini, API Key ou credenciais.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|URL Servidor|URL do servidor para se conectar|https://roc.myrb.io/|
|Selecione um método para se conectar ao orquestrador|Opções para fazer login no R.O.C, você pode usar credenciais de usuário, chave de API ou selecionar o arquivo noc.ini|API Key|
|Proxies|Proxies com os que se configurará a sessão. Indique o protocolo seguido do servidor|http://00.00.000.000:0000|
|Usuario proxie|Opcional. Completar se requirirá configurar proxies.|user/user|
|Contraseña proxie|Opcional. Completar se requiriere configurar proxies.|#Aa000000.Aa0000000a#|
|Não verifique o certificado SSL|Se marcada, a solicitação enviada não verifica o certificado SSL.||
|Atribuir resultado à variável|Variável onde será armazenado o estado da conexão, retorna True se for bem sucedida ou False caso contrário|Variable|

### Obter fila de trabalho de Formulários
  
Obtém as filas de trabalho
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Form Token|Form Token|8YWUW8AXAV3UPNKY|
|Definir como variável|Variável para guardar resultado sem {}|var|

### Obter fila de trabalho bloqueada de Formulários
  
Obtém as filas de trabalho bloqueadas
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Form Token|Form Token|8YWUW8AXAV3UPNKY|
|Definir como variável|Variável para guardar resultado sem {}|var|

### Obter todos os dados de formulário
  
Obter todos os dados de formulário da fila de trabalho. O comando retorna os dados no formato de dicionário
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da fila de trabalho|ID da fila de trabalho|1|
|Form Token|Form Token|8YWUW8AXAV3UPNKY|
|Variáveis de preenchimento automático|O resultado será atribuído às variáveis já criadas|True|
|Definir como variável|Variável para guardar resultado sem {}|var|

### Baixar arquivo
  
Baixe um arquivo enviado em um formulário
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|ID da fila|ID da fila|1|
|Arquivo|Variável que contém o caminho do arquivo do formulário|orchestator/arquivo.ext|
|Salvar arquivo em|Caminho onde o arquivo será salvo|C:\Rocketbot\file.ini|

### Atualizar estado da fila Form
  
Mudar o estado da fila
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Estado|Selecione o estado da fila|Done|
|ID da fila de trabalho|Insira o ID da fila de trabalho|1|
|Atribuir a variável|Nome da variável sem {} onde o resultado será salvo|variable|

### Return Message to Xperience
  
Returns a message to the Xperience form
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Xperience Token|Xperience Token|{xperience}|
|Message to return|Message to return|This is a message|

### Envie um arquivo para o Xperience
  
Enviar um arquivo sempre que a opção SEND API do formulário estiver ativa
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Xperience Token|Token {xperience} gerado com o comando 'Obter dados do formulário'|{xperience}|
|Arquivo para carregar|Caminho do arquivo a ser enviado ao orquestrador|C:/Users/pc/Downloads/img.png|
|Atribuir a variável|Nome da variável onde o resultado será salvo|variable|

### Pesquisar dados no formulário
  
Este comando permite pesquisar dados em um formulário Xperience
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Form Token|Form Token|8YWUW8AXAV3UPNKY|
|ID do input|ID do input a ser pesquisado|User|
|Valor a buscar|Valor a ser pesquisado no input selecionado|Rocketbot|
|Variáveis de preenchimento automático|O resultado será atribuído às variáveis já criadas|True|
|Bloquear fila do formulário|A fila do formulário será bloqueada no Orquestrador|True|
|Atribuir resultados à variável|Variável para guardar resultado sem {}|var|
|Definir id da fila do formulário para variável|Variável para armazenar id da fila do formulário|var|

### Obter todas as filas de trabalho
  
Obtém as filas de trabalho de todos os formulários que estão no intervalo de datas indicado
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|De data |Obrigatório. Formato de data AAAA-MM-DD|2024-01-01|
|A data |Obrigatório. Formato de data AAAA-MM-DD|2024-01-01|
|Definir como variável|Variável para guardar resultado sem {}|var|
