"use client";
import localFont from "next/font/local";
import "./globals.css";
import NavBar from "../components/NavBar";
import { AuthProviderComponent } from "../contexts/AuthContext";

const geistSans = localFont({
  src: "./fonts/GeistVF.woff",
  variable: "--font-geist-sans",
  weight: "100 900",
});
const geistMono = localFont({
  src: "./fonts/GeistMonoVF.woff",
  variable: "--font-geist-mono",
  weight: "100 900",
});

// Metadata has been moved to a separate file to comply with "use client" directive

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        <AuthProviderComponent>
          <NavBar />
          {children}
        </AuthProviderComponent>
      </body>
    </html>
  );
}
