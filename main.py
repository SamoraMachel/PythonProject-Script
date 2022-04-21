from colorama import Fore, Style
import click
import subprocess

TICK_SYMBOL = "\u2714"

# finish message to display in the terminal
def print_finish(message : str):
    print(Fore.LIGHTGREEN_EX(f"{TICK_SYMBOL} {message}" ))

def create_files(project_name : str):
    # create the necessary files
    # create the docker files
    with open('./docker.txt', 'r') as docker_file:
        with open('Dockerfile', 'w') as docker:
            docker.writelines(docker_file.readlines())
        

    with open('./dockerignore.txt', 'r') as docker_ignore_file:
        with open('.dockerignore', 'w') as dockerignore:
            dockerignore.writelines(docker_ignore_file.readlines(0))
            
    print_finish("Created all the docker neccessary files")
        
    # create the git files
    with open('./gitignore.txt', 'r') as git_file:
        with open('.gitignore', 'w') as gitignore:
            gitignore.writelines(git_file.readlines())
        subprocess.run('git init .')
        print_finish('Initialized git')
        
    # Addin markdown files
    with open('./license.txt', 'r') as license_file:
        with open('LICENSE.md', 'w') as license:
            license.writelines(license_file.readlines())
        print_finish('Added GNU license')
        
    with open('README.md', 'w') as readme:
        readme.writelines([f"# {project_name}", '\n' "Add a brief description about the project"])
    print_finish("Added a README file")
    
@click.argument('project-name')
def main(project : str) :
    create_files(project)