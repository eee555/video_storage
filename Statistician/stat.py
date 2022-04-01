import ms_toollib as ms
import os, click
import json
from github3 import GitHub

# i.e.
# python stat.py --video_dir ../videos --username ${{ github.repository_owner }} --token ${{ secrets.GITHUB_TOKEN }}



@click.command()
@click.option('--video_dir', default='videos', help='录像的目录')
@click.option('--username', default='videos', help='令牌')
@click.option('--token', default='videos', help='令牌')
def stat(video_dir, username, token):
    avfs = os.listdir(video_dir)
    json_list = []
    for avf in avfs:
        avf = video_dir + r"/" + avf
        a = ms.AvfVideo(avf)
        a.parse_video()
        a.analyse()
        json_list.append({"player": a.player, "rtime": a.r_time, "bbbv": a.bbbv})
    filename = "v.json"


    gh = GitHub(token=token)
    rep = gh.repository(username, '')
    j = rep.file_contents('/v.json')
    j.update('auto commit', json.dumps(json_list))
    # with open(filename, 'w') as file_obj:
        # json.dump(json_list, file_obj)
if __name__ == '__main__':
    stat()

