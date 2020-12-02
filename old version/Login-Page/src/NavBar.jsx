import React from "react";
import {Navbar,Nav,NavItem, Button} from "react-bootstrap";
import {Link} from 'react-router-dom';
import logo from './coutloot-logo.png'
import {isLoggedIn, deleteTokens} from './auth.js';

import './nav.css';

const Log = () =>{
    if(isLoggedIn()){
        return(
            <Button
          onClick={() => {
            deleteTokens();
            window.location.replace("/")
          }}
        >
          Sign out
        </Button>
        )
    }
    // else{
    //     return(
    //          <Link to="/login">Video Window</Link>
    //     )
    // }
    return(
        <Button
      onClick={() => {
        deleteTokens();
        window.location.replace("/")
      }}
    >
      Sign out
    </Button>
    )
}

const NavBar =  () =>{
    
        return(
            <Navbar className="nav-container">
                <Nav className="pull-right">
                    <NavItem className="navitem" eventKey={1} href="#">
                    <Log/>
                    </NavItem>
                </Nav>
            </Navbar>
        )
}

export default NavBar