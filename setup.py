from setuptools import setup, find_packages
import os

setup(  name='AIFactoryDS',

        version='0.1.13',

        description='AI Project Skeleton and Utilities',

        author='yoosunyoung',

        author_email='luysunyoung9@gmail.com',

        url='https://github.com/YooSunYoung',

        license='MIT',

        py_modules=['greetings', 'AbstractProcesses', 'Worker', 'ImageUtilities'],

        python_requires='>=3.8',

        install_requires=['numpy~=1.21.1'],

        package_dir={'': "src/"},

        packages=find_packages('src'),

        scripts=['bin/build_project_skeleton'],

        include_package_data=True,


        package_data={'training': ['formats/training_recipe_format.json']}
)
