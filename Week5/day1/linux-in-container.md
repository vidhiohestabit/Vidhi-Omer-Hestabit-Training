# Linux in Docker Container

## Directory structure
- /bin → essential binaries
- /usr → user programs
- /etc → config files
- /var → variable files (logs)
- /app → our Node.js app

## Commands explored
- Users: `whoami`
- Processes: `ps aux`, `top`
- Disk usage: `df -h`, `du -sh *`
- File listing: `ls -la`
- Logs: `cat /var/log/*.log`

## Commands to run

- image build: `docker build -t day1 .`
- run the file: `docker run -d day1`
- running container: `docker ps`
- image: `docker image ls`
- CPU usage: `docker top day1`
- disk usage: `docker exec -it <name_of_container> df -h`


## Notes
- Container behaves like a lightweight Linux OS
- Changes inside container may not persist unless using volumes