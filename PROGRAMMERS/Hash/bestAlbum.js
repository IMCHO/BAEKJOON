function solution(genres, plays) {
    var answer = [];
    let music = {};
    for (let key in genres) {
        key = Number(key);
        if (genres.hasOwnProperty(key)) {
            const element = genres[key];
            if (music[element] === undefined) {
                music[element] = { total: 0, lists: [] };
                music[element].lists.push([key, plays[key]]);
                music[element].total += plays[key];
            } else {
                music[element].lists.push([key, plays[key]]);
                music[element].total += plays[key];
            }
        }
    }

    let temp = Object.values(music).sort((a, b) => b.total - a.total);

    temp.forEach(element => {
        element.lists.sort((a, b) => {
            if (b[1] - a[1] == 0) {
                return a[0] - b[0];
            } else {
                return b[1] - a[1];
            }
        });

        let cnt = 0;
        for (let index = 0; index < element.lists.length && cnt < 2; index++) {
            const info = element.lists[index];
            answer.push(info[0]);
            cnt++;
        }
    });
    return answer;
}