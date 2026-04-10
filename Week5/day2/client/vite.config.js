import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    host: true,       // bind to 0.0.0.0 so host can access
    port: 5173,       // matches docker-compose
    strictPort: true, // optional: fail if 5173 is in use
  },
})