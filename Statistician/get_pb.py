import ms_toollib as ms
import os, click, sys
import json
from io import StringIO

# 获取仓库中的所有玩家的排名，由于仅有一个玩家，拟弃用。

# i.e.
# python get_pb.py --json_dir ../meta-minesweeper/static/v.json > ../meta-minesweeper/static/pb.json

@click.command()
@click.option('--json_dir', default='../meta-minesweeper/static/v.json', help='录像的目录')
def main(json_dir):
    with open(json_dir) as f:
        video_json = json.load(f)
    pb = {'beg': {}, 'int': {}, 'exp': {}}
    for video in video_json:
        if video['row'] == 8 and video['column'] == 8 and video['mine_num'] == 10:
            bv = video['bbbv']
            if bv in pb['beg']:
                pb['beg'][bv] = set_pb(pb['beg'][bv], video)
            else:
                pb['beg'][bv] = {'rtime': video['rtime'], 'file': video['file']}
        elif video['row'] == 16 and video['column'] == 16 and video['mine_num'] == 40:
            bv = video['bbbv']
            if bv in pb['int']:
                pb['int'][bv] = set_pb(pb['int'][bv], video)
            else:
                pb['int'][bv] = {'rtime': video['rtime'], 'file': video['file']}
        elif video['row'] == 16 and video['column'] == 30 and video['mine_num'] == 99:
            bv = video['bbbv']
            if bv in pb['exp']:
                pb['exp'][bv] = set_pb(pb['exp'][bv], video)
            else:
                pb['exp'][bv] = {'rtime': video['rtime'], 'file': video['file']}
        else:
            ...
    click.echo(json.dumps(pb))
    
def set_pb(old, new):
    if old['rtime'] < new['rtime']:
        return old
    else:
        return {'rtime': new['rtime'], 'file': new['file']}
    
       
if __name__ == '__main__':
    main() 
    
    
    
    
    
    
    
    