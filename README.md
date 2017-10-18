[![Build Status](https://travis-ci.org/devenney/reverie.svg?branch=master)](https://travis-ci.org/devenney/reverie)
[![Coverage Status](https://coveralls.io/repos/github/devenney/reverie/badge.svg)](https://coveralls.io/github/devenney/reverie)
[![Requirements Status](https://requires.io/github/devenney/reverie/requirements.svg?branch=master)](https://requires.io/github/devenney/reverie/requirements/?branch=master)

# reverie

## Contributing

### Dependencies

* Python 3.6
* Yarn (NodeJS LTS)

### Project Structure

`assets/`

* Contains SCSS resources which are bundled by webpack.
* If you need to force a rebuild, execute `yarn run build`.
* Hot rebundling is enabled by default.

`campaign/`

* The campaign tracking application.

`reverie/`

* The Django project.

### Building and Running

    # Install Python Dependencies
    pip install -r requirements.txt

    # Install Node Dependencies
    yarn install

    # Webpack Build
    yarn run build

    # Database Migrations
    python manage.py makemigrations campaign
    python manage.py migrate

    # Start Development Server
    yarn start

    # Create Administrative User
    python manage.py createsuperuser
