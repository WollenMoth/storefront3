import { Fragment, useState, useEffect } from "react";
import { Navigate, Route, Routes } from "react-router-dom";
import { ToastContainer } from "react-toastify";
import NavBar from "./components/navBar";
import HomePage from "./components/homePage";
import NotFound from "./components/notFound";
import Products from "./components/products";
import LoginForm from "./components/loginForm";
import Logout from "./components/logout";
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
          <Route path="/logout" element={<Logout />} />
          <Route path="/login" element={<LoginForm />} />
          <Route path="/products" element={<Products />} />
          <Route path="/not-found" element={<NotFound />} />
          <Route path="/" element={<HomePage />} />
          <Route path="*" element={<Navigate to="/not-found" />} />
        </Routes>
      </main>
    </Fragment>
  );
}

export default App;
