import React from "react";
import BlogPosts from "../../views/BlogPosts";
import "../../global.js";
import { Card, CardHeader, ListGroup, Row, Col, Button } from "shards-react";
const axios = require("axios");

export default class UserDetails extends React.Component {
  constructor(props) {
    super(props);
    this.state = { Posts: 0, UserId: this.props.id };
    this.componentDidMount = this.componentDidMount.bind(this);
    this.followUser = this.followUser.bind(this);
  }

  async componentDidMount() {
    let config = {
      headers: {
        "content-type": "application/json"
      }
    };

    let userData = JSON.stringify({ userId: this.state.UserId });
    if (this.state.UserId !== -1) {
      const response = await axios.post(
        //"http://twistter-API.azurewebsites.net/get-user",
        "http://localhost:5000/get-user",
        userData,
        config
      );
      this.setState(response.data);
    }
  }

  async followUser() {
    let userData = JSON.stringify({
      userId: global.ValidatedUser,
      followingId: this.state.UserId
    });
    const response = await axios.post(
      //"http://twistter-API.azurewebsites.net/follow-user",
      "http://localhost:5000/follow-user",
      userData
    );
    console.log(response);
  }

  render() {
    return (
      <div>
        <p>{console.log(this.state)}</p>
        <Card small className="mb-4 pt-3">
          <CardHeader className="border-bottom text-center">
            <h2 className="mb-0">{this.state.CommonName}</h2>
            <h5>{this.state.UserName}</h5>
            <br />
            {this.props.id !== global.ValidatedUser && (
              <Button
                pill
                outline
                size="sm"
                className="mb-2"
                onClick={this.followUser}
              >
                <i className="material-icons mr-1">person_add</i> Follow
              </Button>
            )}

            <br />
            <br />
            <p>{this.state.Followers} Followers</p>
            <p>{this.state.Following} Following</p>
          </CardHeader>
          <ListGroup flush>
            <Col>
              <br />
              <Row form>
                {/* Description */}
                <Col md="12" className="form-group">
                  <label htmlFor="Description">
                    <strong>Description</strong>
                  </label>
                  <p>{this.state.Description}</p>
                </Col>
              </Row>
            </Col>
          </ListGroup>
        </Card>
        <br></br>

        <h1>{this.state.Posts} POSTS BY THIS USER</h1>

        {/* TODO: pass userId into BlogPosts 
        <BlogPosts topic="all" />
        */}
      </div>
    );
  }
}
