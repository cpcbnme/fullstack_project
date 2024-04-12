import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { AppRouterCacheProvider } from "@mui/material-nextjs/v13-appRouter";
import { ApplicationThemeProvider } from "@/providers/Theme";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Beers and cheers",
  description: "A simple page application powered by NextJS",
};

export default function RootLayout({
                                     children,
                                   }: Readonly<{
  children: React.ReactNode;
}>) {
  return (
      <html lang="en">
      <body>
      <link rel="favicon" href="/favicon.ico" sizes="any" />
      <link rel="preconnect" href="https://fonts.googleapis.com"></link>
      <link rel="preconnect" href="https://fonts.gstatic.com"></link>
      <link href="https://fonts.googleapis.com/css2?family=Inter:wght@100..900&family=Montserrat:ital,wght@0,100..900;1,100..900&family=Poppins:wght@400;600&display=swap" rel="stylesheet"></link>
      {
        <AppRouterCacheProvider options={{
          enableCssLayer: process.env.NODE_ENV === "production",
          key: "cometa"
        }}>
          <ApplicationThemeProvider>{children}</ApplicationThemeProvider>
        </AppRouterCacheProvider>
      }</body>
      </html>
  );
}
