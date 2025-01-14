const task1 = new Promise((resolve) => setTimeout(() => resolve("Task 1 complete"), 2000));
task1.then(console.log);

//

const task2 = new Promise((_, reject) => reject("Task 2 failed"));
task2.catch(console.error);

//

const task3 = new Promise((resolve) => resolve(5));
task3.then((num) => num * 2).then(console.log);

//

function task4() {
  return new Promise((resolve) => setTimeout(() => resolve("First"), 2000))
    .then((msg) => {
      console.log(msg);
      return new Promise((resolve) => setTimeout(() => resolve("Second"), 1000));
    })
    .then(console.log);
}

//

function task5() {
    return new Promise((_, reject) => setTimeout(() => reject("Task 3 failed"), 2000)).catch(console.error);
  }
  
  task5();
  