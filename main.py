import sys #arguments
import os #filesys
import subprocess#shell calls
import TextGeneration as TG

def getVideoURL(fullurl):
	return "https://www.youtube.com/watch?v=pk6zdlZVVlU"
	#return "2dBY7kRIu6E"
def downloadVideoFile(pathtofolder, videoID):
	if not os.path.exists(pathtofolder):
		os.mkdir(pathtofolder)

	flags = "--write-srt --srt-lang en "+videoID+" -f \"best[height=720]\" --output '"+pathtofolder+"/%(title)s.%(ext)s'"

	proc = subprocess.Popen(["youtube-dl "+flags, ], stderr=subprocess.PIPE, shell=True)
	(err) = proc.communicate()

	if("video doesn't have subtitles" in err ):
		#^
		print("Video Doesn't Have Subtitles")
	else:
		print("")
	return

def main():
	Args = sys.argv;

	videoID = getVideoURL(sys.argv[0])	
	downloadVideoFile("video/", videoID)
	TG.openVideoFile("video/Call of Duty - Advanced Warfare Multiplayer Gameplay.mp4")
	return;


if __name__ == '__main__':
	main()
