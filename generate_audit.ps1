# =====================================================================
# Script PowerShell : Génération de audit_notes.md
# À exécuter depuis la racine du projet TRADING_BOT
# =====================================================================

$modulesPath = "modules"
$outputFile = "audit_notes.md"

"# Audit automatique des modules (`$(Get-Date)`)`n" | Out-File $outputFile

Get-ChildItem -Path $modulesPath -Recurse -Filter *.py | ForEach-Object {

    $file = $_.FullName
    $relative = $_.FullName.Replace((Get-Location).Path + "\", "")

    Add-Content $outputFile "`n## Fichier : $relative`n"

    $lines = Get-Content $file
    $lineNumber = 0

    foreach ($line in $lines) {
        $lineNumber++

        if ($line.Trim() -eq '"""') {
            Add-Content $outputFile "- Ligne $lineNumber → Docstring vide"
        }

        if ($line.Trim().StartsWith("#") -and $line.Trim().Length -gt 1) {
            Add-Content $outputFile "- Ligne $lineNumber → Commentaire : $line"
        }

        if ($line -match "TODO|FIXME") {
            Add-Content $outputFile "- Ligne $lineNumber → TODO/FIXME détecté : $line"
        }
    }
}

Add-Content $outputFile "`n---`nAudit terminé automatiquement."
Write-Host "✅ audit_notes.md généré avec succès."
