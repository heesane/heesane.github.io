@echo off
echo start deploy
npm run build

xcopy /Y /s /i "C:\Users\win102102\Desktop\GithubPage\githubpage\out\*" "C:\Users\win102102\Desktop\GithubPage\" > DeployLogs.txt 2>&1

git add .
git commit -m "deploy"
git push