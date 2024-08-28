import Box from "@mui/material/Box"

import AppFooter from "@/components/AppFooter"
import AppHeader from "@/components/AppHeader"

export default function Home() {
  return (
    <Box sx={{ display: "flex", flexDirection: "column", minHeight: "100vh" }}>
      <Box sx={{ flexGrow: 1 }}>
        <AppHeader />
        foo
      </Box>
      <AppFooter />
    </Box>
  )
}
