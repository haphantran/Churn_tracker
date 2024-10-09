// pages/_app.tsx
import type { AppProps } from 'next/app'
import { AuthProviderComponent } from '../contexts/AuthContext' // Import AuthProviderComponent

export default function MyApp({ Component, pageProps }: AppProps) {
  return (
    <AuthProviderComponent>
      <Component {...pageProps} />
    </AuthProviderComponent>
  )
}