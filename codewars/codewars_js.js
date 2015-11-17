// Codewars JS challenges 

// Instructions:




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