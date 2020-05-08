function solution(bridge_length, weight, truck_weights) {
    let time = 0;
    let totalWeight = 0;
    let onBridge = [];
    while (onBridge.length != bridge_length) onBridge.push(0);

    let nowTruck = truck_weights.shift();
    onBridge.push(nowTruck);
    onBridge.shift();
    totalWeight = onBridge.reduce((a, b) => a + b);
    time++;

    while (totalWeight) {
        totalWeight -= onBridge.shift();
        nowTruck = truck_weights.shift();
        if (nowTruck !== undefined) {
            if (totalWeight + nowTruck <= weight) {
                onBridge.push(nowTruck);
                totalWeight += nowTruck;
            } else {
                onBridge.push(0);
                truck_weights.unshift(nowTruck);
            }
        } else {
            onBridge.push(0);
        }
        time++;
    }
    return time;
}