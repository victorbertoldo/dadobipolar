# d48a075c-651a-4ed3-8a95-66eb8026ff65

# $var = Get-ChildItem -Path "S:\0fbb5a71-cde9-491a-bf20-a2cae504ef2a.*.log" |  Sort-Object -Property CreationTime | Select-Object -Last 1 
    # get-content $var.FullName -Wait



    $var = Get-ChildItem -Path "C:\Users\victor.bertoldo\Documents\Qlik\Sense\Log\Script\" |  Sort-Object -Property CreationTime | Select-Object -Last 1 
    get-content $var.FullName -Wait