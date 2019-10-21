import React from "react";
import NavigationBar from "../components/NavigationBar";
import { Form, Button, Col, Alert } from "react-bootstrap";
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
  constructor() {
    super();
    this.state = {
      fields: {},
      errors: {}
    };
    this.handleChange = this.handleChange.bind(this);
    this.submitUserRegistrationForm = this.submitUserRegistrationForm.bind(
      this
    );
  }

  validate_form() {
    let fields = this.state.fields;
    let errors = {};
    if (
      !fields["password"].match(
        /^(?=.*[a-z])+(?=.*[A-Z])+(?=.*\d)+(?=.*[~`!@#$%^&*()_\-+=:?])+[A-Za-z\d~`!@#$%^&*()_\-+=:?]{8,20}$/
      )
    ) {
      errors["password"] =
        "Password must be between 8-20 characters and contain at least one\
        uppercase letter, lowercase letter, number, and special character.";
      this.setState({ errors: errors });
      return false;
    }
    fields["password"] = "";
    this.setState({ fields: fields });
    return true;
  }

  handleChange(evt) {
    let fields = this.state.fields;
    fields[evt.target.name] = evt.target.value;
    this.setState({ fields });
  }

  submitUserRegistrationForm(e) {
    e.preventDefault();
    if (this.validate_form()) {
      let fields = {};
      let errors = {};
      fields["password"] = "";
      errors["password"] = "";
      this.setState({ fields: fields, errors: errors });
      alert("submitted");
    }
  }

  render() {
    return (
      <Form onSubmit={this.submitUserRegistrationForm}>
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
            <Form.Control
              type="password"
              name="password"
              placeholder="Password"
              value={this.state.fields.password}
              onChange={this.handleChange}
              isInvalid={!validate_password(this.state.fields.password)}
              required
            />
            <p className="errMsg">{this.state.errors.password}</p>
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

/* Validates a password that is passed into the function with the following parameters:
 * At least one uppercase letter, one lowercase letter, one number, one special
 * character, with a total length between 8 and 20 characters, inclusive.
 * TODO: clean password inputs and make sure that no SQL injection is possible.
 */

function validate_password(pass) {
  if (typeof pass == "undefined") {
    return true;
  }
  return /^(?=.*[a-z])+(?=.*[A-Z])+(?=.*\d)+(?=.*[~`!@#$%^&*()_\-+=:?])+[A-Za-z\d~`!@#$%^&*()_\-+=:?]{8,20}$/.test(
    pass
  );
}
