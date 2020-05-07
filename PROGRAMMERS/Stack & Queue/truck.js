function solution(bridge_length, weight, truck_weights) {
    let stack = [];
    let lastTime;
    let temp;
    truck_weights.forEach(element => {
        if (stack.length == 0) {
            stack.push([element, bridge_length + 1]);
            lastTime = bridge_length + 1;
        }
        else if (stack.reduce((a, b) => [a[0] + b[0], 0])[0] + element <= weight) {
            stack.push([element, ++lastTime]);
        } else {
            while (true) {
                temp = stack.shift();
                if (stack.reduce((a, b) => [a[0] + b[0], 0], [0, 0])[0] + element <= weight) {
                    stack.push([element, temp[1] + bridge_length]);
                    lastTime = temp[1] + bridge_length;
                    break;
                }
            }
        }
    });
    return stack.pop()[1];
}