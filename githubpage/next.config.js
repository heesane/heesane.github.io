/** @type {import('next').NextConfig} */
const debug = process.env.NODE_ENV !== 'production'
const repository = "heesane.github.io"

const nextConfig = {
    reactStrictMode : true,
    assetPrefix: !debug ? `/${repository}/` : '',
    trailingSlash: true,
}

module.exports = nextConfig
