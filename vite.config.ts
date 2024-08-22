import * as fs from "fs"
import path from "path"

import { defineConfig } from "vite"
import react from "@vitejs/plugin-react"

const insideDocker = () => {
  return fs.existsSync("/.dockerenv")
}

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  root: "./src",
  build: {
    outDir: "../dist",
  },
  server: {
    host: insideDocker() ? "0.0.0.0" : "127.0.0.1",
    port: 3000,
  },
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
})
