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

    yarn install
    yarn run build
    yarn start
