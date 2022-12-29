# check if Python is installed

if (!(get-command choco)) {
    Write-Output "Chocolatey is not installed, install now..."
    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
}
else {
    Write-Output "Chocolatey is installed."
}

if (!(get-command python)) {
    Write-Output "Python is not installed, installing now..."
    choco install python3
}
else {
    Write-Output "Python is installed, checking for necessary dependencies..."
    if (!(pip freeze | select-string -Pattern "windows-curses")) {
        Write-Output "Windows-Curses packages is not installed, installing it now..."
        pip install windows-curses
    }
    else {
        Write-Output "Python and all dependencies are installed, running script now..."
    }
}

python \\office\office\IT\library\software\programming-projects\python\rogueish.py