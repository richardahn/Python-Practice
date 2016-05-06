'''
pipd is a project manager for Python.

pipd is a command-line program.
-   To make a new project, just type:
    'python pipd.py new project_name'
    in your projects folder.
-   To build a project, just type:
    'python pipd.py run'
    inside of your project
'''

## Imports
import sys # To get the arguments
import os # To operate on the system

## Functions
def main():
    # Check if arg size is at least 2
    if (len(sys.argv) < 2):
        print('Not enough args')
        return
    # Check for an operation
    op = sys.argv[1]
    if (op == 'new'):
        # Check if arg size is EXACTLY 3
        if (len(sys.argv) != 3):
            print('New op has bad arguments')
            return
        new_op(sys.argv[2])
    elif (op == 'run'):
        # Check if arg size is EXACTLY 2
        if (len(sys.argv) != 2):
            print('Run op has bad arguments')
            return
        run_op()
    else:
        print('An improper operation was entered')
        return

def run_op():
    os.chdir()

def new_op(directory_name):
    '''
    Creates a new project folder

    Arguments:
    -   directory_name: The name of the new project

    Returns:
    -   None

    Raises:
    -   Nothing
    '''
    print('Making a new project...')
    # Create the project directory
    try:
        project_directory = make_directory(directory_name)
    except DuplicatePathError as e:
        print(e.msg)
        return
    except:
        print('Unknown error')
        return
    # Create a src folder inside
    os.chdir(project_directory)
    src_directory = make_directory('src')
    # Create a main.py file
    os.chdir(src_directory)
    make_file('main.py')
    # Go back to main directory and git init
    os.chdir(project_directory)
    create_config(directory_name)
    # Done
    print('Finished making the project.')

#def create_config(name):
    # Create the config file that will be used by pipd run


#def make_file(name):
    # Get the new file path
    #new_file = os.getcwd() + '\\' + name
    # Check if the file exists
    #open(new_file, 'a')
    #return new_file


def make_directory(name):
    '''
    Makes a folder in the current working directory

    Arguments:
    -   name: The name of the new folder

    Returns:
    -   string: the path of the new folder

    Raises:
    -   DuplicatePathError
    '''
    # Get the new directory path
    new_directory = os.getcwd() + '\\' + name
    # Check if directory exists
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)
    else:
        raise DuplicatePathError('Directory ' + new_directory + ' already exists')
    return new_directory

class DuplicatePathError(Exception):
    def __init__(self, msg):
        self.msg = msg

main()

# Define a path tree data structure
# Define ProjectDirectory
# that contains a hierarchy of path nodes
# The ProjectDirectory is given a project name
# and it makes a project given that name in the current working directory
# it also git inits the root folder
