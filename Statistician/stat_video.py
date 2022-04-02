import ms_toollib as ms
import os, click, sys
import json
from io import StringIO

# i.e.
# python stat_video.py --video_dir ../videos > ../meta-minesweeper/static/v.json



@click.command()
@click.option('--video_dir', default='../videos', help='录像的目录')
def stat(video_dir):
    avfs = os.listdir(video_dir)
    video_info_list = []
    for avf in avfs:
        avf = video_dir + r"/" + avf
        a = ms.AvfVideo(avf)
        a.parse_video()
        a.analyse()
        video_info_list.append({"player": a.player, "row": a.row, 
                                "column": a.column, "mine_num": a.mine_num, 
                                "rtime": a.r_time, "bbbv": a.bbbv, "bbbv_s": a.bbbv_s})
        
    click.echo(json.dumps(video_info_list))
    
    
    
    
if __name__ == '__main__':
    stat()

