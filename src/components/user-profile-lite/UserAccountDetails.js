import React, { useState } from "react";
import {
  Card,
  CardHeader,
  ListGroup,
  ListGroupItem,
  Row,
  Col,
  Form,
  FormInput,
  FormTextarea,
  Button
} from "shards-react";
import Alert from "react-bootstrap/Alert";
const axios = require("axios");

class UserAccountDetails extends React.Component {
  constructor() {
    super();

    this.state = {
      UserName: "kbuzza",
      Password:
        "AgAAAL3TGAwoCfdc9WzoMWuCya/6t3+9qUHeULhpxwcy+VBSPuaySpwyCAcOgFo5FntJfQ==",
      CommonName: "Kyle",
      Email: "kbuzza@purdue.edu",
      Description: "This is my description.",
      passwordInvalid: false
    };
    this.handleName = this.handleName.bind(this);
    this.handleFirstPassword = this.handleFirstPassword.bind(this);
    this.handleSecondPassword = this.handleSecondPassword.bind(this);
    this.handleDescription = this.handleDescription.bind(this);
    this.submitForm = this.submitForm.bind(this);
    //this.updateUserDetails = this.updateUserDetails.bind(this);
  }

  /*
  updateUserDetails(post_data) {
    //TODO: /get-user-id-from-email
    const common_name_response = axios.post(
      "http://twistter-API.azurewebsites.net/user-update-common-name",
      post_data
    );
    console.log(common_name_response);
    const description_response = axios.post(
      "http://twistter-API.azurewebsites.net/user-update-description",
      post_data
    );
    console.log(description_response);
    const password_response = axios.post(
      "http://twistter-API.azurewebsites.net/update-password",
      post_data
    );
    console.log(password_response);
  }
*/
  submitForm() {
    if (this.state.FirstPassword.localeCompare(this.state.SecondPassword)) {
      this.setState({ passwordInvalid: true });
    } else {
      this.setState({ passwordInvalid: false });

      /* Random lowercase shit is to communicate with the api better */
      // TODO:
      const userSubmission = {
        UserName: this.state.UserName,
        newPassword: this.state.FirstPassword,
        newCommonName: this.state.CommonName,
        Email: this.state.Email,
        newDescription: this.state.Description
      };

      //TODO: COMMUNICATE WITH API
      //this.updateUserDetails(userSubmission);
      console.log(userSubmission);
    }
  }

  handleName(e) {
    this.setState({ CommonName: e.target.value });
  }

  handleFirstPassword(e) {
    this.setState({ FirstPassword: e.target.value });
  }

  handleSecondPassword(e) {
    this.setState({ SecondPassword: e.target.value });
  }

  handleDescription(e) {
    this.setState({ Description: e.target.value });
  }

  render() {
    return (
      <Card small className="mb-4" bg="secondary">
        <CardHeader className="border-bottom">
          <h6 className="m-0">Account Details</h6>
        </CardHeader>
        <ListGroup flush>
          <ListGroupItem className="p-3">
            <Col>
              <Form>
                <Row form>
                  {/* Name */}
                  <Col md="6" className="form-group">
                    <label htmlFor="DisplayName">Display Name</label>
                    <FormInput
                      id="DisplayName"
                      name="DisplayName"
                      placeholder="Display Name"
                      defaultValue={this.state.CommonName}
                      onChange={this.handleName}
                    />
                  </Col>
                  {/*
                  {/* Email /}
                  <Col md="6" className="form-group">
                    <label htmlFor="feEmail">Email</label>
                    <FormInput
                      type="email"
                      id="Email"
                      name="Email"
                      defaultValue={this.state.Email}
                      placeholder="Email Address"
                      onChange={this.handleEmail}
                      autoComplete="email"
                    />
                  </Col>
                  */}
                </Row>
                <Row form>
                  {/* Password */}
                  <Col md="6" className="form-group">
                    <label htmlFor="Password">Change Password</label>
                    <FormInput
                      type="password"
                      id="Password"
                      name="Password"
                      placeholder="Password"
                      onChange={this.handleFirstPassword}
                      autoComplete="current-password"
                    />
                    <label htmlFor="PasswordConfirm">
                      Confirm Password Change
                    </label>
                    <FormInput
                      type="password"
                      id="PasswordConfirm"
                      name="PasswordConfirm"
                      placeholder="Password"
                      onChange={this.handleSecondPassword}
                      autoComplete="current-password"
                    />
                    {this.state.passwordInvalid && (
                      <p>Passwords must match and be valid strings!</p>
                    )}
                  </Col>
                </Row>
                <Row form>
                  {/* Description */}
                  <Col md="12" className="form-group">
                    <label htmlFor="Description">Description</label>
                    <FormTextarea
                      id="Description"
                      name="Description"
                      defaultValue={this.state.Description}
                      placeholder="Description"
                      rows="5"
                      onChange={this.handleDescription}
                    />
                  </Col>
                </Row>
                <Row>
                  <Col>
                    <Button theme="dark" onClick={this.submitForm}>
                      Update Account
                    </Button>
                  </Col>
                  <Col>
                    <DeleteAccountButton />
                  </Col>
                </Row>
              </Form>
            </Col>
          </ListGroupItem>
        </ListGroup>
      </Card>
    );
  }
}

function DeleteAccountButton() {
  const [show, setShow] = useState(false);

  return (
    <>
      <Alert variant="danger" show={show}>
        <Alert.Heading>WARNING</Alert.Heading>
        <p>CONTINUING WILL PERMANENTLY DELETE YOUR ACCOUNT!</p>
        <hr />
        <Button onClick={() => setShow(false)}>
          Yes, I would like to permanently delete my account.
        </Button>
      </Alert>

      {!show && (
        <Button className="float-right" onClick={() => setShow(true)}>
          Delete Account
        </Button>
      )}
    </>
  );
}

export default UserAccountDetails;
