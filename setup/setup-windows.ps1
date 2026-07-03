# Windows setup — link Claude Code dirs to this repo (junctions, no admin needed)
# Prereq: install git + Claude Code, run `claude` once (creates %USERPROFILE%\.claude), then:
#   powershell -ExecutionPolicy Bypass -File .\setup\setup-windows.ps1
$repo = Split-Path $PSScriptRoot -Parent
$claude = "$env:USERPROFILE\.claude"
if (-not (Test-Path $claude)) { New-Item -ItemType Directory -Force -Path $claude | Out-Null }

# 1) agents + skills -> repo
foreach ($d in @('agents', 'skills')) {
    $target = "$claude\$d"
    if (Test-Path $target) { Rename-Item $target "$target.bak" -Force }
    cmd /c mklink /J "$target" "$repo\$d"
}

# 2) per-project memory -> repo\memory
#    Claude Code keys memory to the working directory. ALWAYS start claude from the
#    repo folder on this machine, so the project slug below matches.
$slug = ($repo -replace '[:\\/]', '-')
$projDir = "$claude\projects\$slug"
New-Item -ItemType Directory -Force -Path $projDir | Out-Null
$mem = "$projDir\memory"
if (Test-Path $mem) { Rename-Item $mem "$mem.bak" -Force }
cmd /c mklink /J "$mem" "$repo\memory"

Write-Host ""
Write-Host "DONE. Junctions created:"
Write-Host "  $claude\agents  -> $repo\agents"
Write-Host "  $claude\skills  -> $repo\skills"
Write-Host "  $mem -> $repo\memory"
Write-Host ""
Write-Host "If Claude Code creates a DIFFERENT folder under $claude\projects when you run it"
Write-Host "from the repo (slug mismatch), delete that new empty 'memory' dir and re-point:"
Write-Host "  cmd /c mklink /J <that-projects-dir>\memory $repo\memory"
