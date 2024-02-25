------Install python and dependencies on localhost------
1 - Clone repository Git.
2 - Install python: dowload in https://www.python.org/downloads/. Be sure to select the option to add Python to the PATH during installation.
3 - Validate that python is installed by running cmd. Running "python --version".
4 - Install PIP: Download the "get-pip.py" file from https://bootstrap.pypa.io/get-pip.py. Open CMD and runnung "python get-pip.py". Validate that it was installed by running this line in cmd "pip --version".
5 - Install environment:
    1 - In the windows terminal or vs code position yourself in the program folder. Example "cd C:\Users\TuNombreDeUsuario\MyProyect".
    2 - Run command "python -m venv venv" (venv is a python library, and the second venv indicates the name of the environment, let's always use that by default). A venv folder will be created in the repository.
    3 - Active the environment run command "./Venv/Scripts/Activate.ps1". If it is activated correctly, in the vscode terminal the name of the environment will appear between parentheses.
        In case the environment cannot be activated, follow these steps:
            1 - Open PowerShell with administrator privileges: Right-click on the Start menu and select "Windows PowerShell (Admin)".
            2 - Verify the script execution policy: In the PowerShell window, run the following command to verify the current script execution policy settings:
                "Get-ExecutionPolicy". if it's wrong, it will show "Restricted".
            3 - Change the script execution policy: If the current policy does not allow script execution, you can change it using the following command:
                "Set-ExecutionPolicy RemoteSigned".
6 - Install Library:
    1 - Inside the repository there is a file with all the libraries to install (requirements.txt). Run the code "pip install -r requirements.txt" in the terminal to install all the libraries. In this way we make sure that everyone has the same versions of the library.

------Add new python library------
In the terminal you can install libraries using pip. Example "pip install python-multipart".
When installing a library remember to update "requirements.txt" file when new libraries are added using "pip freeze > requirements.txt" command in terminal.

----- PYLINT -----
To run linting rules with pylint, we need to have the virtual environment running and navigate to the 'src' folder. From here, we can run pylint on the entire 'src' folder with 'pylint *' or on specific folders/files as needed, for example, 'pylint services/*' or 'pylint services/maizplus.py'.
