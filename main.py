from colorama import Fore, Style
import click
import os
from pyfiglet import Figlet
from docker import docker_text
from dockerignore import dockerignore_text
from gitignore import gitignore_text
from license import license_text
from mainfile import mainfile_text

TICK_SYMBOL = "\u2714"


# finish message to display in the terminal
def print_finish(message : str):
    print(Fore.LIGHTGREEN_EX + (f"{TICK_SYMBOL} {message}"))

def create_files(project_name : str):
    # create the necessary files
    # create the docker files
    with open('Dockerfile', 'w') as docker:
        docker.write(docker_text)

    with open('.dockerignore', 'w') as dockerignore:
        dockerignore.write(dockerignore_text)
        print_finish("Created all the docker neccessary files")
        
    # create the git files
    with open('.gitignore', 'w') as gitignore:
        gitignore.write(gitignore_text)
        os.system('git init .')
        print_finish('Initialized git')
        
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
    
    # add test folder for test files
    os.system('mkdir test')      

@click.command('create-project')
@click.argument('project-name')
def main(project_name : str) :
    """Generate a python project with default files setup"""
    os.system(f'mkdir {project_name}')
    os.chdir(project_name)
    # if(os.path.exists(os.path.join(os.getcwd(), project_name))):
    create_files(project_name)
    os.system('git add .')
    os.system(f'git commit -m "Initialize {project_name} project"')
    os.system('git branch -m main')
    print_finish('Commited changes')
    print_finish('Initializing your virtual environment')
    os.system('pipenv --python 3')
    os.system('pipenv shell')
    
    f = Figlet(font='slant')
    print(Fore.YELLOW + f.renderText(f'{project_name} CREATED'))
    
    

if __name__ == '__main__':
    main()