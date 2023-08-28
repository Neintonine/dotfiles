#Requires -RunAsAdministrator
param(
    [bool]$runInstall,
    [bool]$runLinks,
    [bool]$runPostInstall,
    [bool]$debug
)

if (!$runInstall -and !$runLinks -and !$runPostInstall) {
    $runInstall = $true;
    $runLinks = $true;
    $runPostInstall = $true;
}

if (!$PSBoundParameters.ContainsKey('debug')) {
    $debug = $false;
}

function checkForFile([string] $file) {
    $relativeFile = './' + $file;
    $completePath = [System.IO.Path]::GetFullPath([System.IO.Path]::Combine($PSScriptRoot, $relativeFile));
    
    return [System.IO.File]::Exists($completePath);
}

function installPrograms() {
    if (!(checkForFile -file "programs.json")) {

        if ($debug) {
            Write-Host "## programs.json not found. Skipping programs install..."
        }

        return
    }

    $programs = Get-Content "programs.json" | ConvertFrom-Json

    if ($programs.PSObject.Properties.name -contains "winget") {
        
        $wingetExists = Get-Command 'winget' -ErrorAction SilentlyContinue;
        if (!$wingetExists) {
            Write-Host "WinGet has to be installed, to use install programs with it. Head over to the 'App Installer'-Page on the Microsoft Store to install it. Then restart the powershell."
            Exit
        }

        foreach ($program in $programs.winget) {
            Write-Progress -Activity "Installing WinGet programs..." -CurrentOperation "Installing: $program"

            if ($debug) {
                Write-Host "## Installing WinGet: $program"
                winget.exe install -e -h --accept-source-agreements --accept-package-agreements --id $program
            } else {
                winget.exe install -e -h --accept-source-agreements --accept-package-agreements --id $program > $null
            }
        }
    }

    if ($programs.PSObject.Properties.name -contains "choco") {

        # Check if "choco" is already available.
        $chocoExists = Get-Command 'choco' -ErrorAction SilentlyContinue;
        if (!$chocoExists) {
            
            if ($debug) {
                Write-Host "## Installing Chocolatey"
                Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
            } else {
                Write-Progress -Activity "Installing Chocolatey programs..." -CurrentOperation "Installing: Chocolatey"
                Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1')) > $nul
            }

        }

        foreach ($program in $programs.choco) {
            if ($debug) {
                Write-Host "## Installing Choco: $program"
                choco.exe install -y $program 
            } else {
                Write-Progress -Activity "Installing Chocolatey programs..." -CurrentOperation "Installing: $program"
                choco.exe install -y $program > $null
            }
        }
    }
    if (!$debug) {
        Write-Progress -Completed True
    }
}

function resolvePlaceholders([string]$value) {
    $placeholders = @{
        "UserProfile" = "$env:USERPROFILE";
        "LocalAppData" = "$env:LOCALAPPDATA";
        "AppData" = "$env:APPDATA";
        "ProgramFiles" = "$env:PROGRAMFILES";
    }

    $target = $value;
    foreach($placeholder in $placeholders.GetEnumerator())
    {
        $target = $target.Replace("[" + $placeholder.name + "]", $placeholder.value);
    }
    return $target;
}

function setupLinks() {
    if (!(checkForFile -file "links.json")) {
        if ($debug) {
            Write-Host "## links.json not found. Skipping link setup..."
        }
        return
    }
    $links = Get-Content "links.json" | ConvertFrom-Json

    foreach($link in $links.PSObject.Properties) {
        $source = "./settings/" + $link.name
        $source =  [System.IO.Path]::GetFullPath([System.IO.Path]::Combine($PSScriptRoot, $source));

        $target = resolvePlaceholders -Value $link.value;
        $target = [System.IO.Path]::GetFullPath($target);
        
        if (![System.IO.Directory]::Exists($source) -and ![System.IO.File]::Exists($source)) {
            continue;
        }

        if ($debug) {
            Write-Host "## Creating Link: $source -> $target"
            New-Item -Path $target -ItemType SymbolicLink -Value $source -Force
        } else {
            Write-Progress -Activity "Create Folder Links..." -CurrentOperation "$source -> $target"
            New-Item -Path $target -ItemType SymbolicLink -Value $source -Force > $null
        }

    }
    if (!$debug) {
        Write-Progress -Completed True
    }
}

function runPostInstall() {
    if (!(checkForFile -file "post-install-scripts.json")) {
        if ($debug) {
            Write-Host "## post-install-scripts.json not found. Skipping post-install..."
        }
        return
    }

    $postInstallScripts = Get-Content ".\post-install-scripts.json" | ConvertFrom-Json
    foreach ($script in $postInstallScripts) {
        $scriptPath = "./scripts/$script"
        $completePath = [System.IO.Path]::GetFullPath([System.IO.Path]::Combine($PSScriptRoot, $scriptPath));

        if (![System.IO.File]::Exists($completePath)) {
            continue;
        }
        
        if ($debug) {
            Write-Host "## Process Post Install Script: $script";
        } else {
            Write-Progress -Activity "Process Post-Install..." -CurrentOperation "Current Script: $script"
        }
        & $completePath
        
    }
    if (!$debug) {
        Write-Progress -Completed True
    }
}

Write-Host "# Starting Setup"

if ($runInstall) {
    Write-Host "# Starting installing programs"
    installPrograms
}

if ($runLinks) {
    Write-Host "# Starting setting up links"
    setupLinks
}

if ($runPostInstall) {
    Write-Host "# Running post-install scripts"
    runPostInstall
}

Write-Host "# Setup Complete"