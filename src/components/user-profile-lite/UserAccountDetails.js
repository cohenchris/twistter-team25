import React, { useState } from "react";
import PropTypes from "prop-types";
import {
  Card,
  CardHeader,
  ListGroup,
  ListGroupItem,
  Row,
  Col,
  Form,
  FormGroup,
  FormInput,
  FormTextarea,
  Button
} from "shards-react";
import Alert from "react-bootstrap/Alert";
import FormCheck from "react-bootstrap/FormCheck";

const UserAccountDetails = ({ title }) => (
  <Card small className="mb-4" bg="secondary">
    <CardHeader className="border-bottom">
      <h6 className="m-0">{title}</h6>
    </CardHeader>
    <ListGroup flush>
      <ListGroupItem className="p-3">
        <Col>
          <Form>
            <Row form>
              {/* First Name */}
              <Col md="6" className="form-group">
                <label htmlFor="feFirstName">First Name</label>
                <FormInput
                  id="feFirstName"
                  placeholder="First Name"
                  required
                  onChange={() => {}}
                />
              </Col>
              {/* Last Name */}
              <Col md="6" className="form-group">
                <label htmlFor="feLastName">Last Name</label>
                <FormInput
                  id="feLastName"
                  placeholder="Last Name"
                  required
                  onChange={() => {}}
                />
              </Col>
            </Row>
            <Row form>
              {/* Email */}
              <Col md="6" className="form-group">
                <label htmlFor="feEmail">Email</label>
                <FormInput
                  type="email"
                  id="feEmail"
                  placeholder="Email Address"
                  required
                  onChange={() => {}}
                  autoComplete="email"
                />
              </Col>
              {/* Password */}
              <Col md="6" className="form-group">
                <label htmlFor="fePassword">Change Password</label>
                <FormInput
                  type="password"
                  id="fePassword"
                  placeholder="Password"
                  required
                  onChange={() => {}}
                  autoComplete="current-password"
                />
                <label htmlFor="fePassword">Confirm Password Change</label>
                <FormInput
                  type="password"
                  id="fePassword"
                  placeholder="Password"
                  required
                  onChange={() => {}}
                  autoComplete="current-password"
                />
              </Col>
            </Row>
            <Row>
              <Col>
                <label>Birthday (MM/DD/YYYY)</label>
                <FormInput placeholder="MM/DD/YYYY" required />
              </Col>
              <Col>
                <FormGroup controlId="phoneNum">
                  <label>Phone Number</label>
                  <FormInput placeholder="555-555-5555" required></FormInput>
                </FormGroup>
              </Col>
              <Col>
                <label>Publicize Birthday and Phone Number?</label>
                <FormCheck type="checkbox"></FormCheck>
              </Col>
            </Row>
            <Row form>
              {/* Description */}
              <Col md="12" className="form-group">
                <label htmlFor="feDescription">Description</label>
                <FormTextarea
                  id="feDescription"
                  placeholder="Description here..."
                  rows="5"
                  required
                />
              </Col>
            </Row>
            <Row>
              <Col>
                <Button theme="dark">Update Account</Button>
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

UserAccountDetails.propTypes = {
  /**
   * The component's title.
   */
  title: PropTypes.string
};

UserAccountDetails.defaultProps = {
  title: "Account Details"
};

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
