# Python Project Starter Script 

This is a simple project that reduces redundacy while creating a new python project. 
The project taloir made based on my preferences when I start a new project.

The script does the following :

    - project folder creation
    - creations of related docker files and populates it according to my preference 
    - creations of related git files and populates the gitignore with a generic template
    - creation of README file
    - creation of GNU license file
    - virtual environment creation
    - test folder creation


## Requirement
The project currently support `python 3` only. The project is also onlye supported on linux based system. Support for other operating system will be added later. </br>

Thes user is also requrired to had `pipenv` installed within the system. 
For pip installation procedure use the link below: 

[pipenv installation guidek](https://pypi.org/project/pipenv/)

## Installation
First install the requirements using
```bash
pip install -r requirements.txt 
```

get the relative path of the `main.py` file by using the following command in the terminal

```bash
pwd
```

a sample output will be displayed
 > /home/\<username>/Documents/scripts/create-project-script/

copy the ouptut and move to root using

```bash
cd ~
```

Now, we are going to modify the terminal file so that our terminal so that we can call our script file like a normal command.
Depending on the type of terminal your using there is a file to modify the terminal , for example if your using `bash` then the file will be `.bashrc` or if your using `zsh` then the file will be `.zshrc`.<br/>
Open the relevant file like so:

```bash
nano .bashrc 
```

this will open a terminal based text editor, you will then navigate to the end of the file and add the following

```bash
alias create-project="python3 <path you had copied>/main.py"
```

therefore your added line will look something of sort

```bash
alias create-project="python3 /home/user/Document/create-script/main.py"
```

now you can close your terminal and then open it again so that the changes are effective.


## Usage
Once everything is complete, you can now create you project using the following syntax

`create-project <project-name>`

therefore is will look something of sort

```bash
create-project Test
```

the execution of the program should produce a similar output as below


![output image](./output.png)


