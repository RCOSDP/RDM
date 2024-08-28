import { BrowserRouter, Routes, Route } from "react-router-dom"
import CssBaseline from "@mui/material/CssBaseline"
import { createTheme, ThemeProvider } from "@mui/material/styles"
import { ErrorBoundary } from "react-error-boundary"
import { RecoilRoot } from "recoil"

import ErrorFallback from "@/pages/ErrorFallback"
import Home from "@/pages/Home"

const theme = createTheme({
  palette: {
    primary: {
      main: "#31363F",
    },
    secondary: {
      main: "#3f51b5",
    },
    background: {
      default: "#FFFFFF",
    },
  },
})

function App() {
  return (
    <BrowserRouter>
      <RecoilRoot>
        <ThemeProvider theme={theme}>
          <CssBaseline />
          <ErrorBoundary FallbackComponent={ErrorFallback}>
            <Routes>
              <Route path="/" element={<Home />} />
            </Routes>
          </ErrorBoundary>
        </ThemeProvider>
      </RecoilRoot>
    </BrowserRouter>
  )
}

export default App
