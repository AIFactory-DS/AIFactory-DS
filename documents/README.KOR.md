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

### 프로젝트 구조
```
├── bin: 실행가능한 스크립트
├── documents
├── env: 환경관련 명세서
├── formats: 레시피 및 포맷 예시 파일
└── src: 모든 파이썬 소스코드
```

빌드 하고 난 후에는 아래 디렉토리들이 추가 되니 개발 편의를 위해 `.git/info/exclude`에 해당 디렉토리들을 추가할 것. 
```
├── AIFactoryDS.egg-info
├── build: 빌드된 파이썬 패키지
└── dist: .whl 파일이 저장된 디렉토리
```