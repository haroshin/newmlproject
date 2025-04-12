from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this is the function for to get the list of requirements from the file

    '''
    HYPEN_E_DOT='-e .'
    requirements=[]
    with open(file_path) as path_obj:# reading the file path
        requirements=path_obj.readline()# reading the first line of the file
        [req.replace("\n","")for req in requirements]# removing the newline character in the each and every line in the txt file.
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='haro',
    author_email='haroshinkk2002@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")


)