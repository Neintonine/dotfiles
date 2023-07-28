#Requires -RunAsAdministrator

function installPrograms() {
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
}

function setupLinks() {
    Write-Host "# Creating Links"

    $links = Get-Content "links.json" | ConvertFrom-Json

    foreach($link in $links.PSObject.Properties) {
        $source = "./settings/" + $link.name
        $source =  [System.IO.Path]::GetFullPath([System.IO.Path]::Combine($PSScriptRoot, $source));

        $target = $link.value.replace("[UserProfile]", "$env:USERPROFILE")
        $target = [System.IO.Path]::GetFullPath($target)

        Write-Host -NoNewline "## Establising Link from '$source' to '$target' ..."
        
        if (![System.IO.Directory]::Exists($source)) {
            Write-Host "failed: Source missing"
            continue;
        }

        New-Item -Path $target -ItemType SymbolicLink -Value $source

        Write-Host "done"
    }
}

installPrograms

Write-Host "# -----------------"

Write-Host ""

setupLinks