# Clean up test bundles
rm -rf assets/dist

# Decrypt production settings
#openssl aes-256-cbc -K $encrypted_8c964e5c4b48_key -iv $encrypted_8c964e5c4b48_iv -in secure/prod.py.enc -out reverie/settings/prod.py -d

# Build production bundle
ASSET_PATH="https://cdn.reverie.oneirism.co/prod/static/bundles/" yarn bundle
pipenv run python manage.py collectstatic --settings reverie.settings.prod --no-input

# Update Zappa stack
pipenv run zappa update prod
