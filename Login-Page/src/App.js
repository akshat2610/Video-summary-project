import React, {Component} from 'react';
import { BrowserRouter as Router, Route } from "react-router-dom";
import Login from './login.jsx';
import NavBar from './NavBar.jsx';
import { PrivateRoute } from "./PrivateRoute.jsx";
import {isLoggedIn} from './auth.js';
import axios from 'axios'; 
import logo from './summarAIze.png';
import useSignUpForm from './CustomHooks';
import './App.css';

const Home = ()=> <h3>Logged in as {localStorage.getItem("username")}</h3>

function App() {
  return (
    <>

    <div className="App">
      <header className="App-header">
        <img style={{ height: '60px'}} src={logo} className="App-logo" alt="logo" />
        &nbsp; &nbsp; &nbsp; Sign In or Sign Up with summarAIze to save your videos and documents
        <Router>
        <div>
          <NavBar/>
          <PrivateRoute exact isloggedin={isLoggedIn()} path="/" component={Home} />
          <Route exact path="/login" component={Login} />
      </div>
    </Router>
        
        {/* <button type="password">Sign Up</button> */}
        {/* <form>
          <label>Username</label>
          <input type="text"/>
          <label> Password</label>
          <input type="password"/>
          <button type="password">Login</button>
      </form> */}
      </header>
      
      
      
    </div>
    </>
  );
}

export default App;

