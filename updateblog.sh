# sync the directories
rsync -av --delete "/home/comet/Documents/webb/posts" "/home/comet/Documents/cometblog/content/posts"

# move photos to the contents
python3 images.py

# build website
hugo

# git commands
git add .
git commit -m "message"
git push -u origin master

# Push the public folder to the vercel branch using subtree split and force push
echo "Deploying to GitHub vercel..."
git subtree split --prefix public -b vercel-deploy
git push origin vercel-deploy:vercel --force
git branch -D vercel-deploy