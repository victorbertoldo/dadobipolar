<#
Copyright (c) 2019 Victor Bertoldo

Após a instalação da Extensão PowerShell da Microsoft, basta selecionar o Script e teclar F8 para fazer o trace em tempo real.

A variável que está descomentada, está apontando para o diretorio local no Sense Desktop

#>
$var = Get-ChildItem -Path "C:\Users\victor.bertoldo\Documents\Qlik\Sense\Log\Script\" |  Sort-Object -Property CreationTime | Select-Object -Last 1 
<#
O diretório comentado é um mapeamento da pasta de logs do servidor
$var = Get-ChildItem -Path "S:\" |  Sort-Object -Property CreationTime | Select-Object -Last 1 
#>
    get-content $var.FullName -Wait