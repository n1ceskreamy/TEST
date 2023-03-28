PATH_PREFIX=~
    
sys-packages:
	# sudo apt install -y docker-compose
	sudo apt install python3-pip -y
	sudo pip install pipenv

permissions:
	chmod u+x $(PATH_PREFIX)/mono/device/device.py
	chmod u+x $(PATH_PREFIX)/mono/command_center/center.py
	chmod u+x $(PATH_PREFIX)/mono/defence_system/system.py
	chmod u+x $(PATH_PREFIX)/mono/file_server/server.py
	chmod 777 $(PATH_PREFIX)/mono/storage

pipenv:
	pipenv install -r requirements.txt

prepare: sys-packages permissions pipenv build

prepare-screen:
	# WSL specific preparation
	sudo /etc/init.d/screen-cleanup start


run-screen: broker run-device-screen run-center-screen run-system-screen run-server-screen

build:
	docker-compose build

run:
	docker-compose up -d

restart:
	docker-compose restart

stop-app:
	pkill flask

restart-app: stop-app run


run-device:
	cd $(PATH_PREFIX)/mono/; pipenv run python device/device.py

run-device-screen:
	screen -dmS ccu bash -c "cd $(PATH_PREFIX)/mono/; pipenv run python device/device.py"

run-system:
	cd $(PATH_PREFIX)/mono/; pipenv run python defence_system/system.py

run-system-screen:
	screen -dmS ccu bash -c "cd $(PATH_PREFIX)/mono/; pipenv run python defence_system/system.py"


run-center:
	cd $(PATH_PREFIX)/mono/; pipenv run python command_center/center.py

run-center-screen:
	screen -dmS ccu bash -c "cd $(PATH_PREFIX)/mono/; pipenv run python command_center/center.py"

run-file-server:
	export FLASK_DEBUG=1; pipenv run python ./file_server/server.py

run-file-server-screen:
	screen -dmS file-server bash -c "export FLASK_DEBUG=1; pipenv run python ./server.py"

test:
	pytest -sv
