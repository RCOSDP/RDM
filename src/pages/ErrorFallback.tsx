import { Box, Typography, Paper, Container, Button } from "@mui/material"

// import AppFooter from "@/components/AppFooter"
// import AppHeader from "@/components/AppHeader"
// import SecHeader from "@/components/SecHeader"

interface ErrorFallbackProps {
  error: Error
  resetErrorBoundary: () => void
}

export default function ErrorFallback({ error, resetErrorBoundary }: ErrorFallbackProps) {
  return (
    <Box sx={{ display: "flex", flexDirection: "column", minHeight: "100vh" }}>
      <Box sx={{ flexGrow: 1 }}>
        {/* <AppHeader /> */}
        <Container maxWidth="lg" sx={{ justifyContent: "flex-start" }}>
          {/* <SecHeader {...{
            title: "想定外のエラー",
            description: "想定外のエラーが発生しました。お手数ですが、以下の詳細情報を開発者にお伝え下さい。\n再試行ボタンをクリックすると、アプリケーションの状態が初期化され、再度読み込みが行われます。",
            sx: { margin: "1.5rem 0" },
          }}
          /> */}

          <Box sx={{ margin: "1.5rem 0" }}>
            <Typography sx={{ fontWeight: "bold", marginBottom: "0.5rem" }}>エラーメッセージ</Typography>
            <Paper variant="outlined" sx={{ padding: "0.5rem 1rem" }}>
              <Box sx={{ fontFamily: "monospace", overflowX: "auto" }}>
                <pre>{error.message}</pre>
              </Box>
            </Paper>
          </Box>

          <Box sx={{ margin: "1.5rem 0" }}>
            <Typography sx={{ fontWeight: "bold", marginBottom: "0.5rem" }}>スタックトレース</Typography>
            <Paper variant="outlined" sx={{ padding: "0.5rem 1rem" }}>
              <Box sx={{ fontFamily: "monospace", overflowX: "auto" }}>
                <pre>{error.stack}</pre>
              </Box>
            </Paper>
          </Box>

          <Box sx={{ margin: "1.5rem 0" }}>
            <Button variant="contained" color="primary" onClick={resetErrorBoundary}>
              再試行する
            </Button>
          </Box>
        </Container>
      </Box>
      {/* <AppFooter /> */}
    </Box>
  )
}
