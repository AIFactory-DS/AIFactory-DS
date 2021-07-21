# AIFactoryDS (KOR)

## 유저 가이드
`AIFactoryDS` 팀 이외의 분들께는 아직 사용을 권하지 않습니다.
## 개발자 가이드

### 환경설정
1. 소스코드 및 기타 문서 다운로드
    
   ```
   git clone git@github.com:AIFactory-DS/AIFactory-DS.git
   ```

2. `src` 디렉토리의 절대경로를 해당 프로젝트의 `PYTHONPATH` 에 추가.
   Pycharm 등의 개발 툴에서도 설정이 가능함.
   ```
   # assuming you're in the root directory of this project.
   export PYTHONPATH=$PYTHONPATH:$(pwd)/src/
   ```
3. 필요한 모듈 설치. 아래 `env/requirements`에 명시된 패키지들은 개발자를 위한 패키지로
   `AIFactoryDS`패키지 설치에 필요한 패키지들이 아니므로 주의할 것.
   `AIFactoryDS`패키지 설치에 필요한 패키지들은 `setup.py`에 명시함.
   ```
   pip install env/requirements
   ```
   
### 빌드와 배포

해당 프로젝트는 `bdist_wheel` 로 빌드하고 패키징한 후에 `twine` 로 배포함.
```
# Please make sure you set the right `version` in `setup.py`
python setup.py bdist_wheel
# {VERSION} should be set as the same tag that was specified in `setup.py`
twine upload dist/AIFactoryDS-{VERSION}.whl 
```