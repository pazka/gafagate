scp -r --exclude node_modules --exclude .git --exclude .vscode --exclude .env . pazka@gafagate:/home/pazka/gafagate-main 
ssh -t pazka@gafagate 'sudo reboot'