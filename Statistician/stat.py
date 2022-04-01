import ms_toollib as ms
import os, click
import json

# i.e.
# python stat.py --video_dir ../videos

@click.command()
@click.option('--video_dir', default='videos', help='录像的目录')
def stat(video_dir):
    avfs = os.listdir(video_dir)
    json_list = []
    for avf in avfs:
        avf = video_dir + r"/" + avf
        a = ms.AvfVideo(avf)
        a.parse_video()
        a.analyse()
        json_list.append({"player": a.player, "rtime": a.r_time, "bbbv": a.bbbv})
    #filename = "v.json"
    with open(filename, 'w') as file_obj:
        json.dump(json_list, file_obj)
if __name__ == '__main__':
    stat()

