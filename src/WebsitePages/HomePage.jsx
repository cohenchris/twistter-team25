import React from "react";
import NavigationBar from "../components/NavigationBar";
import "bootstrap/dist/css/bootstrap.min.css";
import BlogPosts from "../views/BlogPosts";
import PageTitle from "../components/common/PageTitle";
import { blogDivStyle } from "..";

export default class HomePage extends React.Component {
  render() {
    return (
      <div className="HomePage" style={blogDivStyle}>
        <NavigationBar />
        <PageTitle
          sm="4"
          title="Blog Posts"
          subtitle="Your Followed Topics"
          className="text-sm-left"
        />
        <BlogPosts />
      </div>
    );
  }
}
