param(
    [switch] $DryRun,
    [switch] $Help,
    [Parameter(ValueFromRemainingArguments = $true)]
    [object[]] $RemainingArgs = @()
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$PackageName = "ai-gateway"
$AigHomeDirname = ".aig"
$AigCommands = @(
    "aig-server",
    "aig-claude",
    "aig-codex",
    "aig-init",
    "ai-gateway"
)

function Show-Usage {
    @"
Usage: uninstall.ps1 [options]

Removes the AI Gateway uv tool and deletes ~/.aig/.
Does not remove uv, Claude Code, Codex, or the uv-managed Python runtime.

Options:
  -DryRun                Print commands without running them.
  -Help                  Show this help text.
"@
}

function Write-Step {
    param([string] $Message)

    Write-Host ""
    Write-Host "==> $Message"
}

function Format-Argument {
    param([string] $Value)

    if ($Value -match '^[A-Za-z0-9_./:@%+=,\[\]-]+$') {
        return $Value
    }

    return "'" + ($Value -replace "'", "''") + "'"
}

function Test-MissingUvToolError {
    param([string] $Output)

    $normalized = $Output.ToLowerInvariant()
    return (
        $normalized.Contains("not installed") -or
        $normalized.Contains("no tool") -or
        $normalized.Contains("nothing to uninstall")
    )
}

function Add-PathEntry {
    param([string] $PathEntry)

    if ([string]::IsNullOrWhiteSpace($PathEntry)) {
        return
    }

    $separator = [IO.Path]::PathSeparator
    $entries = @()
    if (-not [string]::IsNullOrEmpty($env:Path)) {
        $entries = $env:Path -split [regex]::Escape([string] $separator)
    }

    if ($entries -notcontains $PathEntry) {
        $env:Path = "$PathEntry$separator$env:Path"
    }
}

function Add-UvToPath {
    Add-PathEntry (Join-Path $HOME ".local\bin")
    Add-PathEntry (Join-Path $HOME ".cargo\bin")
}

function Assert-NoAigProcessesRunning {
    $running = @()

    foreach ($commandName in $AigCommands) {
        $processes = @(Get-Process -Name $commandName -ErrorAction SilentlyContinue)
        if ($processes.Count -gt 0) {
            $running += $commandName
        }
    }

    if ($running.Count -gt 0) {
        throw "AI Gateway is still running ($($running -join ', ')). Stop those processes, then rerun uninstall."
    }
}

function Uninstall-AiGateway {
    Add-UvToPath

    if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
        Write-Host "uv not found on PATH; skipping uv tool uninstall."
        return
    }

    Write-Host "+ uv tool uninstall $PackageName"
    if (-not $DryRun) {
        $previousErrorActionPreference = $ErrorActionPreference
        $ErrorActionPreference = "Continue"
        try {
            $output = (& uv tool uninstall $PackageName 2>&1 | Out-String).Trim()
            $exitCode = $LASTEXITCODE
            if ($exitCode -eq 0) {
                return
            }
            if (Test-MissingUvToolError -Output $output) {
                Write-Host "AI Gateway uv tool not installed or already removed; skipping uv tool uninstall."
                return
            }
            if (-not [string]::IsNullOrWhiteSpace($output)) {
                [Console]::Error.WriteLine($output)
            }
            throw "uv tool uninstall $PackageName failed with exit code $exitCode; aborting before deleting ~/.aig."
        }
        finally {
            $ErrorActionPreference = $previousErrorActionPreference
        }
    }
}

function Purge-AigHome {
    $aigHome = Join-Path $HOME $AigHomeDirname
    if (-not (Test-Path -LiteralPath $aigHome)) {
        Write-Host "No AI Gateway config directory at $aigHome; skipping purge."
        return
    }

    $commandText = @(
        "Remove-Item",
        "-LiteralPath",
        (Format-Argument $aigHome),
        "-Recurse",
        "-Force"
    ) -join " "
    Write-Host "+ $commandText"

    if (-not $DryRun) {
        Remove-Item -LiteralPath $aigHome -Recurse -Force
    }
}

if ($Help) {
    Show-Usage
    return
}

if ($RemainingArgs.Count -gt 0) {
    Show-Usage
    throw "Unknown option: $($RemainingArgs -join ' ')"
}

Write-Step "Checking for running AI Gateway processes"
Assert-NoAigProcessesRunning

Write-Step "Removing AI Gateway uv tool"
Uninstall-AiGateway

Write-Step "Purging AI Gateway config and data from ~/.aig"
Purge-AigHome

Write-Host ""
Write-Host "AI Gateway has been removed."
Write-Host "uv, Claude Code, Codex, and the uv-managed Python runtime were left installed."
