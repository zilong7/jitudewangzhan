from fabric.api import env,run
from fabric.operations import sudo 

GIT_REPO = "https://github.com/zilong7/jitudewangzhan.git"

env.user = 'zilong7'
env.password = 'longpojun7'

env.hosts = ['www.goubilvshi.club']

env.port = '28417'

def deploy():
	source_folder = '/home/zilong7/sites/www.goubilvshi.com/jitudewangzhan'
	run('cd %s && git pull' % source_folder)
	run("""
		cd {} &&
		pip install -r requirements.txt &&
		python3 manage.py collectstatic --noinput &&
		python3 manage.py migrate
		""".format(source_folder))
	sudo('restart gunicorn-www.goubilvshi.com')
	sudo('service nginx reload')