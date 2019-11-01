/* eslint jsx-a11y/anchor-is-valid: 0 */

import React, { useState } from "react";
import { Container, Row, Col, Card, CardBody, Badge } from "shards-react";
import { ToggleButton, ToggleButtonGroup, Button } from "react-bootstrap";
const axios = require("axios");

export default class BlogPosts extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      PostsList: [
        {
          PostId: 2,
          PostTitle: "Post 1 Title",
          PostText: "Post 1",
          Topics: "Gaming,All",
          Timestamp: "2019-10-24T20:56:56",
          b: [
            {
              UserId: 1,
              UserName: "kbuzza",
              CommonName: "Kyle",
              Likes: 0,
              Retweets: 0
            }
          ]
        },
        {
          PostId: 3,
          PostTitle: "Post 2 Title",
          PostText: "Post 2",
          Topics: "Sports,News,All",
          Timestamp: "2019-10-24T20:56:56",
          b: [
            {
              UserId: 1,
              UserName: "kbuzza",
              CommonName: "Kyle",
              Likes: 0,
              Retweets: 0
            }
          ]
        },
        {
          PostId: 4,
          PostTitle: "Post 3 Title",
          PostText: "Post 3",
          Topics: "Gaming,Entertainment,All",
          Timestamp: "2019-10-24T20:56:56",
          b: [
            {
              UserId: 1,
              UserName: "kbuzza",
              CommonName: "Kyle",
              Likes: 0,
              Retweets: 0
            }
          ]
        },

        {
          PostId: 1,
          PostTitle: "Post 4 Title",
          PostText: "Post 4",
          Topics: "Gaming,All",
          Timestamp: "2019-10-24T19:08:11",
          b: [
            {
              UserId: 1,
              UserName: "kbuzza",
              CommonName: "Kyle",
              Likes: 0,
              Retweets: 0
            }
          ]
        }
      ]
    };
  }

  /*
  async componentDidMount() {
    await axios
      .post(
        //"http://twistter-API.azurewebsites.net/get-all-posts"
        "http://localhost:5000/get-all-posts"
      )
      .then(response => {
        const PostsList = [];
        PostsList.push(response);
        this.setState({ PostsList });
      });
  }
  */

  render() {
    const { PostsList } = this.state;
    //console.log(PostsList);
    return (
      <Container fluid className="main-content-container px-4">
        {/* Page Header */}
        <Row noGutters className="page-header py-4"></Row>
        <Row>
          {PostsList.map((post, idx) => (
            <Col lg="3" md="6" sm="12" className="mb-4" key={idx}>
              <Card small className="card-post card-post--1">
                <div className="card-post__image">
                  <Col>
                    <Badge pill className={`card-post__category bg-dark`}>
                      {post.Topics}
                    </Badge>
                    {/* TODO: make it so that this button only shows up when the post is created by the currently logged in user! */}
                    <Button size="sm" variant="danger" className="float-right">
                      X
                    </Button>
                  </Col>
                  <Col>
                    <div className="card-post__author d-flex">
                      <a
                        href="#"
                        className="card-post__author-avatar card-post__author-avatar--small"
                      >
                        {post.b[0].CommonName +
                          " (@" +
                          post.b[0].UserName +
                          ")"}
                      </a>
                    </div>
                  </Col>
                </div>
                <Col>
                  <div>
                    <span className="text-muted">
                      {post.Timestamp.substr(0, 10) +
                        " at " +
                        post.Timestamp.substr(11)}
                    </span>
                  </div>
                </Col>
                <CardBody>
                  <h5 className="card-title">{post.PostTitle}</h5>
                  <p className="card-text d-inline-block mb-3">
                    {post.PostText}
                  </p>
                  <LikeAndQuoteButtons
                    like_count={post.b[0].Likes}
                    quote_count={post.b[0].Retweets}
                  />
                </CardBody>
              </Card>
            </Col>
          ))}
        </Row>
      </Container>
    );
  }
}

const LikeAndQuoteButtons = props => {
  const [button, setButton] = useState();
  const [likes, setLikes] = useState(props.like_count);
  const [quotes, setQuotes] = useState(props.quote_count);
  const handleLike = val => {
    setButton(val);
    if (val == 1) {
      setLikes(likes + 1);
    } else {
      setLikes(likes - 1);
    }
  };
  const handleQuote = val => {
    setButton(val);
    if (val == 2) {
      setQuotes(quotes + 1);
    } else {
      setQuotes(quotes - 1);
    }
  };

  return (
    <Row>
      <Col>
        <ToggleButtonGroup type="checkbox" size="sm" onChange={handleLike}>
          <ToggleButton variant="outline-dark" value={1}>
            Like
          </ToggleButton>
          <Button variant="dark" disabled>
            {likes}
          </Button>
        </ToggleButtonGroup>
      </Col>

      <Col>
        <ToggleButtonGroup type="checkbox" size="sm" onChange={handleQuote}>
          <ToggleButton variant="outline-dark" value={2}>
            Quote
          </ToggleButton>
          <Button variant="dark" disabled>
            {quotes}
          </Button>
        </ToggleButtonGroup>
      </Col>
    </Row>
  );
};

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
