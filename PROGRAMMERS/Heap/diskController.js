function solution(jobs) {
    let now = 0;
    let time = 0;
    let len = jobs.length;
    jobs.sort((a, b) => a[1] - b[1]);

    while (jobs.length) {
        for (let index = 0; index < jobs.length; index++) {
            const element = jobs[index];
            if (element[0] <= now) {
                now += element[1];
                time += (now - element[0]);
                jobs.splice(jobs.indexOf(element), 1);
                break;
            }
            if (index == jobs.length - 1) now++;
        }
    }

    return Math.floor(time / len);
}