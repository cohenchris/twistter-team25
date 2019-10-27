import React from "react";
import { Form, Button, Nav, Row } from "react-bootstrap";
import NavigationBar from "../components/NavigationBar";
import { otherDivStyle } from "..";

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
      Email: "",
      Password: ""
    };
    this.handleEmail = this.handleEmail.bind(this);
    this.handlePassword = this.handlePassword.bind(this);
    this.submitLoginRequest = this.submitLoginRequest.bind(this);
  }

  handleEmail(e) {
    this.setState({ Email: e.target.value });
  }

  handlePassword(e) {
    this.setState({ Password: e.target.value });
  }

  submitLoginRequest() {
    console.log(this.state);
    this.setState({ Password: "" });
  }

  render() {
    return (
      <Form>
        <Row>
          <Form.Group controlId="Email">
            <Form.Label>Email address</Form.Label>
            <Form.Control
              type="email"
              placeholder="Enter email"
              onChange={this.handleEmail}
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
