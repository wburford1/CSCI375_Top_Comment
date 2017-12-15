# requires the video_id to be read in as first command line arg
from controller import ensemble_run, parse_video_dict
import sys
import json

if __name__ == '__main__':
    video_id = sys.argv[1]
    with open('comment_generated.json', 'r') as f:
        coms = json.load(f)
        # coms = [c.split(':')[1] for c in coms if ':' in c]
        coms = [c for c in coms if not c.isspace() and c != ""]
        for c in coms:
            c.strip()
        video_dict = parse_video_dict()
        best = ensemble_run(video_dict, coms, video_id)
        print('Best comment is: {}'.format(best))
