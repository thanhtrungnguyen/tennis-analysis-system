import React from "react";
import {store} from "./state/store.ts";
import {createStore} from "@reduxjs/toolkit";
export default props()=>{
    return(
        <Provider store={createStore(store,{})}>

        </Provider>
    )
}