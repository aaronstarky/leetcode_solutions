function reverse(x: number): number {
    // get num digits
    let numDigits = getNumDigits(x)
    let total = 0;
    for (let i = numDigits - 1; i >= 0; i--) {
        const digit = x % 10;
        total += digit * (Math.pow(10, i))
        x = x >= 0 ? Math.floor(x / 10) : Math.ceil(x / 10)
    }
    if (total > (Math.pow(2, 31) - 1) || total < (Math.pow(-2, 31))) {
        return 0;
    }
    return total;
};

function getNumDigits(x: number): number {
    let numDigits = 0
    let copy = x
    while (x >= 0 ? copy > 0 : copy < 0) {
        copy = x >= 0 ? Math.floor(copy / 10) : Math.ceil(copy / 10)
        numDigits += 1
    }
    return numDigits
}

console.log(reverse(-51));

console.log(reverse(123));