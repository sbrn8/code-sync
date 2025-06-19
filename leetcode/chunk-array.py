/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    let result_arr = [];
    for (let i = 0; i < arr.length; i += size) {
        result_arr.push(arr.slice(i, i + size));
    }
    return result_arr;
};