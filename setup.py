from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT ='-e .'

def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements= [req.replace("\n","") for req in requirements] #readlines reeturn \n after reading every line, so we are replacing the \n wth a blank

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        
    return requirements



setup(
    name = "mlproject", 
    version='0.0.1',
    author='Sunil',
    author_email='sunil.m7176@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)