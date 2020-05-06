function solution(bridge_length, weight, truck_weights) {
    let stack = [];
    let lastTime = 0;
    let temp;
    truck_weights.forEach(element => {
        if (stack.length == 0) {
            stack.push([element, bridge_length + 1]);
            lastTime = bridge_length + 1;
        }
        else if (stack.reduce((a, b) => [a[0] + b[0], 0])[0] <= weight) {
            stack.push([element, ++lastTime]);
            while (true) {
                if (stack.reduce((a, b) => [a[0] + b[0], 0])[0] <= weight) {
                    break;
                } else {
                    stack.pop();
                    temp = stack.shift();
                    stack.push([element, temp[1] + bridge_length]);
                    lastTime = temp[1] + bridge_length;
                }
            }
        } else {
            temp = stack.shift();
            while (true) {
                stack.push([element, temp[1] + bridge_length]);
                if (stack.reduce((a, b) => [a[0] + b[0], 0])[0] <= weight) {
                    lastTime = temp[1] + bridge_length;
                    break;
                } else {
                    stack.pop();
                    temp = stack.shift();
                }
            }
        }
    });
    return stack.pop()[1];
}