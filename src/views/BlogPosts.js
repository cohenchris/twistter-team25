/* eslint jsx-a11y/anchor-is-valid: 0 */

import React, { useState } from "react";
import { Container, Row, Col, Card, CardBody, Badge } from "shards-react";
import ToggleButton from "react-bootstrap/ToggleButton";
import ToggleButtonGroup from "react-bootstrap/ToggleButtonGroup";

export default class BlogPosts extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      PostsList: [
        {
          category: "Business",
          categoryTheme: "dark",
          author: "Anna Kunis",
          title: "Conduct at an replied removal an amongst",
          body:
            "However venture pursuit he am mr cordial. Forming musical am hearing studied be luckily. But in for determine what would see...",
          date: "28 February 2019"
        },
        {
          category: "Travel",
          categoryTheme: "info",
          author: "James Jamerson",
          title: "Off tears are day blind smile alone had ready",
          body:
            "Is at purse tried jokes china ready decay an. Small its shy way had woody downs power. To denoting admitted speaking learning my...fffffffffffffffffff",
          date: "29 February 2019"
        },
        {
          category: "Technology",
          categoryTheme: "royal-blue",
          author: "Jimmy Jackson",
          title: "Difficult in delivered extensive at direction",
          body:
            "Is at purse tried jokes china ready decay an. Small its shy way had woody downs power. To denoting admitted speaking learning my...",
          date: "29 February 2019"
        },
        {
          category: "Business",
          categoryTheme: "warning",
          author: "John James",
          title: "It so numerous if he may outlived disposal",
          body:
            "How but sons mrs lady when. Her especially are unpleasant out alteration continuing unreserved ready road market resolution...",
          date: "29 February 2019"
        },
        {
          category: "Travel",
          categoryTheme: "info",
          author: "Anna Ken",
          title: "Attention he extremity unwilling on otherwise",
          body:
            "Conviction up partiality as delightful is discovered. Yet jennings resolved disposed exertion you off. Left did fond drew fat head poor jet pan flying over...",
          date: "29 February 2019"
        },
        {
          category: "Business",
          categoryTheme: "dark",
          author: "John James",
          title: "Totally words widow one downs few age every",
          body:
            "Discovered had get considered projection who favourable. Necessary up knowledge it tolerably. Unwilling departure education to admitted speaking...",
          date: "29 February 2019"
        },
        {
          category: "Computer Science",
          author: "John James",
          title: "Had denoting properly jointure which",
          body:
            "In said to of poor full be post face snug. Introduced imprudence see say unpleasing devonshire acceptance son. Exeter longer wisdom work...",
          date: "29 February 2019"
        },
        {
          category: "Computer Science",
          author: "John James",
          title: "Husbands ask repeated resolved but",
          body:
            "It abode words began enjoy years no do ﻿no. Tried spoil as heart visit blush or. Boy possible blessing sensible set but margaret interest. Off tears...",
          date: "29 February 2019"
        },
        {
          category: "Computer Science",
          author: "John James",
          title: "Instantly gentleman contained belonging",
          body:
            "West room at sent if year. Numerous indulged distance old law you. Total state as merit court green decay he. Steepest merit checking railway...",
          date: "29 February 2019"
        },
        {
          category: "Computer Science",
          author: "Alene Trenton",
          authorUrl: "#",
          categoryUrl: "#",
          title: "Extremity so attending objection as engrossed",
          body:
            "Pursuit chamber as elderly amongst on. Distant however warrant farther to of. My justice wishing prudent waiting in be...",
          date: "29 February 2019"
        },
        {
          category: "Computer Science",
          author: "Chris Jamie",
          authorUrl: "#",
          categoryUrl: "#",
          title: "Bed sincerity yet therefore forfeited his",
          body:
            "Speaking throwing breeding betrayed children my to. Me marianne no he horrible produced ye. Sufficient unpleasing and...",
          date: "29 February 2019"
        },
        {
          category: "Computer Science",
          author: "Monica Jordan",
          authorUrl: "#",
          categoryUrl: "#",
          title: "Object remark lively all did feebly excuse our",
          body:
            "Morning prudent removal an letters by. On could my in order never it. Or excited certain sixteen it to parties colonel not seeing...",
          date: "29 February 2019"
        },
        {
          category: "Computer Science",
          author: "Monica Jordan",
          authorUrl: "#",
          categoryUrl: "#",
          title: "His followed carriage proposal entrance",
          body:
            "For county now sister engage had season better had waited. Occasional mrs interested far expression directly as regard...",
          date: "29 February 2019"
        }
      ]
    };
  }

  render() {
    const { PostsList } = this.state;

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
                    <Badge
                      pill
                      className={`card-post__category bg-${post.categoryTheme}`}
                    >
                      {post.category}
                    </Badge>
                  </Col>
                  <Col>
                    <div className="card-post__author d-flex">
                      <a
                        href="#"
                        f
                        className="card-post__author-avatar card-post__author-avatar--small"
                      >
                        {post.author}
                      </a>
                    </div>
                  </Col>
                </div>
                <Col>
                  <div>
                    <span className="text-muted">{post.date}</span>
                  </div>
                </Col>
                <CardBody>
                  <h5 className="card-title">{post.title}</h5>
                  <p className="card-text d-inline-block mb-3">{post.body}</p>
                  <LikeAndQuoteButtons />
                </CardBody>
              </Card>
            </Col>
          ))}
        </Row>
      </Container>
    );
  }
}

export function LikeAndQuoteButtons() {
  const [button, setButton] = useState();
  const handleButtonPress = val => setButton(val);

  return (
    <ToggleButtonGroup
      type="checkbox"
      size="sm"
      value={button}
      onChange={handleButtonPress}
    >
      <ToggleButton variant="outline-dark" value={1}>
        Like
      </ToggleButton>
      <ToggleButton variant="outline-dark" value={2}>
        Quote
      </ToggleButton>
    </ToggleButtonGroup>
  );
}
