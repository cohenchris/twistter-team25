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

const Editor = () => (
  <Card small className="mb-3">
    <CardBody>
      <Form className="add-new-post">
        <FormInput size="lg" className="mb-3" placeholder="Your Post Title" />
        <ReactQuill className="add-new-post__editor mb-1" />
        <FormGroup controlId="birthMonth">
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
      <Button type="submit" variant="dark">
        Post
      </Button>
    </CardBody>
  </Card>
);

export default Editor;
