let exp_time_best = 28;
let exp_time_worst = 100;
let exp_bvs_best = 5.5;
let exp_bvs_worst = 1.4;
let exp_stnb_best = 180;
let exp_stnb_worst = 20;
let exp_rqp_best = 6;
let exp_rqp_worst = 60;

let int_time_best = 7;
let int_time_worst = 35;
let int_bvs_best = 6.1;
let int_bvs_worst = 1.7;
let int_stnb_best = 180;
let int_stnb_worst = 25;
let int_rqp_best = 2;
let int_rqp_worst = 20;

let beg_time_best = 0.1;
let beg_time_worst = 12;
let beg_bvs_best = 10;
let beg_bvs_worst = 2.2;
let beg_stnb_best = 300;
let beg_stnb_worst = 30;
let beg_rqp_best = 0.1;
let beg_rqp_worst = 4;
let rr = [246, 246, 246, 246, 246, 246, 246, 246, 246, 244, 242, 239, 237, 235, 233, 231, 229, 226, 224, 222, 220, 218, 216, 213, 211, 209, 207, 205, 203, 201, 198, 196, 193, 191, 188, 185, 182, 179, 176, 174, 171, 168, 165, 163, 160, 157, 154, 151, 149, 146, 143, 140, 141, 146, 150, 154, 158, 162, 166, 171, 175, 179, 183, 187, 191, 196, 200, 204, 208, 213, 217, 219, 221, 223, 224, 226, 228, 229, 231, 233, 234, 236, 238, 240, 241, 243, 245, 246, 248, 250, 251, 253, 255, 255, 255, 255, 255, 255, 255, 255];
let gg = [248, 248, 248, 248, 248, 248, 248, 248, 248, 247, 246, 245, 244, 243, 242, 241, 239, 238, 237, 236, 235, 234, 233, 232, 231, 230, 229, 228, 227, 226, 225, 224, 222, 221, 220, 219, 218, 217, 216, 214, 213, 212, 211, 210, 209, 207, 206, 205, 204, 203, 202, 201, 199, 197, 195, 193, 191, 189, 187, 184, 182, 180, 178, 176, 174, 172, 170, 168, 166, 164, 162, 162, 164, 166, 168, 170, 172, 174, 175, 177, 179, 181, 183, 185, 187, 189, 191, 192, 194, 196, 198, 200, 202, 202, 202, 202, 202, 202, 202, 202];
let bb = [252, 252, 252, 252, 252, 252, 252, 252, 252, 248, 245, 242, 239, 236, 233, 230, 226, 223, 220, 217, 214, 211, 207, 204, 201, 198, 195, 192, 189, 185, 182, 181, 185, 188, 192, 196, 199, 203, 207, 210, 214, 217, 221, 224, 228, 232, 235, 239, 242, 246, 250, 253, 254, 253, 252, 251, 250, 249, 247, 246, 245, 244, 243, 242, 240, 239, 238, 237, 236, 235, 233, 229, 224, 219, 213, 208, 203, 197, 192, 187, 181, 176, 171, 165, 160, 155, 149, 144, 139, 133, 128, 123, 117, 117, 117, 117, 117, 117, 117, 117];


export function get_color(pb, para) {
    let level = pb.level;
    let value, idx;
    if (para == 0) {
        value = pb.rtime
    } else if (para == 1) {
        value = pb.bvs
    } else if (para == 2) {
        value = pb.stnb
    } else if (para == 3) {
        value = pb.rqp
    }
    if (level == 'beg') {
        if (para == 'rtime' || para == 0) {
            idx = (beg_time_worst - value) / (beg_time_worst - beg_time_best);
        } else if (para == 'bvs' || para == 1) {
            idx = (value - beg_bvs_worst) / (beg_bvs_best - beg_bvs_worst);
        } else if (para == 'stnb' || para == 2) {
            idx = (value - beg_stnb_worst) / (beg_stnb_best - beg_stnb_worst);
        } else if (para == 'rqp' || para == 3) {
            idx = (beg_rqp_worst - value) / (beg_rqp_worst - beg_rqp_best);
        }
    } else if (level == 'int') {
        if (para == 'rtime' || para == 0) {
            idx = (int_time_worst - value) / (int_time_worst - int_time_best);
        } else if (para == 'bvs' || para == 1) {
            idx = (value - int_bvs_worst) / (int_bvs_best - int_bvs_worst);
        } else if (para == 'stnb' || para == 2) {
            idx = (value - int_stnb_worst) / (int_stnb_best - int_stnb_worst);
        } else if (para == 'rqp' || para == 3) {
            idx = (int_rqp_worst - value) / (int_rqp_worst - int_rqp_best);
        }
    } else if (level == 'exp') {
        if (para == 'rtime' || para == 0) {
            idx = (exp_time_worst - value) / (exp_time_worst - exp_time_best);
        } else if (para == 'bvs' || para == 1) {
            idx = (value - exp_bvs_worst) / (exp_bvs_best - exp_bvs_worst);
        } else if (para == 'stnb' || para == 2) {
            idx = (value - exp_stnb_worst) / (exp_stnb_best - exp_stnb_worst);
        } else if (para == 'rqp' || para == 3) {
            idx = (exp_rqp_worst - value) / (exp_rqp_worst - exp_rqp_best);
        }
    }
    idx = Math.round(idx * 100);
    idx = Math.max(idx, 0);
    idx = Math.min(idx, 99);
    return [rr[idx], gg[idx], bb[idx]]
}



