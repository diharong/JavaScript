# JavaScript 03

# 참조 자료형 01

## 함수 Function

- 참조 자료형에 속하며 모든 함수는 Function object

- 원시 자료형은 불변값이었다면, 참조자료형은 객체의 주소가 저장되는 자료형으로 가변적이다.

### 함수 정의

- 함수 구조

```javascript
function name([param[, param, [..., param]]]) {
    statements
    return value
}
```

함수의 구조에 따라서 함수를 작성할 수 있는 방법이 크게 두가지가 있다.

1. 선언식 - 함수 정의 구조와 거의 동일하다.

```javascript
function funcName() {
  statements;
}
```

2. 표현식 - 변수의 할당개념으로 시작 함수의 이름을 변수명으로 쓰고 이름이 없는 함수의 표현식이 나타난다.

```javascript
const funcName = function () {
  statements;
};
```

= > 선언식과 표현식은 함수를 호출할 땐 동일하다.
하지만 **_함수를 정의할 때_** 차이가 발생한다.

1. 선언식 (함수 그 자체로 선언하느냐)

```javascript
function add(num1, num2) {
  return num1 + num2;
}

add(1, 2); // 3
```

2. 표현식 (변수에 할당하여 선언하느냐)

```javascript
const sub = function (num1, num2) {
  return num1 - num2;
};

sub(2, 1); // 1
```

기능상의 차이도 존재한다.

- 함수 선언식 특징
  - 호이스팅 됨 (선언이 끌어올려지는 현상)
  - 코드의 구조와 가독성 면에서는 표현식에 비해 장점이 있음

```javascript
add(1, 2); // 3 add라는 함수가 아래에서 선언됨에도 불구하고 에러가 발생하지 않음

function add(num1, num2) {
  return num1 + num2;
}
```

- 함수 표현식 특징
  - 호이스팅 되지 않음
    - 변수 선언만 호이스팅되고 함수 할당은 실행 시점에 이루어짐
  - 함수 이름이 없는 '익명 함수'를 사용할 수 있음

```javascript
sub(2, 1); // ReferenceError : Cannot access 'sub' before initialization 참조에러

const sub = function (num1, num2) {
  return num1 - num2;
};
// sub 라는 변수이름만 호이스팅이 된다.
// 함수는 할당되지 않는다. 함수가 실행될 때 할당된다. 메모리를 미리 쓰지않는다.
```

- 함수 표현식 사용을 권장하는 이유

1. 예측 가능성

   - 호이스팅의 영향을 받지 않아 코드의 실행 흐름을 더 명확하게 예측할 수 있음

2. 유연성

   - 변수에 할당되므로 함수를 값으로 다루기 쉬움

3. 스코프 관리
   - 블록 스코프를 가지는 let이나 const와 함께 사용하여 더 엄격한 스코프 관리가 가능

---

---

## 매개변수 정의 방법

1. 기본 함수 매개변수
2. 나머지 매개변수

---

1. 기본 함수 매개변수
   - 전달하는 인자가 없거나 undefined가 전달될 경우 이름 붙은 매개변수를 기본값으로 초기화

```javascript
const greeting = function (name = "Anonymous") {
  return `Hi, ${name}`;
};

console.log(greeting()); // Hi, Anonymous

// 전달하는 인자가 없어 기본값인 Anonoymous 로 출력
```

2. 나머지 매개변수
   - 임의의 수 인자를 자바스크립트에서는 **_'배열' (로 처리함)_** 로 허용하여 가변인자를 나타내는 방법
   - 작성 규칙
     - 함수 정의 시 나머지 매개변수는 하나만 작성할 수 있음
     - 나머지 매개변수는 함수 정의에서 매개변수 마지막에 위치해야 함

```javascript
const myFunc = function (param1, param2, ...restParams) {
  // 자바스크에서는  ... 은 전개구문이라고 함 , 여기서는 나머지 매개변수를 처리하기 위한 구문으로 작성됨
  return [param1, param2, restParams];
};

console.log(myFunc(1, 2, 3, 4, 5)); // [1, 2, [3, 4, 5]]
console.log(myFunc(1, 2)); // [1, 2, []]

// 기본적으로 2개의 위치인자를 받게 되고, 그 이후의 나머지는 임의의 인자의 개수를 처리하게 된다.
// 나머지 매개변수는 함수 정의에서 매개변수 마지막에 위치해야한다.
```

---

- JS 의 독특한 동작 원리
  - JS 는 매개변수와 인자의 개수 불일치를 허용해준다!

1. 매개변수 개수 > 인자 개수
   - 누락된 인자는 undefined 로 할당

```javascript
const threeArgs = function (num1, num2, num3) {
  return [num1, num2, num3];
};

console.log(threeArgs()); // [undefined, undefined, undefined]
// 개수가 부족하면 undefined 으로 출력
console.log(threeArgs(1)); // [1, undefined, undefined]

console.log(threeArgs(1, 2)); // [1, 2, undefined]

// POINT ) 에러를 발생시키지 않음!!!!!
```

2. 매개변수 개수 < 인자 개수
   - 초과 입력한 인자는 사용하지 않음(무시)

```javascript
const noArgs = function () {
  return 0;
};

console.log(noArgs(1, 2, 3)); // 인자를 강제로 넣기
// 에러 뜨지않고 return 0 이 뜬다. 그냥 무시한 것!
```

---

---

#### Spread syntax 전개구문 ' ... '

- 배열이나 문자열과 같이 반복 가능한 항목을 펼쳐내는 역할
- 전개 대상에 따라 역할이 다름
  - 배열이나 객체의 요소를 개별적인 값으로 분리하거나
    다른 배열이나 객체의 요소를 현재 배열이나 객체에 추가할 수 있음 등

여기서는 함수 관련된 전개구문만 보도록 한다.

- 전개 구문 활용처

1. 함수와의 사용

   - 함수 호출 시 인자 확장
   - 나머지 매개변수 (압축)

2. 객체와의 사용 (객체파트에서 진행)
3. 배열와의 사용 (배열파트에서 진행)

---

- 함수와의 사용

1. 인자 확장 (함수 호출 시)

- 인자 개수 일치

```javascript
let numbers = [1, 2, 3]; // 개수 일치

function myFunc(x, y, z) {
  return x + y + z;
}

// console.log(myFunc(numbers[0], numbers[1], numbers[2])) //원래는 직접 인덱스에 넣어야해
console.log(myFunc(...numbers)); // 6
```

- 인자의 개수가 다를 경우

```javascript
let numbers2 = [1, 2]; // 개수 불일치

function myFunc(x, y, z) {
  return x + y + z;
}

console.log(myFunc(...numbers)); // NaN

// NaN 이 나오는 이유
// JS 에서는 불일치를 허용하므로 z 값은 undefined 으로 출력된다.
// 따라서 x+y+z 는 1+2+undefined 이므로 전개자체를 진행되지만 더하기는 진행되지 않아 NaN 출력
```

---

---

#### 화살표 함수 표현식

(JS가 굉장히 좋아함)

- 함수 표현식의 간결한 표현법

```javascript
const arrow = function (name) {
  return `hello, ${name}`;
};
```

위의 식과 아래의 식은 같다.

```javascript
const arrow = (name) => `hello, ${name}`;
```

- 화살표 함수 작성 과정

1. 1단계 : function 키워드 제거 후 매개변수와 중괄호 사이에 화살표(=>) 작성

2. 2단계 : 함수의 매개변수가 하나 뿐이라면, 매개변수의 '()' 제거 가능
   (단, 생략하지 않는 것을 권장)

3. 3단계 : 함수 본문의 표현식이 한 줄이라면, '{}'와 'return' 제거 가능

```javascript
const arrow1 = function (name) {
  return `hello, ${name}`;
};
// 1. function 키워드 삭제 후 화살표 작성
const arrow2 = (name) => {
  return `hello, ${name}`;
};

// 2. 인자의 소괄호 삭제 (인자가 1개일 경우에만 가능)
const arrow3 = (name) => {
  return `hello, ${name}`;
};

// 3. 중괄호와 return 삭제 (함수 본문이 return을 포함한 표현식 1개일 경우에만 가능)
const arrow4 = (name) => `hello, ${name}`;

// 명시도가 떨어진다.
```

일반 함수식 적고 화살표 함수로 바꿔보기

---

---

- 화살표 함수 심화

1. 인자가 없다면 () or \_ 로 표시 가능

```javascript
const noArgs1 = () => "No args";
const noArgs2 = (_) => "No args";
```

2-1. object 를 return 한다면 return 을 명시적으로 작성해야 함

```javascript
const returnObject1 = () => {
  return { key: "value" };
};
```

2-2. return을 작성하지 않으려면 객체를 소괄호로 감싸야 함

```javascript
const returnObject2 = () => ({ key: "value" });
```

💖 mdn 문서 활용하자 !!!!
