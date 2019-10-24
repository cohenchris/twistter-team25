import React from "react";
//import PropTypes from "prop-types";
import {
  Card,
  CardHeader,
  ListGroup,
  ListGroupItem,
  Row,
  Col,
  Button,
  Progress
} from "shards-react";

export default class UserDetails extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      avatar: "../images/Chris_Test_Profile_Pic.jpg",
      name: "Chris Cohen",
      birthday: "1/8/1999",
      phone: "636-675-9358",
      email: "cohen50@purdue.edu",
      description: "please let me be done with React I wanna die"
    };
  }

  render() {
    return (
      <Card small className="mb-4 pt-3">
        <CardHeader className="border-bottom text-center">
          <div className="mb-3 mx-auto">
            {/*
            <img
              className="rounded-circle"
              src={this.state.avatar}
              alt={this.state.name}
              width="110"
            />
            */}
          </div>
          <h4 className="mb-0">{this.state.name}</h4>
          {/*<span className="text-muted d-block mb-2">{this.state.jobTitle}</span>*/}
          <br />
          <Button pill outline size="sm" className="mb-2">
            <i className="material-icons mr-1">person_add</i> Follow
          </Button>
        </CardHeader>
        <ListGroup flush>
          <ListGroupItem className="px-4">
            <div className="progress-wrapper">
              <strong className="text-muted d-block mb-2">
                {this.state.performanceReportTitle}
              </strong>
              <Progress
                className="progress-sm"
                value={this.state.performanceReportValue}
              >
                <span className="progress-value">
                  {this.state.performanceReportValue}%
                </span>
              </Progress>
            </div>
          </ListGroupItem>
          <ListGroupItem className="p-4">
            <strong className="text-muted d-block mb-2">
              {this.state.metaTitle}
            </strong>
            <span>{this.state.metaValue}</span>
          </ListGroupItem>
          <Col>
            <Row>
              {/* First Name */}
              <Col md="6" className="form-group">
                {/*<label htmlFor="feFirstName">First Name</label>*/}
                <p>{this.state.name}</p>
              </Col>
              {/* Last Name */}
              <Col md="6" className="form-group">
                {/*<label htmlFor="feLastName">Last Name</label>*/}
              </Col>
            </Row>
            <Row form>
              {/* Email */}
              <Col md="6" className="form-group">
                <p>{this.state.email}</p>
                {/*<label htmlFor="feEmail">Email</label>*/}
              </Col>
            </Row>
            <Row>
              <Col>
                {/*<label>Birthday (MM/DD/YYYY)</label>*/}
                <p>{this.state.birthday}</p>
              </Col>
              <Col>
                <p>
                  <strong>Phone Number</strong>
                </p>
                <p>{this.state.phone}</p>
                {/*
                <FormGroup controlId="phoneNum">
                  <label>Phone Number</label>
                </FormGroup>*/}
              </Col>
            </Row>
            <Row form>
              {/* Description */}
              <Col md="12" className="form-group">
                <label htmlFor="feDescription">Description</label>
              </Col>
            </Row>{" "}
          </Col>
        </ListGroup>
      </Card>
    );
  }
}
