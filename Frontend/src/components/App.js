import React, { Component } from "react";
import { render } from "react-dom";
import { BrowserRouter, Routes, Route, } from 'react-router-dom';
import NavBar from './organisms/NavBar';
import Playground from "./playground/playground";
import HomePage from './pages/HomePage'
import { 
    Box 
} from '@mui/material'


export default function App(props){
    return (
        <div>
            <BrowserRouter>
                <NavBar/>
                <Box sx={{ pt : 7, pl : 0 , maxHeight: '100%'}}>
                    <Routes>
                        <Route exact path='/' element={<HomePage/>}/>
                        <Route path='/test' element={<Playground/>}/>
                    </Routes>
                </Box>
            </BrowserRouter>
        </div>
    )
}

const rootDiv = document.getElementById("root")
render(<App/>, rootDiv)