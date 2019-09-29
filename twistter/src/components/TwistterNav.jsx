import React from "react";
import Nav from "react-bootstrap/Nav";
import NavBar from "react-bootstrap/Navbar";
import NavDropdown from "react-bootstrap/NavDropdown";
import Form from "react-bootstrap/Form";
import FormControl from "react-bootstrap/FormControl";
import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";
import "bootstrap/dist/css/bootstrap.min.css";

export default class TwistterNav extends React.Component {
  handleClick(page) {
    /* Redirect to appropriate page here */
  }
  render() {
    return (
      <div>
        <Container>
          <NavBar bg="dark" variant="dark" fixed="top">
            <NavBar.Brand>Twistter</NavBar.Brand>
            <Nav className="mr-auto">
              <Nav.Link>#all</Nav.Link>
              <NavDropdown title="Profile">
                <NavDropdown.Item>My Profile</NavDropdown.Item>
                <NavDropdown.Item>Settings</NavDropdown.Item>
                <NavDropdown.Divider />
                <NavDropdown.Item>Log Out</NavDropdown.Item>
              </NavDropdown>
            </Nav>
            <Nav>
              <Form inline>
                <FormControl
                  type="text"
                  placeholder="Search"
                  className="mr-sm-2"
                />
                <Button variant="outline-light" type="submit">
                  Go!
                </Button>
              </Form>
            </Nav>
          </NavBar>
        </Container>
        {/*THIS H1 IS TO MAKE SURE THAT TEXT ISN'T ACCIDENTALLY RENDERED UNDER THE NAVBAR */}
        <h1>navbar</h1>{" "}
      </div>
    );
  }
}
