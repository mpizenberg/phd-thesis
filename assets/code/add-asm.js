function add(x, y) {
    var x = x | 0;  // x is a 32-bit value
    var y = y | 0;  // so is y
    return (x+y) | 0; // 32-bit addition, no type or overflow checks
}
