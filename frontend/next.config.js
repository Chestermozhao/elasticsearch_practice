const withCSS = require('@zeit/next-css')
const withSass = require('@zeit/next-sass')
const withImages = require('next-images')
const withReactSvg = require('next-react-svg')
const path = require('path')

module.exports = withReactSvg(withImages(withCSS(withSass({
    devIndicators: {autoPrerender: false},
    include: path.resolve(__dirname, 'images'),
    webpack(config, options) {
         return config
    }
}))))
