from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e.'
def get_requirements(file_path:str)->List[str]:
    '''This function is going to return list of requirement for a given file_path'''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n","")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='ML-Project1',
    version='0.0.1',
    author='Keshav Bainsla',
    author_email='keshavbainsla3435@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')




)