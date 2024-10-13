import { createTheme } from "@nextui-org/react";

export const myCustomTheme = createTheme({
  type: "light", // or 'dark'
  theme: {
    colors: {
      primary: "#0070F3", // Example: change the primary color
      secondary: "#7928CA", // Example: secondary color
      background: "#f0f0f0", // Example: background color
      text: "#333333", // Example: text color
    },
    space: {},
    fonts: {
      sans: "'Inter', sans-serif",
    },
  },
});
