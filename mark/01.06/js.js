// 普通的继承
class A extends Object{};
console.log(A)  // [Function: A]

// 匿名继承
const B = class extends Object{
    constructor(){
        super();
        console.log('B constructor');
    }
};

console.log(B) // [Function: B]
b = new B()  // B constructor
console.log(b)  // B {}

// 箭头函数，参数是类，返回值也是类
const x = (Sup) =>{
    return class extends Sup {
        constructor(){
            super();
            console.log('C constructor');
        }
    };
}
// 演化成下面的形式
const C = Sup =>class extends Sup{
    constructor(){
        super();
        console.log('C constructor');
    }
}
// cls = new C(Object);  // 不可以new，因为是一个普通函数，
// 它的返回值是一个带constructor的类
cls = C(A)  // 调用它返回一个类，一个带constructor的class 
console.log(cls);  // C constructor
c = new cls();
console.log(c);  // A {}











