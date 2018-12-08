const path = require('path');

const BundleTracker = require('webpack-bundle-tracker');
const webpack = require('webpack');

module.exports = {
  entry: [
    'jquery',
    './assets/src/index.js'
  ],
  output: {
    path: path.resolve(__dirname, 'assets/dist/bundles/'),
    filename: "[name]-[contenthash].js"
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
              publicPath: '../static/fonts'
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
