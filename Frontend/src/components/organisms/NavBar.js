import React, { Component, useEffect, useState } from "react";
import { Link } from 'react-router-dom';
import { 
    AppBar,
    Toolbar,
    Grid,
    Tabs,
    Tab,
    Button,
    Typography,
 } from '@mui/material';



export default function NavBar(props){
    console.log(props.csrftoken)

    function handleLogOutClicked(crsftoken) {
        console.log('func: ' + crsftoken)
        const requestOptions ={
            method: 'POST',
            headers: {
                'Content-Type' : 'application/json',
                'X-CSRFToken' : crsftoken
            },
        };

        fetch('/api/account/logout/', requestOptions)
        .then((response) => console.log(response.json()));
        window.location.reload()
    }

    function userCorner() {
        if (props.user.isLoggedIn) {
            return (
                <Button color='secondary' onClick={() => handleLogOutClicked(props.csrftoken)}> Logout </Button>
            )
        } else {
            return (
                <Button color='warning' component={Link} to='login'> Login </Button>
            )
        }
    }
 
    return (
        <div>
            <AppBar>
                <Toolbar>
                    <Grid container>
                        <Grid item xs={3} md={3}>
                            <Button component={Link} to='/'>
                                <img src={"../../static/images/LockV1.png"} height={40} width={40}/>
                            </Button>  
                        </Grid>
                        <Grid item xs={6} md={6} justifyContent="center" style={{display:'flex'}}>
                            <Tabs>
                                <Tab label='Sportsbook'/>
                                <Tab label='Bets'/>
                                <Tab label='League'/>
                                <Tab label='Stats'/>
                            </Tabs>
                        </Grid>
                        <Grid item xs={3} md={3} justifyContent='flex-end' style={{display:'flex'}}> 
                            {userCorner()}
                        </Grid>
                    </Grid>
                </Toolbar>
            </AppBar>
        </div>
    )
}