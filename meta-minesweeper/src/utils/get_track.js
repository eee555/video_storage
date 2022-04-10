// 根据video，解析x轴路径，返回echart的option
export function get_x_track(video) {
    const x_track = [];
    const time = [];
    let t = 0;
    const len = video.get_events_len;
    for (let i = 0; i < len; i++) {
        while (video.events_time(i) - 0.000001 > t) {
            time.push(t.toFixed(2));
            t += 0.01;
            x_track.push(video.events_y(i) / 16);
        }
        if (video.events_time(i) + 0.000001 < t) {
            continue
        }
    }
    let option = {
        title: {
            text: 'x轴轨迹'
        },
        xAxis: {
            type: "category",
            data: time,
        },
        yAxis: {
            type: "value",
        },
        series: [
            {
                data: x_track,
                type: "line",
                symbol: 'none',
            },
        ],
    };
    return option
}


export function get_y_track(video) {
    const y_track = [];
    const time = [];
    let t = 0;
    const len = video.get_events_len;
    for (let i = 0; i < len; i++) {
        while (video.events_time(i) - 0.000001 > t) {
            time.push(t.toFixed(2));
            t += 0.01;
            y_track.push(video.events_x(i) / 16);
        }
        if (video.events_time(i) + 0.000001 < t) {
            continue
        }
    }
    let option = {
        title: {
            text: 'y轴轨迹'
        },
        xAxis: {
            type: "category",
            data: time,
        },
        yAxis: {
            type: "value",
        },
        series: [
            {
                data: y_track,
                type: "line",
                symbol: 'none',
            },
        ],
    };
    return option
}





