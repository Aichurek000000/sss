// print
// alert("hello world")

// переменные
var a = 7 // int // изменяемая переменная
let c = 3.14 // float // изменяемая переменная
const b = "hello" // string // неизменяемая переменная
const isPublished = true // boolean

// список
const names = ["Ularbek", "Janar", "Asan"]

// словарь, объект, ассоциативный массив
const profile = {
    name: "Elnura",
    "code": "python"
}

// print
console.log(profile.name)
console.log(profile.code)

// объект класса
const now = new Date()
console.log(now)

// if
if (a > 5) {
    console.log("А БОЛЬШЕ 5")
} else if (a > 3) {
    console.log("А больше 3")
} else {
    console.log("ЧТО-то тут")
}

// цикл for
for (let i=0; i<3; i++) {
    console.log(names[i])
}

// function
function hello(a, b) {
    return a + b
}