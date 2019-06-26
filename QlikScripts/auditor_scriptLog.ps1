$var = Get-ChildItem -Path "C:\Users\victor.bertoldo\Documents\Qlik\Sense\Log\Script\" |  Sort-Object -Property CreationTime | select -Last 1 
#O diretório comentado é um mapeamento da pasta de logs do servidor
#$var = Get-ChildItem -Path "S:\" |  Sort-Object -Property CreationTime | select -Last 1 
get-content $var.FullName -Wait