const dictionary = {
    apple: "A fruit",
    banana: "Another fruit",
    cat: "A small domesticated carnivorous mammal"
};

const dictionary2 = new Map();

// Adding key-value pairs
dictionary2.set('apple', 'A fruit');
dictionary2.set('banana', 'Another fruit');
dictionary2.set('cat', 'A small domesticated carnivorous mammal');

const dictionary3 = {};

// Adding key-value pairs
dictionary3.apple = 'A fruit';
dictionary3.banana = 'Another fruit';
dictionary3.cat = 'A small domesticated carnivorous mammal';


//// get object keys
console.log(dictionary.apple)
console.log(dictionary2.get("apple"))
console.log(dictionary.apple)

const dictionary4 = {
    "apple": "A fruit",
    "banana": "Another fruit",
    "cat": "A small domesticated carnivorous mammal"
};



// ####################### process dictionary
console.log(typeof(Object.keys(dictionary4)))
for (const key of Object.keys(dictionary4)){
	console.log(typeof(key), key)
}

console.log(Object.keys(dictionary4))
console.log(typeof(Object.values(dictionary4)))
console.log(Object.values(dictionary4))

for (const [k, v] of Object.entries(dictionary4)){
	console.log("dictionary output: ", k, v);
}

for (const v of Object.values(dictionary4)){
	console.log(v)
}


const fruits = [
    { name: "Apple", color: "Red", taste: "Sweet" },
    { name: "Banana", color: "Yellow", taste: "Sweet" },
    { name: "Lemon", color: "Yellow", taste: "Sour" },
    { name: "Grapes", color: "Purple", taste: "Sweet" }
];


const apple = fruits.find(f=>f.name === "Apple")
console.log(apple.color)

for (const row of fruits) {
	for (const [k, v] of Object.entries(row)){
		console.log(k, v)
	}
}

