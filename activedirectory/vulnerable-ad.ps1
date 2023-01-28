$DomainName = 'evilcorp.org' ## put domain name here

# Run the vulnerable-AD script
Invoke-Expression ((new-object net.webclient).downloadstring('https://raw.githubusercontent.com/wazehell/vulnerable-AD/master/vulnad.ps1'));
Invoke-VulnAD -UsersLimit 100 -DomainName $DomainName