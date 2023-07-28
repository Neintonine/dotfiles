#Requires -RunAsAdministrator


$programs = Get-Content "programs.json" | ConvertFrom-Json

if ($programs.PSObject.Properties.name -contains "winget") {
    Write-Host "# Installing programs using WinGet..."

    foreach ($program in $programs.winget) {
        Write-Host -NoNewline "## Installing: $program ..."

        #winget.exe install -e -h --id $program > $null
        Write-Host "done"
    }
}

Write-Host "# -----------------"

if ($programs.PSObject.Properties.name -contains "choco") {
    Write-Host "# Installing programs using Chocolatey"

    # Check if "choco" is already available.
    $chocoExists = Get-Command 'choco' -ErrorAction SilentlyContinue;
    if (!$chocoExists) {
        
        Write-Host "## Installing Chocolatey"
        Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1')) > $nul
    }

    foreach ($program in $programs.choco) {
        Write-Host -NoNewline "## Installing: $program ..."

        choco.exe install -y $program > $null
        Write-Host "done"
    }
}

Write-Host "# -----------------"

Write-Host ""