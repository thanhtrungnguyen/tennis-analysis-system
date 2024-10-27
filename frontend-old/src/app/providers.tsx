"use client";

import { NextUIProvider } from "@nextui-org/react";
import { ThemeProvider } from "next-themes";
import { Provider } from "react-redux";
import store from "@/app/store/store";

export default function Providers({ children }: { children: React.ReactNode }) {
  return (
    <Provider store={store}>
      <NextUIProvider>
        <ThemeProvider
          attribute="class"
          defaultTheme="dark"
          themes={["light", "dark", "modern"]}
        >
          {children}
        </ThemeProvider>
      </NextUIProvider>
    </Provider>
  );
}
