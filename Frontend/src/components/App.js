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
import RegisterPage from "./pages/RegisterPage";

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
    const [leagues, setLeagues] = useState([]);
    const [currentLeague, setCurrentLeague] = useState();
    const [openBets, setOpenBets] = useState()
    const [closedBets, setClosedBets] = useState()
    const [error, setError] = useState();

    useEffect(() => {
        setCsrftoken(getCookie('csrftoken'))
        getCurrentUser()
        getLeagues()
        getBets()
    }, [])

    function getCurrentUser(){
        fetch('/api/account/current-user')
        .then((response) => {
            response.json()
            .then((data) => {
                setUser({...data})
            })

        })
    }

    function getLeagues() {
        fetch('/api/SIH/get-all-leagues')
        .then((response) => {
            response.json()
            .then((data) => {
                setLeagues([...data])
            })
        })
    }

    function getBets(){
        fetch('/api/SIH/get-league-bet-history?q=' + "1234")
        .then((response) => {
            response.json()
            .then((data) => {
                console.log(data)
            })
        })
    }

    function handleLogin(userData) {
        setUser(userData)
        setCsrftoken(getCookie('csrftoken'))
    }

    function handleLogout(userData) {
        setUser(userData)
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
                                        leagues={leagues}
                                        currentLeague={currentLeague}
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
                        <Route 
                            path='/register'
                            element={<RegisterPage
                            
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