const path = require('path');

const BundleTracker = require('webpack-bundle-tracker');
const webpack = require('webpack');

console.log(process.env.ASSET_PATH)

module.exports = {
  entry: [
    'jquery',
    './assets/src/index.js'
  ],
  output: {
    filename: "[name]-[contenthash].js",
    path: path.resolve(__dirname, 'assets/dist/bundles/'),
    publicPath: process.env.ASSET_PATH,
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
    new webpack.EnvironmentPlugin({
      ASSET_PATH: '/',
      DEBUG: false,
      NODE_ENV: 'development',
    }),
    new webpack.ProvidePlugin({
      $: 'jquery',
      jQuery: 'jquery'
    })
  ],
};
