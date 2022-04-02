import ms_toollib as ms
import os, click, sys
import json
from io import StringIO

# i.e.
# python get_leaderboard.py --json_dir ../meta-minesweeper/static/v.json > ../meta-minesweeper/static/l.json

@click.command()
@click.option('--json_dir', default='../meta-minesweeper/static/v.json', help='录像的目录')
def stat(json_dir):
    with open(json_dir) as f:
        video_json = json.load(f)
        
    leaderboard = {}
    for video in video_json:
        if video['player'] in leaderboard:
            if video['row'] == 8 and video['column'] == 8 and video['mine_num'] == 10:
                if video['rtime'] < leaderboard[video['player']]['beg_time']:
                    leaderboard[video['player']]['beg_time'] = video['rtime']
                if video['bbbv_s'] > leaderboard[video['player']]['beg_bbbv_s']:
                    leaderboard[video['player']]['beg_bbbv_s'] = video['bbbv_s']
            elif video['row'] == 16 and video['column'] == 16 and video['mine_num'] == 40:
                if video['rtime'] < leaderboard[video['player']]['int_time']:
                    leaderboard[video['player']]['int_time'] = video['rtime']
                if video['bbbv_s'] > leaderboard[video['player']]['int_bbbv_s']:
                    leaderboard[video['player']]['int_bbbv_s'] = video['bbbv_s']
            elif video['row'] == 16 and video['column'] == 30 and video['mine_num'] == 99:
                if video['rtime'] < leaderboard[video['player']]['exp_time']:
                    leaderboard[video['player']]['exp_time'] = video['rtime']
                if video['bbbv_s'] > leaderboard[video['player']]['exp_bbbv_s']:
                    leaderboard[video['player']]['exp_bbbv_s'] = video['bbbv_s']
            else:
                ...
        else:
            if video['row'] == 8 and video['column'] == 8 and video['mine_num'] == 10:
                leaderboard[video['player']] = {}
                leaderboard[video['player']]['beg_time'] = video['rtime']
                leaderboard[video['player']]['beg_bbbv_s'] = video['bbbv_s']
                leaderboard[video['player']]['int_time'] = 60
                leaderboard[video['player']]['int_bbbv_s'] = 1
                leaderboard[video['player']]['exp_time'] = 240
                leaderboard[video['player']]['exp_bbbv_s'] = 0.5
            elif video['row'] == 16 and video['column'] == 16 and video['mine_num'] == 40:
                leaderboard[video['player']] = {}
                leaderboard[video['player']]['beg_time'] = 10
                leaderboard[video['player']]['beg_bbbv_s'] = 2
                leaderboard[video['player']]['int_time'] = video['rtime']
                leaderboard[video['player']]['int_bbbv_s'] = video['bbbv_s']
                leaderboard[video['player']]['exp_time'] = 240
                leaderboard[video['player']]['exp_bbbv_s'] = 0.5
            elif video['row'] == 16 and video['column'] == 30 and video['mine_num'] == 99:
                leaderboard[video['player']] = {}
                leaderboard[video['player']]['beg_time'] = 10
                leaderboard[video['player']]['beg_bbbv_s'] = 2
                leaderboard[video['player']]['int_time'] = 60
                leaderboard[video['player']]['int_bbbv_s'] = 1
                leaderboard[video['player']]['exp_time'] = video['rtime']
                leaderboard[video['player']]['exp_bbbv_s'] = video['bbbv_s']
            else:
                ...
    
    click.echo(json.dumps(leaderboard))
    
    
    
    
if __name__ == '__main__':
    stat()

