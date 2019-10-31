import React from "react";
import { Form, Button, Nav, Row } from "react-bootstrap";
import NavigationBar from "../components/NavigationBar";
import { otherDivStyle } from "..";
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
    this.setState({ UserName: e.target.value });
  }

  handlePassword(e) {
    this.setState({ Password: e.target.value });
  }

  async submitLoginRequest() {
    //TODO: COMMUNICATE WITH API
    const response = await axios.post(
      "twistter-API.azurewebsites.net/validate-login",
      this.state
    );
    console.log(response);
    this.setState({ password: "" });
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
            <Nav.Link>New User? Click Here!</Nav.Link>
          </Nav>
        </Row>
      </Form>
    );
  }
}
