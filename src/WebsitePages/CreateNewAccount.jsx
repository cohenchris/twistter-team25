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
    let isValid = true;
    if (
      !fields["password"].match(
        /^(?=.*[a-z])+(?=.*[A-Z])+(?=.*\d)+(?=.*[~`!@#$%^&*()_\-+=:?])+[A-Za-z\d~`!@#$%^&*()_\-+=:?]{8,20}$/
      )
    ) {
      errors["password"] =
        "Password must be between 8-20 characters and contain at least one uppercase letter, lowercase letter, number, and special character.";
      isValid = false;
    } else if (fields["password"].localeCompare(fields["password_duplicate"])) {
      errors["password_duplicate"] = "Passwords must match";
      isValid = false;
    }
    if (
      !fields["bday"].match(/^((0|1)\d{1})\/((0|1|2)\d{1})\/((19|20)\d{2})$/)
    ) {
      errors["bday"] = "Birthday must be in the format 'MM/DD/YYYY'";
      isValid = false;
    }
    if (!fields["phone"].match(/^\d{3}-\d{3}-\d{4}$/)) {
      errors["phone"] = "Phone number must be in the format '###-###-####'";
      isValid = false;
    }
    this.setState({ errors: errors });
    return isValid;
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
      //fields["password"] = "";
      errors["password"] = "";
      //fields["password_duplicate"] = "";
      errors["password_duplicate"] = "";
      //fields["phone"] = "";
      errors["phone"] = "";
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
            <FormInput
              placeholder="MM/DD/YYYY"
              name="bday"
              onChange={this.handleChange}
              isInvalid={!validate_birthday(this.state.fields.bday)}
              required
            ></FormInput>
            <p className="errMsg">{this.state.errors.bday}</p>
          </Col>
          <Col>
            <label>Phone Number</label>
            <FormInput
              placeholder="###-###-####"
              name="phone"
              onChange={this.handleChange}
              isInvalid={!validate_phone(this.state.fields.phone)}
              required
            ></FormInput>
            <p className="errMsg">{this.state.errors.phone}</p>
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
              name="password_duplicate"
              placeholder="Enter Password Again"
              value={this.state.fields.password_duplicate}
              onChange={this.handleChange}
              required
            />
            <p className="errMsg">{this.state.errors.password_duplicate}</p>
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
  if (typeof pass === "undefined" || pass === "") {
    return true;
  }
  return /^(?=.*[a-z])+(?=.*[A-Z])+(?=.*\d)+(?=.*[~`!@#$%^&*()_\-+=:?])+[A-Za-z\d~`!@#$%^&*()_\-+=:?]{8,20}$/.test(
    pass
  );
}

function validate_birthday(bday) {
  if (typeof bday === "undefined" || bday === "") {
    return true;
  }
  return /^((0|1)\d{1})\/((0|1|2)\d{1})\/((19|20)\d{2})$/.test(bday);
}

function validate_phone(phone) {
  if (typeof phone === "undefined" || phone === "") {
    return true;
  }
  return /^\d{3}-\d{3}-\d{4}$/.test(phone);
}
