import React from "react";
import NavigationBar from "../../components/NavigationBar";
import logo from "../../images/Logo.png";
import { blogDivStyle } from "../..";
import "./DmPage.css";

export default class DmPage extends React.Component {
    render() {
      return (
        <div className="DmPage" style={blogDivStyle}>
          <NavigationBar />
          <h1>Chats</h1>
          <Messages />
        </div>
        );
    }
}

class Messages extends React.Component {
    render() {
        return (
          <div>
          <div className="container">
            <img src={logo} alt="Avatar" height="35" width="90"/>
            <p>Hello. How are you today?</p>
            <span class="time-right">11:00</span>
          </div>

          <div className="container darker">
            <img src={logo} alt="Avatar" height="35" width="90"/>
            <p>Hey! I'm fine. Thanks for asking!</p>
            <span class="time-left">11:01</span>
          </div>

          <div className="container">
            <img src={logo} alt="Avatar" height="35" width="90"/>
            <p>Sweet! So, what do you wanna do today?</p>
            <span class="time-right">11:02</span>
          </div>

          <div className="container darker">
          <img src={logo} alt="Avatar" height="35" width="90"/>
            <p>Nah, I dunno. Play soccer.. or learn more coding perhaps?</p>
            <span class="time-left">11:05</span>
          </div>
          </div>
        );
    }
}