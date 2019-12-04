import React from "react";
import ConversationList from "../ConversationList";
import MessageList from "../MessageList";
import "./Messenger.css";

export default class Messenger extends React.Component {
  constructor(props) {
    super(props);
    this.state = { sender: this.props.sender, receiver: this.props.receiver };
    console.log(this.state);
  }

  render() {
    return (
      <div className="messenger">
        <div className="scrollable sidebar">
          <ConversationList />
        </div>

        <div className=" scrollable content">
          <MessageList
            sender={this.state.sender}
            receiver={this.state.receiver}
          />
        </div>
      </div>
    );
  }
}
