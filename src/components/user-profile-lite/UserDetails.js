import React from "react";
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
  Button,
  Progress
} from "shards-react";

const UserDetails = ({ userDetails }) => (
  <Card small className="mb-4 pt-3">
    <CardHeader className="border-bottom text-center">
      <div className="mb-3 mx-auto">
        <img
          className="rounded-circle"
          src={userDetails.avatar}
          alt={userDetails.name}
          width="110"
        />
      </div>
      <h4 className="mb-0">{userDetails.name}</h4>
      <span className="text-muted d-block mb-2">{userDetails.jobTitle}</span>
      <Button pill outline size="sm" className="mb-2">
        <i className="material-icons mr-1">person_add</i> Follow
      </Button>
    </CardHeader>
    <ListGroup flush>
      <ListGroupItem className="px-4">
        <div className="progress-wrapper">
          <strong className="text-muted d-block mb-2">
            {userDetails.performanceReportTitle}
          </strong>
          <Progress
            className="progress-sm"
            value={userDetails.performanceReportValue}
          >
            <span className="progress-value">
              {userDetails.performanceReportValue}%
            </span>
          </Progress>
        </div>
      </ListGroupItem>
      <ListGroupItem className="p-4">
        <strong className="text-muted d-block mb-2">
          {userDetails.metaTitle}
        </strong>
        <span>{userDetails.metaValue}</span>
      </ListGroupItem>
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
          <Button theme="dark">Update Account</Button>
        </Form>
      </Col>
    </ListGroup>
  </Card>
);

UserDetails.propTypes = {
  /**
   * The user details object.
   */
  userDetails: PropTypes.object
};

UserDetails.defaultProps = {
  userDetails: {
    name: "Chris Cohen",
    avatar: require("./../../images/Chris_Test_Profile_Pic.jpg"),
    jobTitle: "Software Engineer",
    performanceReportTitle: "Workload",
    performanceReportValue: 74,
    metaTitle: "Description",
    metaValue: "please let me be done with React i wanna die"
  }
};

export default UserDetails;
