import ms_toollib as ms
import os, click, sys
import json
#from github3 import GitHub
from io import StringIO

# i.e.
# python stat.py --video_dir ../videos > v.json



@click.command()
@click.option('--video_dir', default='videos', help='录像的目录')
def stat(video_dir):
    #click.echo('Hello World!')
    avfs = os.listdir(video_dir)
    json_list = []
    for avf in avfs:
        avf = video_dir + r"/" + avf
        a = ms.AvfVideo(avf)
        a.parse_video()
        a.analyse()
        json_list.append({"player": a.player, "rtime": a.r_time, "bbbv": a.bbbv})
    filename = "v.json"


    #gh = GitHub(token=token)
    #rep = gh.repository(username, '')
    #j = rep.file_contents('/v.json')
    #j.update('auto commit', json.dumps(json_list))
    #strIO = StringIO()
    #sys.stdout = strIO
    click.echo(json.dumps(json_list))
    #print(strIO.tell())
    # strIO.write(json.dumps(json_list))
    # with open(filename, 'w') as file_obj:
        # json.dump(json_list, file_obj)
if __name__ == '__main__':
    stat()

