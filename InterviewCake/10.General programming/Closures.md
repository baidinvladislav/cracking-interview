<h2>Closures</h2>

Замыкание — это функция, которая обращается к переменной «вне себя». Например:

```javascript
const message = 'The British are coming.';
function sayMessage(){
    alert(message); // Here we have access to message,
    // even though it's declared outside this function!
}
```

Мы бы сказали, что message "замкнуто" функцией sayMessage().

Одна полезная вещь, которую можно сделать с замыканием, — это создать что-то вроде «переменной экземпляра», 
которая может меняться со временем и влиять на поведение функции.

```javascript
// Function for getting the id of a dom element,
// giving it a new, unique id if it doesn't have an id yet
const getUniqueId = (() => {
    let nextGeneratedId = 0;
    return element => {
        if (!element.id) {
          element.id = `generated-uid-${nextGeneratedId}`;
          nextGeneratedId++;
        }
        return element.id;
    };
})();
```

Почему мы поместили nextGeneratedId в немедленно выполняемую анонимную функцию? Он делает nextGeneratedId приватным, 
что предотвращает случайные изменения из внешнего мира:

```javascript
// Function for getting the id of a dom element,
// giving it a new, unique id if it doesn't have an id yet
let nextGeneratedId = 0;
const getUniqueId = element => {
    if (!element.id) {
    element.id = `generated-uid-${nextGeneratedId}`;
    nextGeneratedId++;
    }
    return element.id;
};

// ...
// Somewhere else in the codebase...
// ...

// WHOOPS--FORGOT I WAS ALREADY USING THIS FOR SOMETHING
nextGeneratedId = 0;

```
