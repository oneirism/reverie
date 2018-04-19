[![Build Status](https://travis-ci.org/oneirism/reverie.svg?branch=master)](https://travis-ci.org/oneirism/reverie)
[![Coverage Status](https://coveralls.io/repos/github/oneirism/reverie/badge.svg)](https://coveralls.io/github/oneirism/reverie)
[![Known Vulnerabilities](https://snyk.io/test/github/oneirism/reverie/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/oneirism/reverie?targetFile=requirements.txt)


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
