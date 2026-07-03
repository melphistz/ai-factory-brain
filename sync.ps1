# One-shot sync for Windows: run at session start AND end.
#   powershell -ExecutionPolicy Bypass -File .\sync.ps1
Set-Location $PSScriptRoot
git pull --rebase --autostash
git add -A
$stamp = Get-Date -Format "yyyy-MM-dd_HHmm"
git commit -m "sync $stamp @$env:COMPUTERNAME" 2>$null
if ($LASTEXITCODE -ne 0) { Write-Host "nothing new to commit" }
git push
Write-Host "SYNCED."
