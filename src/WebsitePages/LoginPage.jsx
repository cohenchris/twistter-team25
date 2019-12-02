import React from "react";
import { Form, Button, Nav, Row, Alert } from "react-bootstrap";
import NavigationBar from "../components/NavigationBar";
import { Link } from "react-router-dom";
import { otherDivStyle } from "..";
import { blackLink } from "../index.js";
const axios = require("axios");

export default class LoginPage extends React.Component {
  render() {
    return (
      <div className="LoginPage" style={otherDivStyle}>
        <NavigationBar />
        <h1>LOGIN PAGE</h1>
        <LoginBoxes />
      </div>
    );
  }
}

class LoginBoxes extends React.Component {
  constructor() {
    super();

    this.state = {
      username: "",
      password: ""
    };
    this.handleUserName = this.handleUserName.bind(this);
    this.handlePassword = this.handlePassword.bind(this);
    this.submitLoginRequest = this.submitLoginRequest.bind(this);
  }

  handleUserName(e) {
    this.setState({ username: e.target.value });
  }

  handlePassword(e) {
    this.setState({ password: e.target.value });
  }

  async submitLoginRequest() {
    let config = {
      headers: {
        "content-type": "application/json"
      }
    };
    const response = await axios.post(
      //"http://twistter-API.azurewebsites.net/validate-login",
      "http://localhost:5000/validate-login",
      this.state,
      JSON.stringify(config)
    );
    console.log(response);
    if (response.data == -1) {
      window.alert("Login Failed.");
    } else {
      window.alert("Login Success!");
    }
    this.setState({ password: "" });
    global.ValidatedUser = response.data;
  }

  render() {
    return (
      <Form>
        <Row>
          <Form.Group controlId="UserName">
            <Form.Label>Username</Form.Label>
            <Form.Control
              type="text"
              placeholder="Enter Username"
              onChange={this.handleUserName}
              required
            />
          </Form.Group>
        </Row>
        <Row>
          <Form.Group controlId="Password">
            <Form.Label>Password</Form.Label>
            <Form.Control
              type="password"
              placeholder="Password"
              onChange={this.handlePassword}
              required
            />
          </Form.Group>
        </Row>
        <Row>
          <Button variant="dark" onClick={this.submitLoginRequest}>
            Submit
          </Button>
        </Row>
        <Row>
          <Nav className="mr-auto">
            {/* RE-ROUTE TO CREATE NEW ACCOUNT PAGE */}
            <Nav.Link>
              <Link to="/create-account" style={blackLink}>
                New User? Click Here!
              </Link>
            </Nav.Link>
          </Nav>
        </Row>
      </Form>
    );
  }
}
