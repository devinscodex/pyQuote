# check if Python is installed

if (!(get-command choco)) {
    Write-Output "Chocolatey is not installed, install now..."
    Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
}
else {
    Write-Output "Choco ok"
}

if (!(get-command python)) {
    Write-Output "Python is not installed, installing now..."
    choco install python
}
else {
    Write-Output "Python is installed, checking for necessary dependencies..."
    if (!(python -m pip freeze | select-string -Pattern "windows-curses")) {
        Write-Output "Windows-Curses package is not installed, installing now..."
        pip install windows-curses
    }
}

# all dependencies installed, run program
python \\office\office\IT\library\software\programming-projects\python\rogueish.py