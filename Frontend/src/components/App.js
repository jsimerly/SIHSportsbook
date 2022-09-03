import React, { Component, useState, useEffect } from "react";
import { render } from "react-dom";
import { BrowserRouter, Routes, Route, Navigate, useNavigate,} from 'react-router-dom';
import { 
    Box 
} from '@mui/material'

import NavBar from './organisms/NavBar';
import LeagueBettingPage from './pages/LeagueBettingPage'
import LoginPage from "./pages/LoginPage";
import Playground from "./playground/playground";
import RegisterPage from "./pages/RegisterPage";
import NewLeaguePage from "./pages/NewLeaguePage";
import LeagueRouter from "./routers/leagueRouter"

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
    const [currentLeague, setCurrentLeague] = useState(
        JSON.parse(localStorage.getItem('currentLeague')) || null
    );
    const [openBets, setOpenBets] = useState([])
    const [closedBets, setClosedBets] = useState([])
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
                if (data.isLoggedIn == false){
                    <Navigate to='/login'/>
                }
            })
        })
    }

    function handleLeagueChange(league) {
        setCurrentLeague(league)
        localStorage.setItem('currentLeague', JSON.stringify(league))
    }

    function getLeagues() {
        console.log(leagues)
        fetch('/api/betting/get-all-leagues')
        .then((response) => {
            response.json()
            .then((data) => {
                setLeagues([...data]);
                if (currentLeague === null){
                    handleLeagueChange(data[0])
                }
            })
        })
    }

    function getBets(){
        // fetch('/api/betting/get-league-bet-history' + '?bettor-id=' + currentLeague.bettor_id)
        // .then((response) => {
        //     response.json()
        //     .then((json)=>{
        //         console.log(json)
        //         setOpenBets(json.open)
        //         setClosedBets(json.closed)
        //     })
        // })
    }

    function handleLogin(userData) {
        setUser(userData)
        setCsrftoken(getCookie('csrftoken'))
    }

    function handleLogout(userData) {
        setUser(userData)
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
                            path='' 
                            element={
                                <LeagueRouter
                                    leagues={leagues}
                                    currentLeague={currentLeague}
                                    user={user}
                                />
                            }
                        />
                        <Route
                            path='/sportsbook/:leagueId' 
                            element={
                                <LeagueBettingPage
                                    setLeague={handleLeagueChange}
                                    leagues={leagues}
                                    currentLeague={currentLeague}
                                    getCookie={getCookie}
                                    openBets={openBets}
                                    closedBets={closedBets}
                                />
                            }
                        />
                        <Route 
                            path='/login' 
                            element={
                                <LoginPage 
                                    handleLogin={handleLogin}
                                />
                            }
                        />
                        <Route 
                            path='/register'
                            element={
                                <RegisterPage
                            
                                />
                            }
                        />
                        <Route
                            path='/new-league'
                            element={
                                <NewLeaguePage

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