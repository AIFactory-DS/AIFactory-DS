# AIFactoryDS
KOREAN version: [README(KOR)](documents/README.KOR.md)

## For Users
I recommend not to use this package YET other than members of `AIFactory`.

## For Developers

### Environment set-up
1. Clone the repository.
    
   ```
   git clone git@github.com:AIFactory-DS/AIFactory-DS.git
   ```

2. Add the absolute path of `src` directory to the `PYTHONPATH` of this project.
   This can be done by the IDE or the command below.
   ```
   # assuming you're in the root directory of this project.
   export PYTHONPATH=$PYTHONPATH:$(pwd)/src/
   ```
3. Install requirements. Please note that this requirements are different from the requirements in `setup.py`. 
   `env/requirements` contains pre-requisites for the development of this project, 
   not the pre-requisites of `AIFactoryDS` package.
   ```
   pip install env/requirements
   ```
   
### Build and Deploy

This project uses `bdist_wheel` for building and packaging and `twine` for the deployment.
```
# Please make sure you set the right `version` in `setup.py`
python setup.py bdist_wheel
# {VERSION} should be set as the same tag that was specified in `setup.py`
twine upload dist/AIFactoryDS-{VERSION}.whl 
```

### Project Structure
```
├── bin: executable scripts
├── documents
├── env: requirements
├── formats: sample formats for recipes
└── src: all python source code of the project
```

After you build the package, the directories below will be created.
Please add the directories in the `.git/info/exclude` file.
```
├── AIFactoryDS.egg-info
├── build
└── dist: contains .whl files
```