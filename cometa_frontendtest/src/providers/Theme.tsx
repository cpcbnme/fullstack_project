"use client";
import React from "react";
import {ThemeProvider} from "@mui/material";
import {applicationBaseTheme} from "@/utils/theme/applicationBaseTheme";

export const ApplicationThemeProvider = ({children}: {children: React.ReactNode}) => {
    return (
        <ThemeProvider theme={applicationBaseTheme}>{children}</ThemeProvider>
    );
};