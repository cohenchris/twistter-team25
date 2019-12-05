import React from "react";
import NavigationBar from "../../components/NavigationBar";
import "bootstrap/dist/css/bootstrap.min.css";
import BlogPosts from "../../views/BlogPosts";
import PageTitle from "../../components/common/PageTitle";
import { blogDivStyle } from "../..";
import { Button, Container, Row, Col } from "react-bootstrap";

export default class HomePage extends React.Component {
  render() {
    return (
      <div className="HomePage" style={blogDivStyle}>
        <NavigationBar />
         <Container>
          <Row>
            <Col sm={8}>
              <PageTitle
                sm="4"
                title="Blog Posts"
                subtitle="HOME"
                className="text-sm-left"
              />
            </Col>
            <Col sm={4}>
              <Button type="submit" variant="dark">
                Follow Topic
              </Button>
            </Col>
          </Row>
        </Container>
        <BlogPosts topic="all" />
      </div>
    );
  }
}
