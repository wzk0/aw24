import os
import time

def get_good_name(name):
	name=name.replace('(','\(')
	name=name.replace(')','\)')
	name=name.replace(' ','\ ')
	return name

def chck():
	ls=os.listdir('.')
	for l in ls:
		if '.webm' in l:
			info=os.stat(l)
			s=info.st_size
			time.sleep(3)
			inf=os.stat(l)
			ss=inf.st_size
			if ss==s:
				t='ffmpeg -i '+get_good_name(l)+' '+get_good_name(l[:-4])+'mp4'
				r='rm -rf '+get_good_name(l)
				n='rm -rf nohup.out'
				os.system(t)
				os.system(r)
				os.system(n)
			else:
				pass
while True:
	chck()