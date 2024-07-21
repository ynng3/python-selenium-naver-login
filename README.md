# python-selenium-naver-login

Python에서 Selenium 을 활용한 네이버 로그인 처리

## 프로젝트 종속성 모듈 패키지

이 프로젝트는 아래와 같은 종속성을 갖습니다.

* [pyperclip](https://pypi.org/project/pyperclip/)
* [PyGetWindow](https://pypi.org/project/PyGetWindow/)
* [selenium](https://pypi.org/project/selenium/)
* [webdrivermangaer](https://pypi.org/project/webdrivermanager/)

## 동작 원리

네이버 아이디와 비밀번호를 사용자에게 입력 받은 후 [모바일 로그인 폼 URL](https://nid.naver.com/nidlogin.login?svctype=262144)으로 이동한 후

실제 사람이 입력하는 것 처럼 클립보드를 사용하여 입력칸에 액션체인을 통한 키보드 입력(Ctrl + V) 입력을 통해 아이디와 비밀번호를 붙여넣기를 하고 버튼 클릭을 처리 합니다.

만약 키보드 입력과 클릭 동작을 통한 로그인 방식을 사용하지 않을 경우 네이버에서 로봇으로 판단하여 캡챠인증을 요구 하기 때문에 해당 기능을 사용 하는 것을 채택 하였습니다.

## Chrome 자동화 브라우저 숨김 방법

원래라면 selenium의 headless 옵션을 사용하면 되지만 네이버에서 headless 모드로 브라우징을 하면 차단하는 것을 확인하였습니다.

따라서, 이 프로젝트에서는 `pygetwindow` 모듈을 통해 창을 숨김 처리하여 보이지 않게 처리합니다.

### pygetwindow 활성화 방법

```py
# pygetwindow 옵션 설정(수정 전)
#window = gw.getWindowsWithTitle("Chrome")[0]
#window.minimize()  # 최소화
#window.hide()      # 완전히 숨기기
```

```py
# pygetwindow 옵션 설정
window = gw.getWindowsWithTitle("Chrome")[0]
window.minimize()  # 최소화
window.hide()      # 완전히 숨기기
```

위 코드를 아래 코드와 같이 주석을 해제합니다.

## 주의사항

이 인증 기능을 통해 봇을 개발하여 네이버 측에 허가 받지 않고 개인정보를 무단으로 수집하는 경우 네이버 측에서 법적 책임을 물 수 있으며 이로 인한 법적 책임은 해당 봇을 개발한 개발자 및 사용자 본인에게 있으며, 이 프로젝트의 [기고자](https://github.com/ynng3)는 어떠한 책임도 지지 않습니다.

학습 및 교육용으로만 사용하시기를 당부 드립니다.

### 로봇 수집에 관한 네이버 약관

[네이버 약관 및 개인정보 보호(로봇의 검색결과 수집에 대한 네이버의 정책)](https://policy.naver.com/policy/search_policy.html)