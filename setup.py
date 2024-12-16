from setuptools import find_packages, setup 
from typing import List 


hyphen_e ='-e .'

def install_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements 
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]
        if hyphen_e in requirements:
            requirements.remove(hyphen_e)
    return requirements   

setup(
    name='ML_project',
    version='0.0.1',
    author='Faiyaz Kadhar Kani',
    author_email='faiyazfab5800@gmail.com',
    packages=find_packages(),
    install_requires=install_requirements('requirements.txt')
)
