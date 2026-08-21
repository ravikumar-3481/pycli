
Write-Host "Detecting Python Scripts folder..." -ForegroundColor Cyan

try {
    $scriptsPath = python -c "import sysconfig; print(sysconfig.get_path('scripts'))"
} catch {
    Write-Host "ERROR: Could not run Python. Make sure Python is installed and accessible as 'python'." -ForegroundColor Red
    exit 1
}

if (-not $scriptsPath) {
    Write-Host "ERROR: Could not determine the Scripts folder path." -ForegroundColor Red
    exit 1
}

Write-Host "Found Scripts folder: $scriptsPath" -ForegroundColor Green

# Get current User PATH
$currentPath = [Environment]::GetEnvironmentVariable("Path", "User")

# Check if it's already present (case-insensitive, trimmed)
$alreadyPresent = $currentPath -split ';' | Where-Object { $_.Trim().ToLower() -eq $scriptsPath.Trim().ToLower() }

if ($alreadyPresent) {
    Write-Host "This folder is already in your PATH. Nothing to do." -ForegroundColor Yellow
} else {
    $newPath = $currentPath.TrimEnd(';') + ";" + $scriptsPath
    [Environment]::SetEnvironmentVariable("Path", $newPath, "User")
    Write-Host "Successfully added to PATH permanently!" -ForegroundColor Green
    Write-Host ""
    Write-Host "IMPORTANT: Close this PowerShell window and open a NEW one for the change to take effect." -ForegroundColor Magenta
}

Write-Host ""
Write-Host "After opening a new terminal, test with:  mkproject --help" -ForegroundColor Cyan