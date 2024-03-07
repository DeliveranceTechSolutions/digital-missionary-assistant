#/bin/bash
touch ./.git/hooks/pre-push
cp ./scripts/pre-push ./.git/hooks/pre-push
chmod +x ./.git/hooks/pre-push
