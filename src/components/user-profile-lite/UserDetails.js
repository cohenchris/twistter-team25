import React from "react";
import BlogPosts from "../../views/BlogPosts";
import { Card, CardHeader, ListGroup, Row, Col, Button } from "shards-react";

export default class UserDetails extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      UserName: "kbuzza",
      CommonName: "Kyle Buzza",
      Following: 0,
      Followers: 69,
      Posts: 4,
      Email: "kylesucks@purdue.edu",
      Description: "This is my description."
    };
  }

  render() {
    return (
      <div>
        <Card small className="mb-4 pt-3">
          <CardHeader className="border-bottom text-center">
            <h2 className="mb-0">{this.state.CommonName}</h2>
            <h5>{this.state.UserName}</h5>
            <br />
            <Button pill outline size="sm" className="mb-2">
              <i className="material-icons mr-1">person_add</i> Follow
            </Button>
            <br />
            <br />
            <p>{this.state.Followers} Followers</p>
            <p>{this.state.Following} Following</p>
          </CardHeader>
          <ListGroup flush>
            <Col>
              <Row form>
                {/* Email */}
                <Col md="6" className="form-group">
                  <br />
                  <label htmlFor="Email">
                    <strong>Email</strong>
                  </label>
                  <p>{this.state.Email}</p>
                  {/*<label htmlFor="feEmail">Email</label>*/}
                </Col>
              </Row>
              <Row></Row>
              <Row form>
                {/* Description */}
                <Col md="12" className="form-group">
                  <label htmlFor="Description">
                    <strong>Description</strong>
                  </label>
                  <p>{this.state.Description}</p>
                </Col>
              </Row>{" "}
            </Col>
          </ListGroup>
        </Card>
        <br></br>
        <h1>{this.state.Posts} POSTS BY THIS USER</h1>
        <BlogPosts />
      </div>
    );
  }
}
