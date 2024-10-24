# JavaScript 04 - 참조 자료형 02

## 객체

- Object : **_키로 구분_**된 데이터 집합을 저장하는 자료형

- 구조 및 속성

- 객체 구조
  - 중괄호 {} 를 이용해 작성
  - 중괄호 안에는 key: value 쌍으로 구성된 속성(property) 를 여러 개 작성 가능
  - key 는 문자형만 허용
  - value 는 모든 자료형 허용

```javascript
const user = {
  name: "Alice", // name 에 따옴표가 없다.-> 띄워쓰기가 없으면 따옴표 생략 가능!
  "key with space": true,
  greeting: function () {
    // greeting 함수 이름
    return "hello";
  },
};
```

- 속성 참조
  - 점('.', changing operator) 또는 대괄호('[]')로 객체 요소 접근
  - key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능

```javascript
// 조회
console.log(user.name); // Alice
console.log(user["key with space"]); // true

// 추가
user.address = "korea";
console.log(user); // {name: 'Alice', key with space: ture, address: 'korea', greeting: f}
```

```javascript
// 수정
user.name = "Bella";
console.log(name); // Bella

// 삭제
delete user.name;
console.log(user); // {key with space: true, address: 'korea', greeting: ƒ}
```

- 'in' 연산자
  - 속성이 객체에 존재하는지 여부를 확인

```javascript
// in 연산자
console.log("greeting" in user); // true
console.log("country" in user); // false
```

---

### 메서드

- 메서드는 클래스에 속해있는 함수였다.
  그래서 호출을 할 때 '객체.메서드' 로 활용했다.
  함수는 단독적으로 호출 가능

- Method : 객체 속성에 정의된 함수

- object.method() 방식으로 호출
- 메서드는 객체를 '행동' 할 수 있게 함

```javascript
console.log(user.greeting()); // hello
```

-> **_'this'_** 키워드를 사용해 객체에 대한 특정한 작업을 수행 할 수 있음

#### 'this' keyword

- 함수나 메서드를 호출한 객체를 가리키는 키워드
  -> 함수 내에서 객체의 속성 및 메서드에 접근하기 위해 사용

✔ Javascript에서 this 는 함수를 "호출하는 방법"에 따라 가리키는 대상이 다름 💖

|  호출방법   |                  대상                   |
| :---------: | :-------------------------------------: |
|  단순 호출  | 전역 객체 (window:브라우저 최상위 객체) |
| 메서드 호출 |          메서드를 호출한 객체           |
|             |

1. 단순 호출 시 this
   - 가리키는 대상 => 전역 객체

```javascript
// 1.1 단순 호출 시 this
const myFunc = function () {
  return this;
};
console.log(myFunc()); // window
```

2. 메서드 호출 시 this
   - 가리키는 대상 => 메서드를 호출한 객체

```javascript
const myObj = {
  data: 1,
  myFunc: function () {
    return this;
  },
};

console.log(myObj.myFunc()); // myObj
```

2-1. 중첩된 함수에서의 this 문제점과 해결책

```javascript
// forEach 함수
const myObj2 = {
  numbers: [1, 2, 3],
  myFunc: function () {
    this.numbers.forEach(function (number) {
      // 여기서 메소드로써 호출됐기 때문에 this는 myObj2 / forEach 는 메서드이고 반복문이다.
      // forEach 라는 메서드안에 인자가 또 함수이다.
      // fucntion(number){console.log(this)} 이 함수는 또 어떻게 호출되고 있을까 ? => 얘는 그냥 일반 함수식으로 호출되고 있다.
      // 일반 함수 호출일 때 this 는 window 이다.
      // 여기서 문제가 발생 . 여기서 window 라는 객체는 필요없고
      // 여기서 this는 myObj2 얘여야 한다. 그래야 저 반복문 안에서 배열의 요소나 다른 속성들을 조작할 수 있다.
      // 이것이 문제점이다.!
      // 이걸 해결하려면 메서드로서 활용되어야 하는데 여기서는 쓸 수 없다. 그래서 어떻게 해결할 수 있을까 ? => 화살표 함수를 사용하면 됨!
      console.log(this); // window
    });
  },
};

console.log(myObj2.myFunc());
```

```javascript
// 해결책 : 화살표함수 (화살표는 본인만의 this를 가지지 않는다. 따라서 본인을 감싸고 있는 상단, 즉 부모 함수의 this값을 가져옴)

const myObj3 = {
  numbers: [1, 2, 3],
  myFunc: function () {
    this.numbers.forEach((number) => {
      console.log(this); // myObj3
    });
  },
};

console.log(myObj3.myFunc());
```

- JavaScript `this` 정리

1. JavaScript의 함수는 호출될 때 `this` 를 암묵적으로 전달 받음
2. JavaScript에서 `this` 는 함수가 `호출되는 방식` 에 따라 결정되는 현재 객체를 나타냄
3. Python의 `self` 와 Java의 `this` 가 선언시 이미 값이 정해지는 것에 비해 JavaScriptdml `this` 는 **_함수가 호출되지 전까지 값이 할당되지 않고 호출 시에 결정_** 됨 (동적 할당)

주의!!

```JavaScript
// 만약 시험에서 함수 호출 없이 (console.log(myFunc()))
const myFunc = function () {
    return this
}

// 만 줬을 때 this 값은 ?
// 정답 : 모른다. 왜냐면 myFunc 이 어떻게 호출되는 지에 따라 달라지기 때문, 호출하지 않으면 몰라!
```

4. `this` 가 미리 정해지지 않고 호출 방식에 의해 결정되는 것은
   - 장점
     - 함수(메서드)를 하나만 만들어 여러 객체에서 재사용할 수 있다는 것
   - 단점
     - 이런 유연함이 실수로 이어질 수 있다는 것

=> 개발자는 `this` 의 동작 방식을 충분히 이해하고 장점을 취하면서 실수를 피하는 데에 집중해야 한다.

---

---

### 추가 객체 문법

1. 단축 속성

- 키 이름과 값으로 쓰이는 변수의 이름이 같은 경우 단축 구문 사용할 수 있음

```JavaScript
// 1. 단축 속성
const name = 'Alice'
const age = 30

const user1 = {
    name: name,
    age: age
}

const user2 = {
    name,
    age
}
```

2. 단축 메서드

- 메서드 선언 시 function 키워드 생략 가능

```JavaScript
// 2. 단축 메서드
const myObj1 = {
    myFunc: function () {
    return 'Hello'
    }
}

const myObj2 = {
    myFunc () {
    return 'Hello'
    }
}
```

3. 계산된 속성

- 키가 대괄호 [] 로 둘러싸여 있는 속성
- 고정된 값이 아닌 변수 값을 사용할 수 있음

```JavaScript
// 3. 계산된 속성
const product = prompt('물건 이름을 입력해주세요')
const prefix = 'my'
const suffix = 'property'

const bag = {
    [product]:5,
    [prefix + suffix]: 'value'
}

console.log(bag) // {연필: 5, myproperty: 'value'}
```

4. 구조 분해 할당 💖💖💖

```JavaScript
 // 4. 구조 분해 할당
const userInfo = {
    firstName: "Alice",
    userId: "alice123",
    email: "alice123@gmail.com",
};

const firstName = userInfo.name;
const userId = userInfo.userId;
const email = userInfo.email;

const { firstName } = userInfo; // userInfo 에 firstName 이 같아야 쓸 수 있다.
const { firstName, userId } = userInfo;
const { firstName, userId, email } = userInfo;

// Alice alice123 alice123@gmail.com
console.log(firstName, userId, email);
```

```JavaScript
// 구조 분해 할당 활용 - "함수 매개변수"
function printInfo({ name, age, city }) {
    console.log(`이름: ${name}, 나이: ${age}, 도시: ${city}`);
}

const person = {
    name: "Bob",
    age: 35,
    city: "London",
};

// 함수 호출 시 객체를 구조 분해하여 함수의 매개변수로 전달
printInfo(person);
```

5. Object with '전개 구문' ...

- "객체 복사"
  - 객체 내부에서 객체 전개
- 얕은 복사에 활용 가능

```JavaScript
// 5. 전개 구문 - "객체 복사"
const obj = { b: 2, c: 3, d: 4 };
const newObj = {a: 1, ...obj, e:5};
console.log(newObj); // {a: 1, b: 2, c: 3, d: 4, e: 5} 그 객체를 풀어서 넣음
```

6. 유용한 객체 메서드

- Object.keys()
- Object.values()

```javascript
// 6. 유용한 객체 메서드 (Object.keys(), Object.values())
const profile = {
  name: "Alice",
  age: 30,
};

console.log(Object.keys(profile)); // ['name', 'age']
console.log(Object.values(profile)); // ['Alice', 30]
```

7.Optional chaining ('?.')

- 속성이 없는 중첩 객체를 에러 없이 접근할 수 있는 방법
- 만약 참조 대상이 null 또는 undefined라면 에러가 발생하는 것 대신 평가를 멈추고 undefined를 반환

```javascript
const user = {
  name: "Alice",
  greeting: function () {
    return "hello";
  },
};

console.log(user.address.street); // Uncaught TypeError: Cannot read properties of undefined (reading 'street')
console.log(user.address?.street); // undefined

console.log(user.nonMethod()); // Uncaught TypeError: user.nonMethod is not a function
console.log(user.nonMethod?.()); // undefined
```

- 만약 Optional chaining 을 사용하지 않는다면 다음과 같이 '&&' 연산자를 사용해야 함

```javascript
const user = {
  name: "Alice",
  greeting: function () {
    return "hello";
  },
};

console.log(user.address && user.address.street); // undefined
```

- Optional chaining ('?.') 장점

1. 참조가 누락될 가능성이 있는 경우 연결된 속성으로 접근할 때 더 짧고 간단한 표현식을 작성할 수 있음
2. 어떤 속성이 필요한지에 대한 보증이 확실하지 않는 경우에 객체의 내용을 보다 편리하게 탐색할 수 있음

- Optional chaining ('?.') 주의사항

1. Optional chaining은 존재하지 않아도 괜찮은 대상에만 사용해야 함(남용X)
   - 왼쪽 평가대상이 없어도 괜찮은 경우에만 선택적으로 사용
   - 중첩 객체를 에러 없이 접근하는 것이 사용 목적이기 때문

```javascript
// 아래 예시 코드 논리상 user는 반드시 있어야 하지만 address는 필수 값이 아님
// user에 값을 할당하지 않은 문제가 있을 때 바로 알아낼 수 있어야 하기 때문
console.log(user.address && user.address.street); // undefined
console.log();

// Bad
user?.address?.street;

// Good
user.address?.street;
```

2. Optional chaining 앞의 변수는 반드시 선언되어 있어야 함

```javascript
console.log(myObj?.address); // Uncaught TypeError: myObj is not defined
```

- Optional chaining 정리

1. obj?.prop

   - obj가 존재하면 obj.prop을 반환하고, 그렇지 않으면 undefined를 반환

2. obj?.[prop]

   - obj가 존재하면 obj.[prop]을 반환하고, 그렇지 않으면 undefined를 반환

3. obj?.method()
   - obj가 존재하면 obj.method()를 호출하고, 그렇지 않으면 undefined를 반환

---

---

#### JSON

```JavaScript
const jsObject = {
    coffee: 'Americano',
    iceCream: 'Cookie and cream'
}

// Object -> JSON
const objToJson = JSON.stringify(jsObject)
console.log(objToJson)  // {"coffee":"Americano","iceCream":"Cookie and cream"}
console.log(typeof objToJson)  // string

// JSON -> Object
const jsonToObj = JSON.parse(objToJson)
console.log(jsonToObj)  // { coffee: 'Americano', iceCream: 'Cookie and cream' }
console.log(typeof jsonToObj)  // object
```

---

---

- 참고

### 클래스

- 객체를 생성하기 위한 템플릿(객체의 속성, 메서드를 정의하는 청사진 역할)

1. 클래스의 기본 문법

- class 키워드
- 클래스 이름
- 생성자 메서드
  - constructor()

```javascript
class Myclass {
    // 여러 메서드를 정의할 수 있음
    constructor() {...}
    method1() {...}
    method2() {...}
    method3() {...}
    ...

}
```

2. 클래스 특징

- ES6 에서 도입
- 생성자 함수를 사용하여 객체를 생성하는 이전의 방식을 객체 지향적으로 표현하고자 만들어지
- 그래서 클래스는 내부적으로 생성자 함수를 기반으로 동작함

```javascript
// 생성자 함수(과거)
function Member(name, age) {
  this.name = name;
  this.age = age;
  this.sayHi = function () {
    console.log(`Hi, I am ${this.name}`);
  };
}

// 클래스
class Member {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
  sayHi() {
    console.log(`Hi, I am ${this.name}`);
  }
}
```

3. 클래스 활용

```javascript
class Member {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }
  sayHi() {
    console.log(`Hi, I am ${this.name}`);
  }
}

const member3 = new Member("Alice", 20);

console.log(member3); // Member {name: 'Alice', age : 20}
console.log(member3.name); // Alice
member3.sayHi(); // Hi I am Alice
```

4. `new` 연산자

- 클래스나 생성자 함수를 사용하여 새로운 객체를 생성

4-1. `new` 연산자 특징

```javascript
const instance = new ClassName(arg1, arg2);
```

- 클래스의 constructor() 는 new 연산자에 의해 자동으로 호출되며 특별한 절차 없이 객체를 초기화 할 수 있음
- new 없이 클래스를 호출하면 TypeError 발생
