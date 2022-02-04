import React from "react";
import Joi from "joi-browser";
import Form from "./common/form";
import { register } from "../services/userService";
import auth from "../services/authService";

class RegisterForm extends Form {
  state = {
    data: {
      first_name: "",
      last_name: "",
      email: "",
      username: "",
      password: "",
    },
    errors: {},
  };

  schema = {
    first_name: Joi.string().allow("").max(150).label("First Name"),
    last_name: Joi.string().allow("").max(150).label("Last Name"),
    email: Joi.string().email().required().label("Email"),
    username: Joi.string().max(150).required().label("Username"),
    password: Joi.string().min(8).required().label("Password"),
  };

  doSubmit = async () => {
    try {
      const { data } = await register(this.state.data);
      auth.loginWithJwt(data.token);
      window.location = "/";
    } catch (ex) {
      if (ex.response && ex.response.status === 400) {
        const errors = ex.response.data;
        this.setState({ errors });
      }
    }
  };

  render() {
    return (
      <div>
        <h1>Register</h1>
        <form onSubmit={this.handleSubmit}>
          {this.renderInput("first_name", "First Name")}
          {this.renderInput("last_name", "Last Name")}
          {this.renderInput("email", "Email", "email")}
          {this.renderInput("username", "Username")}
          {this.renderInput("password", "Password", "password", "new-password")}
          {this.renderButton("Register")}
        </form>
      </div>
    );
  }
}

export default RegisterForm;
