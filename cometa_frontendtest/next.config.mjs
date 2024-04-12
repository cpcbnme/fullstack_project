/** @type {import('next').NextConfig} */
const nextConfig = {
	env: {
		API_URL: process.env.BACKEND_URL,
	},
};

export default nextConfig;
