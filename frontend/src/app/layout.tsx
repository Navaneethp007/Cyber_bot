import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import NavBar from '@/components/NavBar';

const inter = Inter({
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Cyber Intelligence Bot",
  description: "Cybersecurity Threat Intelligence and Analysis Platform",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className={`${inter.className} bg-gray-50 min-h-screen dark:bg-gray-900`} suppressHydrationWarning>
        <div className="min-h-screen bg-gradient-to-b from-gray-50 to-gray-100 dark:from-gray-900 dark:to-gray-800">
          <NavBar />
          <main className="min-h-[calc(100vh-4rem)]">
            {children}
          </main>
        </div>
      </body>
    </html>
  );
}
