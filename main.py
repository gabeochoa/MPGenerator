import sys #arguments
import os #filesys
import youtube_dl

class MyLogger(object):
	def debug(self, msg):
		pass

	def warning(self, msg):
		pass

	def error(self, msg):
		print(msg)


def my_hook(d):
	if d['total_bytes']:
		print '{0:2.2f}%\r'.format(float(d['downloaded_bytes'])/float(d['total_bytes'])*100),
		sys.stdout.flush()
	if d['status'] == 'finished':
		print('Done downloading, now converting ...')

def getVideoURL(fullurl):
	return "https://www.youtube.com/watch?v=pk6zdlZVVlU"
	#return "2dBY7kRIu6E"

def downloadVideoFile(pathtofolder, videoID):
	if not os.path.exists(pathtofolder):
		os.mkdir(pathtofolder)
	ydl_opts = {
		'format': 'best',
		'outtmpl': pathtofolder + '%(title)s.%(ext)s',
		'logger': MyLogger(),
		'progress_hooks': [my_hook],
		'FileDownloader': ['continuedl'],
	}
	print (pathtofolder)
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([getVideoURL('asfdasdfa')])

def main():
	Args = sys.argv;

	videoID = getVideoURL(sys.argv[0])	
	downloadVideoFile("video/", videoID)
	return;


if __name__ == '__main__':
	main()