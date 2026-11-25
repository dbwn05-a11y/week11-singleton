# 11주차 실습: Singleton 패턴

## 실행 환경

- 언어: Python
- 버전: CPython 3.13.3 (64비트)
- 운영체제: Windows 11
- 단일 프로세스·단일 스레드로 실행하며 추가 패키지는 필요 없다.

## 실행 방법

저장소를 내려받고 `main.py`와 `singleton.py`가 있는 폴더에서 PowerShell을 연다.
확인할 때 사용한 실행 명령은 다음과 같다.

```powershell
& "$env:USERPROFILE\AppData\Local\Programs\Python\Python313\python.exe" main.py
```

`python` 명령으로 Python 3를 실행할 수 있다면 `python main.py`를 입력해도 된다.

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

인스턴스는 `SingletonCounter` 클래스의 `__instance`에 저장한다.
`get_instance()`는 처음 호출할 때만 객체를 만들고, 그다음부터는 같은 객체를 돌려준다.
`SingletonCounter()`로 직접 만들려고 하면 오류가 나도록 했다.
`first is second`가 `True`이므로 두 변수는 같은 객체를 가리킨다.
`first`로 카운터를 올린 뒤 `second.count`도 1로 나와, 두 변수가 같은 카운터 값을 공유한다는 것을 확인했다.
