import React from "react";
import ReactQuill from "react-quill";
import {
  Card,
  CardBody,
  Form,
  FormInput,
  FormGroup,
  FormSelect
} from "shards-react";
import Button from "react-bootstrap/Button";

import "react-quill/dist/quill.snow.css";
import "../../assets/quill.css";

export default class Editor extends React.Component {
  constructor() {
    super();
    this.state = {
      post_characters_remaining: 150,
      valid_post: true,
      text: ""
    };
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(text_value) {
    let post_characters_remaining = this.state.post_characters_remaining;
    let valid_post = this.state.valid_post;
    this.setState({ text: text_value });

    /* strips html text so real length of post body is obtained */
    var html = this.state.text;
    var div = document.createElement("div");
    div.innerHTML = html;
    var stripped_text = div.textContent || div.innerText || "";

    post_characters_remaining = 150 - stripped_text.length;
    if (post_characters_remaining < 0) {
      valid_post = false;
    } else {
      valid_post = true;
    }
    this.setState({
      post_characters_remaining: post_characters_remaining,
      valid_post: valid_post
    });
  }

  render() {
    return (
      <Card small className="mb-3">
        <CardBody>
          <Form className="add-new-post">
            <FormInput
              size="lg"
              className="mb-3"
              placeholder="Your Post Title"
              maxLength={45}
              required
            />
            <ReactQuill
              className="add-new-post__editor mb-1"
              name="post_text_box"
              value={this.state.text}
              onChange={this.handleChange}
              required
            />
            <p>{this.state.characters_remaining} characters remaining</p>
            <FormGroup controlId="topicSelect">
              <FormSelect placeholder="Topic" as="select" value="All">
                <option>All</option>
                <option>Music</option>
                <option>Computer Science</option>
                <option>Politics</option>
                <option>Beauty</option>
                <option>Animals</option>
                <option>Memes</option>
                <option>Art</option>
                <option>Sports</option>
              </FormSelect>
            </FormGroup>
          </Form>
          {!this.state.valid_post && (
            <Button type="submit" variant="dark" disabled>
              Post
            </Button>
          )}
          {this.state.valid_post && (
            <Button type="submit" variant="dark">
              Post
            </Button>
          )}
        </CardBody>
      </Card>
    );
  }
}
