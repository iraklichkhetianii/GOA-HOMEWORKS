let masivi = []

for(let i = 0; i < 100; i++){
    Array.push(i)
}

let evenSum = 0
for(let i = 0; i < evenSum.length; i++){
    if(i % 2 === 0){
        evenSum += i;
    }
}


const cars = ["Prius", "BMW", "Porsche", "Honda"];
cars.push("Honda");

// ამატებს კონკრეტულ მნიშვნელობას სიაში

const Cars = ["Lexus", "Mercedes", "Buggati", "Lamborghini"];
Cars.pop();

//აშორებს ბოლო ელემენტს

const cArs = ["Banana", "Dragon fruit", "Kiwi", "Apple"];
cArs.shift();

// შლის ბოლო ელემენტს

const caRs = ["Prius", "Porsche", "Lexus", "Bugatti"];
caRs.unshift("Honda", "Opel");

// ამატებს ელემენტებს სიაში

const carS = ["BMW", "Mustang", "Audi", "Mercedes"];
carS.splice(2,0,"Honda");


const CARS = ["Prius", "Porsche", "Lexus", "Bugatti"];
const theBestOne = CARS.slice(1);

// ახალი სია იქმნება, რომელიც შედგება კონკრეტული ელემენტებისგან ძველი სიიდან



function manualSlice(arr, num1, num2){
    let slicedArr = new Array()
    for(let i = num1; i < num2; i++){
        slicedArr.push(arr[i])
    }

    console.log(slicedArr)
}


function manualReverse(arr){
    let reversedArr = new Array()
    for(let i = reversedArr.lenght - 1; i >=0; i--){
        reversedArr.push(arr[i]);
    }
}


function manualIndexOf(arr,element){
    for(let i = 0; i < arr.length; i++){
        if(arr[i] === element){
            return i;
        }
    }
    return -1;
}


const arr = ["hello", "bye", "whatever"]
arr.indexOf('whatever')
arr.lastIndexOf()
arr.sort()
arr.reverse()