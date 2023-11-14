document.addEventListener("DOMContentLoaded", myFunction)

function myFunction () {
    console.log('hi')
    const num1 = document.getElementById("num1")
    const num2 = document.getElementById("num2")
    const plus_button = document.getElementsByTagName("button")[0]
    const result = document.getElementById("res")
    plus_button.addEventListener("click", mySum)

    function mySum() {
        console.log('call mySum')
        value1 = Number(num1.value)
        value2 = Number(num2.value)
        sm = value1 + value2
        // console.log(sm)
        result.textContent = sm     
    }
}