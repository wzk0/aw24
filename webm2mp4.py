import os
import time

def get_good_name(name):
	name=name.replace('(','\(')
	name=name.replace(')','\)')
	name=name.replace(' ','\ ')
	return name

def get_core():
	os.system("cat /proc/cpuinfo |grep 'processor'|wc -l > .core")
	with open('.core','r')as f:
		core=f.read()
	os.system('rm -rf .core')
	return str(core[0])

def chck(road,time_s):
	ls=os.listdir(road)
	if '.webm' in str(ls):
		for l in ls:
			if '.webm' in l:
				info=os.stat(l)
				s=info.st_size
				time.sleep(5)
				inf=os.stat(l)
				ss=inf.st_size
				if ss==s:
					t='ffmpeg -threads '+get_core()+' -i '+get_good_name(l)+' '+get_good_name(l[:-4])+'mp4'
					r='rm -rf '+get_good_name(l)
					n='nohup.out'
					os.system(t)
					os.system(r)
					if os.path.exists(n):
						os.system('rm -rf '+n)
					else:
						pass
				else:
					time.sleep(5)
			else:
				pass
	else:
		time.sleep(time_s)

while True:
	chck('.',300)