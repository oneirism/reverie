const path = require('path');

const BundleTracker = require('webpack-bundle-tracker');
const webpack = require('webpack');

module.exports = {
  entry: [
    'jquery',
    './assets/src/index.js'
  ],
  output: {
    filename: "[name]-[contenthash].js",
    path: path.resolve(__dirname, 'assets/dist/bundles/'),
    publicPath: process.env.ASSET_PATH || 'static/bundles/',
  },
  module: {
    rules: [
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
      },
      {
        test: /\.scss$/,
        use: [
          'style-loader',
          'css-loader',
          'sass-loader',
        ]
      },
      {
        test: /.(gif)(\?[a-z0-9]+)?$/,
        use: [
          {
            loader: 'url-loader',
            options: {
              limit: 10000,
            }
          }
        ]
      }
    ]
  },
  plugins: [
    new BundleTracker({filename: 'webpack-stats.json'}),
    new webpack.ProvidePlugin({
      $: 'jquery',
      jQuery: 'jquery'
    })
  ],
};
