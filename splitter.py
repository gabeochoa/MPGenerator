import sys #arguments
import os #filesys
import youtube_dl

def getVideoURL(fullurl):
	return "https://www.youtube.com/watch?v=pk6zdlZVVlU"
	#return "2dBY7kRIu6E"

def downloadVideoFile(pathtofolder, videoID):
	if not os.path.exists(pathtofolder):
		os.mkdir(pathtofolder)
	ydl_opts = {
		'format': 'best',
	}

def main():
	Args = sys.argv;

	videoID = getVideoURL(sys.argv[0])	
	downloadVideoFile("video/", videoID)
	return;


if __name__ == '__main__':
	main()