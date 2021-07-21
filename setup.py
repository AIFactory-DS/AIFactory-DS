from setuptools import setup, find_packages
import os

setup(  name='AIFactoryDS',

        version='0.1.11',

        description='Project Skeleton',

        author='yoosunyoung',

        author_email='luysunyoung9@gmail.com',

        url='https://github.com/YooSunYoung',

        license='MIT',

        py_modules=['greetings', 'AbstractProcesses', 'Worker', 'ImageUtilities'],

        python_requires='>=3.8',

        install_requires=[],

        packages=['EasterEggs', 'AIFactoryDS'],

        scripts=['build_project_skeleton'],

        include_package_data=True,

        package_dir={'': "src"},

        package_data={'training': ['formats/training_recipe_format.json']}
)
