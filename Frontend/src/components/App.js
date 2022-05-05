import React, { Component } from "react";
import { render } from "react-dom";
import PageRouter from "./PageRouter";
import DrawerComp from "./Drawer";
import NavBar from "./NavBar";

export default function App(props){
    return (
        <div>
            <NavBar/>
        </div>
       
    )
}

const rootDiv = document.getElementById("root")
render(<App/>, rootDiv)