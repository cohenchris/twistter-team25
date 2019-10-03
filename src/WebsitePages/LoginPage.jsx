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
  render() {
    return (
      <Form>
        <Row>
          <Form.Group controlId="formBasicEmail">
            <Form.Label>Email address</Form.Label>
            <Form.Control type="email" placeholder="Enter email" required />
          </Form.Group>
        </Row>
        <Row>
          <Form.Group controlId="formBasicPassword">
            <Form.Label>Password</Form.Label>
            <Form.Control type="password" placeholder="Password" required />
          </Form.Group>
        </Row>
        <Row>
          <Button variant="dark" type="submit">
            Submit
          </Button>
        </Row>
        <Nav className="mr-auto">
          {/* RE-ROUTE TO CREATE NEW ACCOUNT PAGE */}
          <Nav.Link>New User? Click Here!</Nav.Link>
        </Nav>
      </Form>
    );
  }
}
