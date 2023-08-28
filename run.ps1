#Requires -RunAsAdministrator
param(
    [bool]$runInstall,
    [bool]$runLinks,
    [bool]$runPostInstall
)

if (!$runInstall -and !$runLinks -and !$runPostInstall) {
    $runInstall = $true;
    $runLinks = $true;
    $runPostInstall = $true;
}

function checkForFile([string] $file) {
    $relativeFile = './' + $file;
    $completePath = [System.IO.Path]::GetFullPath([System.IO.Path]::Combine($PSScriptRoot, $relativeFile));
    
    return [System.IO.File]::Exists($completePath);
}

function installPrograms() {
    if (!(checkForFile -file "programs.json")) {
        return
    }

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
            Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1')) > $nul
        }

        foreach ($program in $programs.choco) {
            Write-Progress -Activity "Installing Chocolatey programs..." -CurrentOperation "Installing: $program"

            choco.exe install -y $program > $null
        }
        
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
        return
    }
    $links = Get-Content "links.json" | ConvertFrom-Json

    foreach($link in $links.PSObject.Properties) {
        $source = "./settings/" + $link.name
        $source =  [System.IO.Path]::GetFullPath([System.IO.Path]::Combine($PSScriptRoot, $source));

        $target = resolvePlaceholders -Value $link.value;
        $target = [System.IO.Path]::GetFullPath($target);

        Write-Progress -Activity "Create Folder Links..." -CurrentOperation "$source -> $target"
        
        if (![System.IO.Directory]::Exists($source) -and ![System.IO.File]::Exists($source)) {
            continue;
        }

        New-Item -Path $target -ItemType SymbolicLink -Value $source -Force > $null

    }
    #Write-Progress -Completed True
}

function runPostInstall() {
    if (!(checkForFile -file "post-install-scripts.json")) {
        return
    }

    $postInstallScripts = Get-Content ".\post-install-scripts.json" | ConvertFrom-Json
    foreach ($script in $postInstallScripts) {
        $scriptPath = "./scripts/$script"
        $completePath = [System.IO.Path]::GetFullPath([System.IO.Path]::Combine($PSScriptRoot, $scriptPath));

        if (![System.IO.File]::Exists($completePath)) {
            continue;
        }
        
        Write-Progress -Activity "Process Post-Install..." -CurrentOperation "Current Script: $script"
        & $completePath
        
    }
    Write-Progress -Completed True
}

Write-Host "# Starting Setup"

if ($runInstall) {
    installPrograms
}

if ($runLinks) {
    setupLinks
}

if ($runPostInstall) {
    runPostInstall
}

Write-Host "# Setup Complete"