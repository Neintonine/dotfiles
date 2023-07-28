#Requires -RunAsAdministrator
function installPrograms() {
    $programs = Get-Content "programs.json" | ConvertFrom-Json

    if ($programs.PSObject.Properties.name -contains "winget") {
        
        foreach ($program in $programs.winget) {
            Write-Progress -Activity "Installing WinGet programs..." -CurrentOperation "Installing: $program"

            winget.exe install -e -h --id $program > $null
        }
        Write-Progress -Completed True
    }

    if ($programs.PSObject.Properties.name -contains "choco") {

        # Check if "choco" is already available.
        $chocoExists = Get-Command 'choco' -ErrorAction SilentlyContinue;
        if (!$chocoExists) {
            
            Write-Progress -Activity "Installing Chocolatey programs..." -CurrentOperation "Installing: Chocolatey"
            Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1')) > $nul
        }

        foreach ($program in $programs.choco) {
            Write-Progress -Activity "Installing Chocolatey programs..." -CurrentOperation "Installing: $program"

            choco.exe install -y $program > $null
        }
        
        Write-Progress -Completed True
    }
}

function setupLinks() {
    $links = Get-Content "links.json" | ConvertFrom-Json

    foreach($link in $links.PSObject.Properties) {
        $source = "./settings/" + $link.name
        $source =  [System.IO.Path]::GetFullPath([System.IO.Path]::Combine($PSScriptRoot, $source));

        $target = $link.value.replace("[UserProfile]", "$env:USERPROFILE")
        $target = [System.IO.Path]::GetFullPath($target)

        Write-Progress -Activity "Create Folder Links..." -CurrentOperation "$source -> $target"
        
        if (![System.IO.Directory]::Exists($source)) {
            continue;
        }

        New-Item -Path $target -ItemType SymbolicLink -Value $source -Force > $null

    }
    Write-Progress -Completed True
}

Write-Host "# Starting Setup"

installPrograms

setupLinks

Write-Host "# Setup Complete"