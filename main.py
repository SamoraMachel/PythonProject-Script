from colorama import Fore, Style
import click
import os
from pyfiglet import Figlet
from docker import docker_text
from dockerignore import dockerignore_text
from gitignore import gitignore_text
from license import license_text
from mainfile import mainfile_text
from test import test_text
from installation import installation_config, setup_code, setup_cfg

TICK_SYMBOL = "\u2714"
PROJECT_NAME = ""
BASE_PATH = ""


# finish message to display in the terminal
def print_finish(message : str):
    print(Fore.YELLOW + (f"{TICK_SYMBOL} {message}"))
    print(Fore.WHITE, end="")

def create_files(project_name : str):
    # create the necessary files
    # create the docker files
    with open('Dockerfile', 'w') as docker:
        docker.write(docker_text)

    with open('.dockerignore', 'w') as dockerignore:
        dockerignore.write(dockerignore_text)
        print_finish("Created all the docker neccessary files")
        
        
    # Adding markdown files
    with open('LICENSE.md', 'w') as license:
        license.write(license_text)
        print_finish('Added GNU license')
        
    with open('README.md', 'w') as readme:
        readme.writelines([f"# {project_name}", '\n' "Add a brief description about the project"])
        print_finish("Added a README file")
        
    
    # Adding python related files
    with open('main.py', 'w') as mainfile:
        mainfile.write(mainfile_text)
        
    os.system('touch requirements.txt')
    print_finish("Added python default files")
    
def testing():
    # add test folder for test files
    os.system('mkdir tests')
    os.chdir(os.path.join(BASE_PATH, 'tests')) 
    os.system('touch __init__.py')
    with open('test.py', 'w') as testfile:
        testfile.write(test_text)
   

# code to allow our project to be installable
def installation(description):
    os.chdir(BASE_PATH)
    with open('pyproject.toml', 'w') as installationfile:
        installationfile.write(installation_config)
    with open('setup.py', 'w') as setupfile:
        setupfile.write(setup_code)
    with open('setup.cfg', 'w') as configfile:
        configfile.write(setup_cfg(PROJECT_NAME, description, os.getlogin()))
    os.system("pip install -e .")
       

# git initialization
def initialize_git() :
   # create the git files
    with open('.gitignore', 'w') as gitignore:
        gitignore.write(gitignore_text)
        os.system('git init .')
        print_finish('Initialized git')
        
    os.system('git add .')
    os.system(f'git commit -m "Initialized {PROJECT_NAME} project"')
    os.system('git branch -m main')
    print_finish('Commited changes')
    
        
# start virtual environment
def virtualenvironment():
    print_finish('Initializing your virtual environment')
    os.system('pipenv --python3')
    f = Figlet(font='slant')
    print(Fore.YELLOW + f.renderText(f'created {PROJECT_NAME}'))
    os.system('pipenv shell')
    
    

# main execution file 
@click.command('create-project')
@click.argument('project-name')
@click.option("--git", help="Initialize git in the repository")
def main(project_name : str) :
    """Generate a python project with default files setup"""
    os.system(f'mkdir {project_name}')
    
    # set variables for runtime usage
    PROJECT_NAME = project_name
    BASE_PATH = os.path.join(os.getcwd(), PROJECT_NAME)
    
    os.chdir(project_name)
    create_files(project_name)
    
    # virtualenvironment()

    

    
    

if __name__ == '__main__':
    main()