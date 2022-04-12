import ms_toollib as ms
import os, click, sys
import json, time
from io import StringIO

# 获取玩家当前比赛的成绩（根据最新标识）

# i.e.
# python get_tournament.py --json_dir ../meta-minesweeper/static/v.json > ../meta-minesweeper/static/tournament.json

@click.command()
@click.option('--json_dir', default='../meta-minesweeper/static/v.json', help='录像的目录')
def main(json_dir):
    with open(json_dir) as f:
        video_json = json.load(f)
    # pb = {'beg': {}, 'int': {}, 'exp': {}}
    latest_stamp = 0
    tournament_player = ''
    tournament_video = []
    for video in video_json:
        stamp = time.mktime(time.strptime(video['start_time'], '%d.%m.%Y.%H:%M:%S:%f'))
        if stamp > latest_stamp and video['player'] != tournament_player:
            latest_stamp = stamp
            tournament_player = video['player']
            tournament_video = []
        if video['player'] == tournament_player:
            tournament_video.append(video)
            
    click.echo(json.dumps(tournament_video))
    
    
def set_pb(old, new):
    if old:
        if old['rtime'] < new['rtime']:
            return old
    return {'rtime': new['rtime'], 'file': new['file']}
    
       
if __name__ == '__main__':
    main() 
    
    
    
    
    
    
    
    