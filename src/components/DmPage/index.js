import React from "react";
import Messenger from "../Messenger";
import NavigationBar from "../NavigationBar";
import { DMPageStyle } from "../..";

export default class DmPage extends React.Component {
  constructor(props) {
    super(props);
    let receive;
    console.log("1");
    console.log(this.props.location);
    if (
      this.props.location === undefined ||
      this.props.location.state === undefined ||
      this.props.location.state.receiver === undefined
    ) {
      console.log("3");
      receive = -1;
    } else {
      receive = this.props.location.state.receiver;
    }
    this.state = { sender: global.ValidatedUser, receiver: receive };
    console.log("receive: " + receive);
  }
  render() {
    return (
      <div className="DmPage" style={DMPageStyle}>
        <NavigationBar />
        <Messenger sender={this.state.sender} receiver={this.state.receiver} />
      </div>
    );
  }
}
