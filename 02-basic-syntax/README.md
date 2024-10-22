# JavaScript 02 Basic syntax

# 데이터 타입

1. 원시 자료형 (primitive type)
   : 변수에 값이 직접 저장되는 자료형(불변, 값이 복사)

- Number, String, Boolen, null, undefined

- 변수에 할당될 때 값이 복사됨
  => 변수 간에 서로 영향을 미치지 않음

```javascript
const a = "bar";
console.log(a); // bar

a.toUpperCase();
console.log(a); // bar
```

```javascript
let a = 10;
let b = a;
b = 20;
console.log(a); // 10
console.log(b); // 20
```

2. 참조 자료형 (Reference type)
   : 객체의 주소가 저장되는 자료형(가변, 주소가 복사)

- Objects(Object, Array, Function)

- 객체를 생성하면 객체의 메모리 주소를 변수에 할당
  => 변수 간에 서로 영향을 미침

```javascript
const obj1 = { name: "Alice", age: 30 };
const obj2 = obj1;
obj2.age = 40;

console.log(obj1.age); //40
console.log(boj2.age); //40
```

---

### 원시형 자료형

1. Number : 정수 또는 실수형 숫자를 표현하는 자료형

```javascript
const a = 13;
const b = -5;
const c = 3.14;
const d = 2.998e8; // 2.998 * 10^8 = 299,800,000
const e = Infinity; // 양의 무한대
const e = -Infinity; // 음의 무한대
const g = NaN; // Not a Number를 나타낸다. 숫자가 아니다.
// 숫자가 아닌데 왜 타입이 Number 냐 ? 연산이 안되는 결과가 NaN으로 나온다.
// 참고에서 봐줘
```

2. String : 텍스트 데이터를 나타내는 자료형

- '+' 연산자를 사용해서 문자열끼리 결합
- 뺄셈,곱셈,나눗셈 불가능

- Template literals(템플릿 리터럴) 💖💖💖💖💖
  - 내장된 표현식을 허용하는 문자열 작성 방식
  - **_Backtick(``)을 이용_**하며, 여러 줄에 걸쳐 문자열을 정의할 수도 있고
    JavaScript의 변수를 문자열 안에 바로 연결할 수 있음
  - 표현식은 '$'와 중괄호({experssion}) 로 표기
  - ES6+ 부터 지원

```javascript
const age = 100;
const message = `홍길동은 ${age} 세 입니다.`; // 백틱!!!!!! 주의!!!!
console.log(message); // 홍길동은 100세 입니다.
```

3. null과 undefined => 값이 없음을 나타내는 자료형!!

- null : 프로그래머가 _의도적으로_ '값이 없음'을 나타낼 때 사용

```javascript
let a = null;
console.log(a); //null
```

- undefined : 시스템이나 JavaScript 엔진이 '값이 할당되지 않음'을 나타낼 때 사용

```javascript
let b;
console.log(b); // undefined
```

4. Boolean

자바스크립트에서는 true / false 가 소문자!!!!!!!!

- 조건문 또는 반복문에서 Boolean이 아닌 데이터 타입을 "자동 형변환 규칙"에 따라
  true 또는 false 로 변환됨

- 자동형변환조건

| 데이터터입 | false          | true             |
| ---------- | -------------- | ---------------- |
| undefined  | 항상 false     | X                |
| null       | 항상 false     | X                |
| Number     | 0, -0, NaN     | 나머지 모든 경우 |
| String     | ' '(빈 문자열) | 나머지 모든 경우 |

---

---

### 연산자

- 단축 연산자 지원

- 증가 & 감소 연산자

1. 증가 연산자('++')

   - 피연산자를 증가(1을 더함) 시키고 연산자의 위치에 따라 증가하기 전이나 후의 값을 반환

2. 감소 연산자('--')
   - 피연산자를 감소(1을 뺌) 시키고 연산자의 위치에 따라 감소하기 전이나 후의 값을 반환

=> '+=' 또는 '-='와 같이 더 명시적인 표현으로 작성하는 것을 권장

```javascript
let x = 3;
const y = x++;
console.log(x, y); // 4 3
// y 에 3을 할당하고 나서 x 에 값을 증가

let a = 3;
const b = ++a;
console.log(a, b); // 4 4
// +1을 하고 나서 y에 할당!
```

```javascript
// "전위 연산자"
// 피연산자에 1을 더한 값을 반환
// a에 +1을 할당한 후의 값 4를 반환
let a = 3;
const b = ++a;
console.log(a, b); // 4 4

// "후위 연산자"
// 피연산자에 1을 더하기 전의 값을 반환
// x를 먼저 반환한 후 x에 +1을 할당
let x = 3;
const y = x++;
console.log(x, y); // 4 3
```

- 비교 연산자

- 동등 연산자 (==)
  => 필요한 케이스가 아니라면 권장하지 않음!!!

1. 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
2. '암묵적 타입 변환' 통해 타입을 일치시킨 후 같은 값인지 비교
3. 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별

```javascript
console.log(1 == 1); // true
console.log("hello" == "hello"); // true

// 암묵적 타입 변환
console.log("1" == 1); // true
console.log(0 == false); // true

// 1이 담겨있는 배열과 정수 1을 넣으면 ??? 이것도 true 로 나와 버림
console.log([1] == 1); // true
```

- 일치 연산자(===)

1. 두 피연산자의 값과 타입이 모두 같은 경우 true를 반환
2. 같은 객체를 가리키거나, 같은 타입이면서 같은 값인지를 비교
3. 엄격한 비교가 이뤄지며 암묵적 타입 변환이 발생하지 않음!!!
4. 특수한 경우를 제외하고는 동등 연산자가 아닌 **일치 연산자 사용 권장**

```javascript
console.log(1 === 1); // true
console.log("hello" === "hello"); // true

// 암묵적 타입 변환 없음!!!!!!
console.log("1" === 1); // false
console.log(0 === false); // false
```

- 논리 연산자

1. `and` 연산자

   - &&

2. `or` 연산자

   - ||

3. `not` 연산자

   - !

4. 단축 평가 지원!

```javascript
//and 연산자
true && false; // false
true && true; // true

false || ture; // true
false || false; // false

!true; // false

//단축평가 예시
1 && 0; // 0
0 && 1; // 0
4 && 7; // 7
1 || 0; // 1
0 || 1; // 1
4 || 7; // 4
```

---

---

---

## 조건문

```javascript
const name = "customer";

if (name === "admin") {
  console.log("관리자님 안녕");
} else if (name === "customer") {
  console.log("고객님 안녕");
} else {
  console.log("반갑습니다. ${name}");
}
```

- 삼항 연산자

```javascript
condition ? expression1 : expression2;
```

- condition
  - 평가할 조건(true 또는 false로 평가)
- expression1
  - 조건이 true일 경우 반환할 값 또는 표현식
- expression2
  - 조건이 false일 경우 반환할 값 또는 표현식

```javascript
const age = 20;

const message = age >= 18 ? "성인" : "미성년자";

console.lot(message); // 성인
```

## 반복문

1. while
2. for
3. for ...in
4. for ...of

---

1. `while` = 조건문이 참이면 문장을 계속해서 수행

```javascript
// while
let i = 0;

while (i < 6) {
  console.log(i);
  i += 1;
}
```

2. `for` = 특정한 조건이 거짓으로 판별될 때까지 반복

```javascript
for ([초기문]; [조건문]; [증감문]) {
  // do something
}

for (let i = 0; i < 6; i++) {
  console.log(i);
}
```

- for 동작 원리

```javascript
// 1. 반복문 진입 및 변수 i 선언
for (let i=0;

// 2. 조건문의 조건 평가 ( i값 확인) 하고 코드 블럭 실행
for (let i =0; i < 6;     ) {
    console.log(i)  // 0
}

//3. 코드 블록 실행 이후 i 값 증가
for (let i = 0: i < 6; i++){
    console.log(i)  //0
}
// 나와서 증감 확인하고 코드블록 실행
```

3. `for ...in `  
   = 객체({키:값} 딕셔너리로 나타내지는 자료형의 객체를 의미)의 열거 가능한 **_속성_**(property)에 대해 반복
   == 객체는 순서가 없다. 그래서 열거 가능하다고 표현한다.

```javascript
for (variable in object) {
  statement;
}
```

```javascript
const object = {
  a: "apple",
  b: "banana",
};

for (const property in object) {
  // const가 있는 이유는 property가 변수이기 때문에 변수 선언 키워드가 있어야함
  console.log(property); // a, b
  console.log(object[property]); // apple, banana
}
```

4. `for ...of`
   = 반복 가능한 객체(배열, 문자열 등)에 대해 반복
   여기서 객체는 위의 3번의 객체가 아니고 리얼 객체를 의미

```javascript
const numbers = [0, 1, 2, 3];

for (const number of numbers) {
  console.log(number);
}

const myStr = "apple";

for (const char of myStr) {
  console.log(char);
}
```

- `for in` 과 `for of` 의 비교(배열과 객체)

`for in` => 순서를 보장하지 않음 그냥 객체의 속성을 나열할 뿐!

```javascript
// Array 배열
const arr = ["a", "b", "c"];
for (const elem in arr) {
  console.log(elem); // 0 1 2  (인덱스임)
  // 왜  0 1 2 가 나왔을까용 for in 은 속성을 출력하니까!
}

// Object 객체
const capitals = {
  korea: "서울",
  japan: "도쿄",
  china: "베이징",
};
for (const capital in capitals) {
  console.log(capital); // korea japan china
}
```

`for of` => 반복가능한 객체에서 씀 = 즉, 순서가 존재한다는 뜻

```javascript
// Array 배열  -> 배열은 순서가 존재하기 때문에 출력이 됨
const arr = ["a", "b", "c"];
for (const elem of arr) {
  console.log(elem); // a b c
}

// Object 객체  -> 객체는 순서가 없으므로 반복가능하지 않음 그래서 출력안됨
const capitals = {
  korea: "서울",
  japan: "도쿄",
  china: "베이징",
};
for (const capital in capitals) {
  console.log(capital); // TypeError : capitals is not iterable
}
```

=> `for in` 은 객체전용, `for of` 는 배열 혹은 문자열처럼 반복가능전용이라고 생각하면 쉬움

- 배열 반복과 `for in`

1. 객체 관점에서 배열의 인덱스는 "정수 이름을 가진 열거 가능한 속성"
2. `for in` 은 정수가 아닌 이름과 속성을 포함하여 열거 가능한 모든 속성을 반환
3. 내부적으로 `for in`은 배열의 반복자가 아닌 속성 열거를 사용하기 때문에
   특정 순서에 따라 인덱스를 반환하는 것을 보장할 수 없음

-> `for in`은 인덱스의 순서가 중요한 배열에서는 사용하지 않음
-> 배열에서는 `for문`, `for of` 를 사용

4. 객체 관점에서 배열의 인덱스는 정수 이름을 가진 속성이기 때문에 인덱스가 출력됨(순서보장X)

```javascript
const arr = ["a", "b", "c"];

for (const i in arr) {
  console.log(i); // 0, 1, 2
}

for (const i of arr) {
  console.log(i); // a, b, c
}
```

---

---

- 반복문 사용 시 const 사용 여부

왜 `for문` 에서는 const를 안쓰고 let 을 썼는데 `for in` 과 `for of` 에서는 const를 써도 에러가 나지 않나요 ??

일단 for문에서 const를 쓰면 안되는 이유는 let i = 0 이 동작을 할 떄 (반복이 돌면서) 재할당이 됨 그래서 안돼

하지만 `for in` 과 `for of` 는 재할당 개념이 아니라, 매 반복마다 다른 속성의 이름이 변수에 지정되는 것 , 그래서 const 써도 돼

1. for문

   - for(let i = 0; i < arr.length; i++) { ... }의 경우에는
     최초 정의한 i 를 "재할당" 하면서 사용하기 때문에 const를 사용하면 에러 발생

2. `for in`, `for of`
   - 재할당이 아니라, 매 반복마다 다른 속성 이름이 변수에 지정되는 것이므로
     const를 사용해도 에러가 발생하지 않음
   - 단, const 특징에 따라 블록 내부에서 변수를 수정할 수 없음

---

---

참고

- NaN을 반환하는 경우 예시

1. 숫자로서 읽을 수 없음(Number(undefined))
2. 결과가 허수인 수학 계산식(Math.sqrt(-1))
3. 피연산자가 NaN(7 \*\* NaN)
4. 정의할 수 없는 계산식(0 \* Infinity)
5. 문자열을 포함하면서 덧셈이 아닌 계산식('가' / 3)
