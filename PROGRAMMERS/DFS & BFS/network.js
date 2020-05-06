function solution(n, computers) {
    let route = [];
    let queue = [];
    let network = 0;
    for (let row = 0; row < n; row++) {
        if (!route.includes(row)) {
            route.push(row);
        } else {
            continue;
        }
        for (let index in computers[row]) {
            index = Number(index);
            if (index == row) continue;
            if (computers[row][index] == 1) {
                queue.push(index);
            }
        }
        while (queue.length != 0) {
            let nextIndex = queue.shift();
            route.push(nextIndex);
            for (let index in computers[nextIndex]) {
                index = Number(index);
                if (index == nextIndex) continue;
                if (computers[nextIndex][index] == 1) {
                    if (!route.includes(index)) {
                        queue.push(index);
                    }
                }
            }
        }
        network++;
    }
    return network;
}