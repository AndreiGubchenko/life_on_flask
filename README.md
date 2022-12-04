## Installation

1. Create virtual environment

linux
`python3 -m venv /path/to/new/virtual/environment`

windows
`python -m venv /folder/to/new/virtual/environment`

2. Activate virtual environment 

<venv> - name of the directory where virtual environment is created

Linux:
$ `source <venv>/bin/activate`

Windows PowerShell	

$ `<venv>/bin/Activate.ps1`

or

PS C:\> `<venv>\Scripts\Activate.ps1`

Windows cmd.exe	

C:\> `<venv>\Scripts\activate.bat`

3. Install requirements 

`pip install requirements.txt`

4. Run flask server

`python -m flask run`

5. Open project in browser

http://127.0.0.1:5000
