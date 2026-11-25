# 11주차 실습: Singleton 패턴

Python으로 싱글톤 카운터를 구현하고, 서로 다른 변수가 같은 객체와 상태를 공유하는지 확인했다.

## 실행 환경

- 언어: Python
- 확인한 버전: CPython 3.13.3 (64비트)
- 운영체제: Windows 11
- 단일 프로세스·단일 스레드 환경이며, 별도로 설치할 패키지는 없다.

## 파일 구성

- `singleton.py`: 인스턴스를 하나만 보관하는 `SingletonCounter` 클래스
- `main.py`: 객체 동일성, 상태 공유, 직접 생성 제한 확인 코드

## 실행 방법

저장소를 내려받은 뒤, `main.py`와 `singleton.py`가 있는 폴더에서 터미널을 열어 실행한다.
Windows PowerShell에서 설치된 Python 3.13을 직접 지정해 확인한 명령은 다음과 같다.

```powershell
& "$env:USERPROFILE\AppData\Local\Programs\Python\Python313\python.exe" main.py
```

Python 3가 `python` 명령으로 연결된 환경에서는 `python main.py`로도 실행할 수 있다.

## 실행 결과

```text
같은 인스턴스인가: True
변경 전 second.count: 0
first로 1 증가 후 second.count: 1
다시 요청한 인스턴스도 같은가: True
다시 요청한 후 third.count: 1
직접 생성 제한: SingletonCounter.get_instance()를 사용하세요.
```

## 구현 설명

만든 인스턴스는 `SingletonCounter` 클래스의 `__instance` 변수에 보관한다.
`get_instance()`는 이 변수가 `None`일 때만 객체를 만들고, 다음 요청부터는 보관한 객체를 돌려주므로 새 객체를 만들거나 카운터를 초기화하지 않는다.
`SingletonCounter()`를 직접 호출하면 `__new__()`에서 오류가 나도록 해서, `get_instance()`를 통해 인스턴스를 얻도록 했다.
`first is second`가 `True`로 나오고 `first`로 카운터를 1 증가시켰을 때 `second.count`도 1이 되므로, 두 변수가 같은 인스턴스와 상태를 공유한다는 것을 확인할 수 있다.
