import ms_toollib as ms
import os, click, sys
import json
from io import StringIO

# 获取仓库中的所有玩家的排名，由于仅有一个玩家，拟弃用。

# i.e.
# python get_medal.py --json_dir ../meta-minesweeper/static/v.json > ../meta-minesweeper/static/medal.json

@click.command()
@click.option('--json_dir', default='../meta-minesweeper/static/v.json', help='录像的目录')
def main(json_dir):
    with open(json_dir) as f:
        video_json = json.load(f)
    m = {'beg': {}, 'int': {}, 'exp': {}}
    for video in video_json:
        if video['row'] == 8 and video['column'] == 8 and video['mine_num'] == 10:
            bv = video['bbbv']
            if bv in m['beg']:
                m['beg'][bv] = min(m['beg'][bv], video['rtime'])
            else:
                m['beg'][bv] = video['rtime']
        elif video['row'] == 16 and video['column'] == 16 and video['mine_num'] == 40:
            bv = video['bbbv']
            if bv in m['beg']:
                m['int'][bv] = min(m['int'][bv], video['rtime'])
            else:
                m['int'][bv] = video['rtime']
        elif video['row'] == 16 and video['column'] == 30 and video['mine_num'] == 99:
            bv = video['bbbv']
            if bv in m['exp']:
                m['exp'][bv] = min(m['int'][bv], video['rtime'])
            else:
                m['exp'][bv] = video['rtime']
        else:
            ...
    click.echo(json.dumps(m))
    
    
       
if __name__ == '__main__':
    main() 
    
    
    
    
    
    
    
    