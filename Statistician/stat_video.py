import ms_toollib as ms
import os, click, sys
import json
from io import StringIO

# i.e.
# python stat_video.py --video_dir ../videos > ../meta-minesweeper/static/v.json

# python stat_video.py > ../meta-minesweeper/static/v.json

@click.command()
# @click.option('--video_dir', default='../Arbiter_0.52.3\replays', help='录像的目录')
def stat():
    dirs = [r'../Arbiter_0.52.3/replays', r'../Arbiter_0.52.3/replays2']
    video_info_list = []
    for dir_ in dirs:
        try:
            avfs = os.listdir(dir_)
        except:
            continue
        for avf_ in avfs:
            if avf_.split('.')[-1] != 'avf':
                continue
            avf = dir_ + r"/" + avf_
            try:
                a = ms.AvfVideo(avf)
                a.parse_video()
                a.analyse()
            except:
                click.echo(avf_)
                return
            video_info_list.append({"player": a.player, "row": a.row, 
                                    "column": a.column, "mine_num": a.mine_num, 
                                    "rtime": a.r_time, "bbbv": a.bbbv, "bbbv_s": a.bbbv_s,
                                    "file": avf_})
            
    click.echo(json.dumps(video_info_list))
    
    
    
    
if __name__ == '__main__':
    stat()

