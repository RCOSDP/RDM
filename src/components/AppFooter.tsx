import { Box, Typography } from "@mui/material"
import { SxProps } from "@mui/system"

interface AppFooterProps {
  sx?: SxProps
}

export default function AppFooter({ sx }: AppFooterProps) {
  return (
    <Box sx={{ ...sx }}>
      <Box sx={{ display: "flex", justifyContent: "center", mb: "1.5rem" }}>
        <Typography sx={{ fontSize: "12px" }}>
          {"Copyright NII 2024, Japan"}
        </Typography>
      </Box>
    </Box>
  )
}
