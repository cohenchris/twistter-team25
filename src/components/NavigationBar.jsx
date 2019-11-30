import React from "react";
import {
  Nav,
  Navbar,
  NavDropdown,
  Form,
  FormControl,
  Button,
  Container,
  Col
} from "react-bootstrap";
import { Link } from "react-router-dom";

const navBarStyle = {
  color: "white"
};

export default class NavigationBar extends React.Component {
  handleClick(page) {
    /* Redirect to appropriate page here */
  }
  render() {
    return (
      <div>
        <Container>
          <Navbar bg="dark" variant="dark" fixed="top">
            <Navbar.Brand>
              <Link to="/home" style={navBarStyle}>
                Twistter
              </Link>
            </Navbar.Brand>
            {/* Website Title, #all, and Profile */}
            <Nav className="mr-auto">
              <NavDropdown title="Profile">
                <NavDropdown.Item>My Profile</NavDropdown.Item>
                <NavDropdown.Item>Settings</NavDropdown.Item>
                <NavDropdown.Divider />
                <NavDropdown.Item>Log Out</NavDropdown.Item>
              </NavDropdown>
              <NavDropdown title="Topics">
                <NavDropdown.Item>All Topics</NavDropdown.Item>
                <NavDropdown.Item>Home</NavDropdown.Item>
                <NavDropdown.Divider />
                <NavDropdown.Item>Sports</NavDropdown.Item>
                <NavDropdown.Item>Animals</NavDropdown.Item>
                <NavDropdown.Item>Art</NavDropdown.Item>
                <NavDropdown.Item>Beauty</NavDropdown.Item>
                <NavDropdown.Item>Computer Science</NavDropdown.Item>
                <NavDropdown.Item>Memes</NavDropdown.Item>
                <NavDropdown.Item>Music</NavDropdown.Item>
                <NavDropdown.Item>Politics</NavDropdown.Item>
              </NavDropdown>
            </Nav>
            {/* Create a New Microblog */}
            <Col>
              <Nav className="float-right">
                <Link to="/create-microblog" style={navBarStyle}>
                  <Button variant="outline-light">
                    + Create A New Microblog
                  </Button>
                </Link>
              </Nav>
            </Col>
            {/* Search Bar */}
            <Form>
              <Nav>
                <FormControl
                  type="text"
                  placeholder="Search"
                  className="mr-sm-2"
                />
                <Button variant="outline-light" type="submit">
                  Go!
                </Button>
              </Nav>
            </Form>
          </Navbar>
        </Container>
      </div>
    );
  }
}
