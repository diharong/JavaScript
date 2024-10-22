# SSAFY 12기 JavaScript 라이브 자료

| 진행일 | 주제                    |
| ------ | ----------------------- |
| 10/21  | DOM                     |
| 10/22  | Basic Syntax            |
| 10/23  | Reference Type 01       |
| 10/24  | Reference Type 02       |
| 10/25  | Reference Type 03       |
| 10/28  | Controlling Event       |
| 10/29  | Asynchronous JavaScript |
| 10/30  | Ajax with Django        |

# 자바스크립트

## 변수

변수 선언 키워드 3가지

1. let
2. const
3. ***

#### let

- 블록 스코프 (block scope)를 갖는 지역 변수를 선언
- 재할당 가능
- 재선언 불가능
- ES6에서 추가

```javascript
let number = 10; // 1. 선언 및 초기값 할당
number = 20; //2. 재할당
```

```javascript
let number = 10; //1. 선언 및 초기값 할당
let number = 20; //2. 재선언 불가능
```

#### const (상수의 약자 = 변할수없는 값:상수)

- 블록 스코프를 갖는 지역 변수를 선언
- 재할당 불가능
- 재선언 불가능
- ES6에서 추가

```javascript
const number = 10; //1. 선언 및 초기값 할당
number = 10; //2. 재할당 불가능
```

```javascript
const number = 10; //1. 선언 및 초기값 할당
const number = 10; //2. 재선언 불간으
```

```javascript
const number // const' declarations must be initialized.
선언 시 반드시 초기값 설정 필요
```

| let과 const 의 유일한 차이점은 _재할당 여부_ 이다. 💖💖💖💖

---

## 식별자(변수명) Naming case

1. 카멜 케이스(camelCase) -- 보통 이걸로 많이 씀

   - 변수, 객체, 함수에 사용

2. 파스칼 케이스 (PascalCase)

   - 클래스, 생성자에 사용

3. 대문자 스네이크 케이스(SNAKE_CASE)
   - 상수(constants)에 사용

---

---

### 블록 스코프 (block scope)

- if, for 함수 등의 '중괄호({}) 내부'를 가리킴
- 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능

---

- 어떤 변수 선언 키워드를 사용해야 할까?

  - const를 기본으로 사용!
  - 필요한 경우에만 let으로 전환
    - 재할당이 필요한 경우 (값이 변경되는 변수구나~)
    - let을 사용하는 것을 해당 변수가 의도적으로 변경될 수 있음을 명확히 나타냄
    - 코드의 유연성을 확보하면서도 const의 장점을 최대한 활용할 수 있음

- const를 기본으로 사용해야 하는 이유?

1. 코드의 의도 명확화

   - 해당 변수가 재할당되지 않을 것임을 명확히 표현
   - 개발자들에게 변수의 용도와 동작을 더 쉽게 이해할 수 있도록 해준다.

2. 버그 예방
   - 의도치 않은 변수 값 변경으로 인한 버그를 예방
   - 큰 규모의 프로젝트나 팀 작업에서 중요

---

---

---

## DOM 문서객체모델

The Document Object Model
웹 페이지(Document)를 구조화된 객체로 제공하여 프로그래밍 언어가 페이지 구조에 접근할 수 있는 방법을 제공

- 문서 구조, 스타일, 내용 등을 변경할 수 있도록 함

- javascript 기능 중에서도 웹 브라우저에서 웹 페이지의 동적인 기능을 구현하는 것에 초점을 맞춰 알아보자

- javaScript 실행 환경 종류

1. HTML script 태그

```html
<body>
  <script>
    console.log("hello");
  </script>
</body>
```

2. js 확장자 파일

3. 브라우저 Console

---

### DOM API

- 다른 프로그래밍 언어가 웹 페이지에 접근 및 조작 할 수 있도록 페이지 요소들을 객체 형태로 제공하며 이에 따른 메서드 또한 제공

#### document 객체 ✔

= 웹 페이지를 나타내는 DOM 트리의 최상위 객체
-> HTML 문서의 모든 콘텐츠에 접근하고 조작할 수 있는 진입점
= DOM 에서 모든 요소, 속성, 텍스트는 하나의 객체
= 모두 document 객체의 하위 객체로 구성됨

- DOM tree

  - HTML 태그를 나타내는 elements의 node는 문서의 구조를 결정
  - 이들은 다시 자식 node를 가질 수 있음(ex. document.body)
    - 객체 간 상속 구조가 존재

- DOM 핵심
  : 문서의 요소들을 객체로 제공하여 다른 프로그래밍 언어에서 접근하고 조작할 수 있는 방법을 제공하는 API

---

---

### DOM 선택

- DOM 조작 시 기억해야 할 것

웹 페이지를 '동적'으로 만들기 == 웹 페이지를 '조작'하기

- 조작순서

1. 조작 하고자 하는 요소를 선택(또는 탐색)
2. 선택된 요소의 콘텐츠 또는 속성을 조작

#### 선택 메서드 💖

- document.querySelector()
  요소 한개 선택
- document.querySelectorAll()
  요소 여러 개 선택

---

- document.querySelector(selector)

  - 제공한 선택자와 일치하는 element 한 개 선택
  - 제공한 선택자를 만족하는 첫 번째 element 객체를 반환(없다면 null 반환)

- document.querySelectorAll(selector)

  - 제공한 선택자와 일치하는 여러 element를 선택
  - 제공한 선택자를 만족하는 NodeList (배열 또는 리스트) 를 반환

---

### DOM 조작

1. 속성(attribute) 조작
   - 클래스 속성 조작
   - 일반 속성 조작
2. HTML 콘텐츠 조작
3. DOM 요소 조작
4. 스타일 조작

---

#### 속성 조작

1. 클래스 속성 조작
2. 일반 속성 조작

- 클래스 속성 조작
  ` 'classList' property`
  = 요소의 클래스 목록을 DOMTokenList(유사 배열) 형태로 반환

1. classList 메서드

- element.classList.add()
  - 지정한 클래스 값을 추가
- element.classList.remove()
  - 지정한 클래스 값을 제거
- element.classList.toggle()

  - 클래스가 존재한다면 제거하고 false를 반환
    (존재하지 않으면 클래스를 추가하고 true를 반환)

- 일반 속성 조작

1. 일반 속성 조작 메서드

- Element.getAttribute()
  - 해당 요소에 지정된 값을 반환(조회)
- Element.getAttribute(name, value)
  - 지정된 요소의 속성 값을 설정
  - 속성이 이미 있으면 기존 값을 갱신(그렇지 않으면 지정된 이름과 값으로 새 속성이 추가)
- Element.removeAttribute()
  - 요소에서 지정된 이름을 가진 속성 제거

---

3. HTML 콘텐츠 조작
`'textContent' property`
요소의 텍스트 콘텐츠를 표현
 <p>lorem </p>

---

#### DOM 요소 조작

- document.createElement(tagName) = 요소 생성

  - 작성한 tagName의 HTML 요소를 생성하여 반환

- Node.appendChild() = 요소 추가

  - 한 Nod를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입
  - 추가된 Node 객체를 반환

- Node.removeChild()
  - DOM 에서 자식 Node를 제거
  - 제거된 Node를 반환

---

- style 조작
  `'style' property`
  해당 요소의 모든 style 속성 목록을 포함하는 속성

---

참고

Node

- DOM 의 기본 구성 단위
