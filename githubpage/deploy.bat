@echo off
echo "deploy to gh-pages"
npm run build
npm run export
echo. > out\.nojekyll
git add -f out\
git commit -m "deploy to gh-pages"
git subtree push --prefix out origin gh-pages
echo "deploy to gh-pages done"
