$Hostname = 'dc01' ## Add hostname
$DomainName = 'evilcorp.org' ## put domain name here
$DomainNetbiosName = 'evilcorp'
# $Credential = 'evilcorp.org\administrator'
$Ipn = Read-Host -Prompt '192.168.20.101'
$Sub = Read-Host -Prompt '255.255.255.0'
$Gateway = Read-Host -Prompt '192.168.20.2'

# Set Hostname
Rename-Computer $Hostname

# Set IP Address
netsh interface ip set address name='Ethernet0' static $Ipn $Sub $Gateway

# Set DNS
Set-DnsClientServerAddress -InterfaceAlias "Ethernet0" -ServerAddresses ("127.0.0.1","192.168.20.2")

# Windows Firewall OFF
netsh advfirewall set allprofile state off

# Join to existing domain
# Add-Computer -Domain $DomainName -NewName $hostname -Credential $Credential -Restart -Force

# Create Active Directory Forest
Install-windowsfeature -name AD-domain-services -IncludeManagementTools

Test-ADDSForestInstallation -DomainName $DomainName -InstallDns

Import-Module ADDSDeployment
Install-ADDSForest -CreateDnsDelegation:$false -DatabasePath 'C:\\Windows\\NTDS' -DomainMode 'Win2012R2' -DomainName $DomainName -DomainNetbiosName $DomainNetbiosName -ForestMode 'Win2012R2' -InstallDns:$true -LogPath 'C:\\Windows\\NTDS' -NoRebootOnCompletion:$false -SysvolPath 'C:\\Windows\\SYSVOL' -Force:$true