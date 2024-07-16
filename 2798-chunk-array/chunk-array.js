/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    let l1 = [];
let l2 = [];
let l = arr.length;
//console.log(l);

if (l === 0) {
  
  return l2;
}
if (size <= l) {
  let j = 1;
  let i = 0;
  while (i <= arr.length - 1) {
    j = 1;
    while (j <= size && i <= arr.length - 1) {
      //console.log(arr[i]);
      l1.push(arr[i]);
      i++;
      j++;
    }
    l2.push(l1);
    l1 = [];
  }
}
if (size > l) {
  for (let i of arr) {
    l1.push(i);
  }
  l2.push(l1);
}

return l2;


};
