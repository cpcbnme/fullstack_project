import { createTheme } from "@mui/material";


const applicationBaseTheme = createTheme({
    // set to dark mode
    palette: {
        mode: "dark",
        primary: {
            main: "#E7FF55"
        },
        secondary: {
            main: "#393A3A"
        }
    },
    typography: {
        fontFamily: "Inter"
    }
})


export { applicationBaseTheme };