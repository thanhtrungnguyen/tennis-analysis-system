import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
// import {ReactDOM} from "react";
// import {BrowserRouter,Route} from "react-router-dom";
import './index.css'
import { App } from './components/App/App';
// import Root from './components/Root'


createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
