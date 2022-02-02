import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./App";
import logger from "./services/logService";
import reportWebVitals from "./reportWebVitals";

logger.init();

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById("root")
);

reportWebVitals();
