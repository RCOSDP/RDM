import { Box, AppBar, Typography } from "@mui/material"
import { SxProps } from "@mui/system"

interface AppHeaderProps {
  sx?: SxProps
}

export default function AppHeader({ sx }: AppHeaderProps) {
  return (
    <Box sx={{ ...sx }}>
      <AppBar position="static" sx={{ display: "flex", flexDirection: "row", justifyContent: "space-between", alignItems: "center", height: "64px" }}>
        <Box sx={{ display: "flex", flexDirection: "row", ml: "1.5rem", alignItems: "center" }}>
          <Typography sx={{ fontSize: "24px" }}>
            NII RDM-Ontology
          </Typography>
          <Box sx={{ display: "flex", flexDirection: "row", ml: "1.5rem", gap: "1rem" }}>
            <Typography sx={{ fontSize: "18px" }}>
              Docs
            </Typography>
            <Typography sx={{ fontSize: "18px" }}>
              Schemas
            </Typography>
            <Typography sx={{ fontSize: "18px" }}>
              Validate
            </Typography>
            <Typography sx={{ fontSize: "18px" }}>
              about
            </Typography>
          </Box>
        </Box>
        <Box sx={{ mr: "1.5rem", fontSize: "18px" }}>right</Box>
      </AppBar>
    </Box>
  )
}
