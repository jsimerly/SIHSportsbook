import React, { Component, useState, useEffect } from "react";
import { render } from "react-dom";
import { BrowserRouter, Routes, Route, } from 'react-router-dom';
import NavBar from './organisms/NavBar';
import LoginPage from "./pages/LoginPage";
import Playground from "./playground/playground";
import HomePage from './pages/HomePage'
import { 
    Box 
} from '@mui/material'

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

export default function App(props){
    const [csrftoken, setCsrftoken] = useState(getCookie('csrftoken'));
    const [user, setUser] = useState({
        email: "",
        isLoggedIn: null,
    });
    const [currentLeague, setCurrentLeague] = useState();
    const [error, setError] = useState();

    useEffect(() => {
        setCsrftoken(getCookie('csrftoken'))
        getCurrentUser()
    }, [])

    function getCurrentUser(){
        fetch('/api/account/current-user')
        .then((response) => {
            if (response.status === 200) {
                response.json()
                .then((data) => {
                    console.log(data)
                    setUser(data)
                })
            } else {
                setError('No User')
            }
        })
    }

    function handleLogin(userData) {
        setUser(userData)
        setCsrftoken(getCookie('csrftoken'))
    }

    function handleLogout() {
        getCurrentUser();
        window.location.reload()
    }
    
    function handleLeagueChange(league) {
        setCurrentLeague(league)
    }

    
    return (
        <div>
            <BrowserRouter>
                <NavBar 
                    user={user}
                    csrftoken={csrftoken}
                    handleLogout={handleLogout}
                />
                <Box sx={{ pt : 7, pl : 0 , maxHeight: '100%'}}>
                    <Routes>
                        <Route 
                            exact path='/' 
                            element={<HomePage
                                        csrftoken={csrftoken}
                                    />
                                    }
                        />
                        <Route 
                            path='/login' 
                            element={<LoginPage 
                                        handleLogin={handleLogin}
                                    />
                                    }
                        />
                        <Route path='/test' element={<Playground/>}/>
                    </Routes>
                </Box>
            </BrowserRouter>
        </div>
    )
}

const rootDiv = document.getElementById("root")
render(<App/>, rootDiv)