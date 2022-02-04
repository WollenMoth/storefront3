import { Fragment, useState, useEffect } from "react";
import { Route, Routes } from "react-router-dom";
import { ToastContainer } from "react-toastify";
import NavBar from "./components/NavBar";
import HomePage from "./components/HomePage";
import Products from "./components/Products";
import auth from "./services/authService";
import "./App.css";

function App() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const result = auth.getCurrentUser();
    setUser(result);
  }, []);

  return (
    <Fragment>
      <ToastContainer />
      <NavBar user={user} />
      <main className="container">
        <Routes>
          <Route path="/products" element={<Products />} />
          <Route path="/" element={<HomePage />} />
        </Routes>
      </main>
    </Fragment>
  );
}

export default App;
