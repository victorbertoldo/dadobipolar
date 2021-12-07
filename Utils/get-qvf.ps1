<#
Copyright (c) 2019 Victor Bertoldo

Este script importa o qvf para o repositório git configurado

Criar a variável de ambiente de sistema: qlikPath com o valor %userprofile%\Documents\Qlik\Sense\Apps\
#>
$path       = $env:qlikPath
$app        = "MapaBr.qvf" # Digite o nome do App
$repo       =  "D:\dadobipolar\Mapa\" #Coloque o caminho destino, onde o repositório local foi configurado.



(New-Object -ComObject Scripting.FileSystemObject).CopyFile($path+$app, $repo)