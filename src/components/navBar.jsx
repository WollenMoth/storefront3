import React, { Fragment } from "react";
import { Link, NavLink } from "react-router-dom";

function NavBar({ user }) {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
      <div className="container-fluid">
        <Link className="navbar-brand" to="/">
          Andrebuy
        </Link>
        <button
          className="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarSupportedContent">
          <ul className="navbar-nav me-auto mb-2 mb-lg-0">
            <li className="nav-item">
              <NavLink className="nav-link" aria-current="page" to="/">
                Home
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink className="nav-link" to="/products">
                Products
              </NavLink>
            </li>
          </ul>
          <form className="d-flex align-items-end mb-lg-0">
            <input
              className="form-control me-2"
              type="search"
              placeholder="Search..."
              aria-label="Search"
            />
          </form>
          <div className="text-end">
            {!user && (
              <Fragment>
                <NavLink className="btn btn-outline-light me-2" to="/login">
                  Login
                </NavLink>
                <NavLink className="btn btn-warning" to="/register">
                  Register
                </NavLink>
              </Fragment>
            )}
            {user && (
              <Fragment>
                <NavLink className="btn btn-outline-light me-2" to="/profile">
                  {user.username}
                </NavLink>
                <NavLink className="btn btn-warning" to="/logout">
                  Logout
                </NavLink>
              </Fragment>
            )}
          </div>
        </div>
      </div>
    </nav>
  );
}

export default NavBar;
