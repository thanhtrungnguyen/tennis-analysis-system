// src/store/store.ts
import { configureStore } from "@reduxjs/toolkit";
import authReducer from "@/app/features/auth/authSlice";
import productReducer from "@/app/features/product/productSlice";

const store = configureStore({
  reducer: {
    auth: authReducer,
    product: productReducer,
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;

export default store;
