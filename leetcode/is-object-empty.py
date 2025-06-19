/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    result = (Object.keys(obj).length == 0) ?  true :  false;
    return result;
};