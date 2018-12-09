const path = require('path');

const BundleTracker = require('webpack-bundle-tracker');
const webpack = require('webpack');

/* Variables */
const PUBLIC_PATH = process.env.PUBLIC_PATH || '/static'
const ENV = process.env.NODE_ENV || 'dev'

const PUBLIC_PATHS = {
  'dev': '/static/bundles/',
  'production': 'https://cdn.reverie.devenney.io/static/',
}

module.exports = {
  entry: [
    'jquery',
    './assets/src/index.js'
  ],
  output: {
    filename: "[name]-[contenthash].js",
    path: path.resolve(__dirname, 'assets/dist/bundles/'),
    publicPath: PUBLIC_PATHS[ENV],
  },
  module: {
    rules: [
      {
        test: /\.scss$/,
        use: [
          'style-loader',
          'css-loader',
          'sass-loader',
        ]
      },
      {
        test: /.(ttf|otf|eot|svg|woff(2)?)(\?[a-z0-9]+)?$/,
        use: [
          {
            loader: 'file-loader',
            options: {
              name: '[name].[ext]',
              outputPath: '../fonts/',
            }
          }
        ]
      }
    ]
  },
  plugins: [
    new BundleTracker({filename: './assets/dist/webpack-stats.json'}),
    new webpack.ProvidePlugin({
      $: 'jquery',
      jQuery: 'jquery'
    })
  ],
};
