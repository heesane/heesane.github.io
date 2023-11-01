/** @type {import('next').NextConfig} */
const nextConfig = {
    reactStrictMode: true,
    output: 'export',
    trailingSlash: '/',
    env: {},
    assetPrefix: process.env.NODE_ENV === 'production' ? '/nextjs-gh-pages/' : '',
}

module.exports = nextConfig
