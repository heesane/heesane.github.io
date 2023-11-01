/** @type {import('next').NextConfig} */
const debug = process.env.NODE_ENV !== "production";
const repository = "heesane.github.io"; // 리포지토리 이름
const nextConfig = {
    output: 'export',
    reactStrictMode: true,
    assetPrefix: !debug ? `/${repository}/` : "", // production 일때 prefix 경로
    trailingSlash: true, // 빌드 시 폴더 구조 그대로 생성하도록
}

module.exports = nextConfig
