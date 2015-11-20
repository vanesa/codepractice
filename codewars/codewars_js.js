// Codewars JS challenges 

// roundToNext5 Instructions:
// Given an integer as input, can you round it to the next 5?

// Examples:

// input:    output:
// 0    ->   0
// 2    ->   5
// 3    ->   5
// 12   ->   15
// 21   ->   25
// 30   ->   30
// etc.
// Input may be any positive or negative integer (including 0).

// You can assume that all inputs are valid integers.


function roundToNext5(n){
  var num = n;
  
  if (num % 5 != 0 || num != 0) {
     while (num % 5 != 0) {
       num += 1
     }
     return num
  }
  return num
}

