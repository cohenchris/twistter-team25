import React from "react";
import NavigationBar from "../components/NavigationBar";
import { Form, Button, Col } from "react-bootstrap";
import { FormInput } from "shards-react";
import { otherDivStyle } from "..";

export default class CreateNewAccount extends React.Component {
  render() {
    return (
      <div className="CreateNewAccount" style={otherDivStyle}>
        <NavigationBar />
        <h1>CREATE A NEW ACCOUNT</h1>
        <NewUserForm />
      </div>
    );
  }
}

class NewUserForm extends React.Component {
  render() {
    return (
      <Form>
        <Form.Row>
          <Col>
            <Form.Group controlId="FirstName" required>
              <Form.Label>First Name</Form.Label>
              <Form.Control type="text" placeholder="First Name" required />
            </Form.Group>
          </Col>
          <Col>
            <Form.Group controlId="LastName">
              <Form.Label>Last Name</Form.Label>
              <Form.Control type="text" placeholder="Last Name" required />
            </Form.Group>
          </Col>
        </Form.Row>
        <Form.Row>
          <Col>
            <Form.Group controlId="Email">
              <Form.Label>Email</Form.Label>
              <Form.Control
                type="email"
                placeholder="example@website.com"
                required
              />
            </Form.Group>
          </Col>
          <Col>
            <Form.Group controlId="Username">
              <Form.Label>Username</Form.Label>
              <Form.Control type="text" placeholder="Username" required />
            </Form.Group>
          </Col>
        </Form.Row>
        <Form.Row>
          <Col>
            <label>Birthday (MM/DD/YYYY)</label>
            <FormInput placeholder="MM/DD/YYYY" required></FormInput>
          </Col>
          <Col>
            <label>Phone Number</label>
            <FormInput placeholder="555-555-5555" required></FormInput>
          </Col>
        </Form.Row>
        <Form.Row>
          <Form.Group controlId="password">
            <Form.Label>Password</Form.Label>
            <Form.Control type="password" placeholder="Password" required />
            <br></br>
            <Form.Control
              type="password"
              placeholder="Enter Password Again"
              required
            />
          </Form.Group>
        </Form.Row>
        <br></br>
        <Form.Check
          id="agree"
          label={"I Agree To The Terms & Conditions"}
          required
        />
        <br></br>
        <Button type="submit" variant="dark">
          Create Account
        </Button>
      </Form>
    );
  }
}
