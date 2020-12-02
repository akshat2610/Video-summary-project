import sys
from moviepy.editor import *

VIDEO_SOURCE_PATH = 'C:\\Work\\SJSU\\Fall 2020\\CS 160\\Video summary project\\upload folder\\video\\2.mp4'
TIMESTAMP_FILE_PATH = 'C:\\Work\\SJSU\\Fall 2020\\CS 160\\Video summary project\\notes and timestamps data folder\\timestamp\\timestamp.txt'
VIDEO_DESTINATION_PATH = 'C:\\Work\\SJSU\\Fall 2020\\CS 160\\Video summary project\\notes and timestamps data folder\\video\\summary.mp4'

def gen_video_summary():
    try:
        source_video = VideoFileClip(VIDEO_SOURCE_PATH)
        print('opened video file')
        subclips = []
        count = 1

        timestamp_file = open(TIMESTAMP_FILE_PATH, 'r')
        print('opened timestamp file')
        timestamps_text = timestamp_file.read()
        timestamps_list = timestamps_text.split('+')

        print(len(timestamps_list))

        for timestamps in timestamps_list:
            print('processing #' + str(count))
            count += 1
            data = timestamps.split('-')
            start = convert_timestamp_to_seconds(data[0])
            end = convert_timestamp_to_seconds(data[1])
            subclip = source_video.subclip(start, end)

            subclips.append(subclip)

        video_summary = concatenate_videoclips(subclips)
        video_summary.write_videofile(VIDEO_DESTINATION_PATH)

    except:
        print(sys.exc_info())

def convert_timestamp_to_seconds(timestamp):
    data = timestamp.split(':')
    return int(data[0]) * 3600 + int(data[1]) * 60 + int(data[2])

if __name__ == '__main__':
    gen_video_summary()
