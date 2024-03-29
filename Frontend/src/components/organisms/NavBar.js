import React, { useEffect, useState } from "react";
import { Link, Navigate } from 'react-router-dom';
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
    const [user, setUser] = useState(props.user)

    useEffect(() => {
        setUser(props.user)
    }, [props.user])

    function handleLogOutClicked(crsftoken) {
        const requestOptions ={
            method: 'POST',
            headers: {
                'Content-Type' : 'application/json',
                'X-CSRFToken' : crsftoken
            },
        };

        fetch('/api/account/logout/', requestOptions)
        .then((response) => {

            if (response.status===200) {
                response.json()
                .then((data) => {
                    props.handleLogout(data)
                });
            }
        });
    }

    function userCorner() {
        if (user.isLoggedIn) {
            return (
                <Button 
                    href='/login' 
                    color='secondary' 
                    onClick={() => handleLogOutClicked(props.csrftoken)}> Logout </Button>
            )
        } else {
            return (
                <Grid container justifyContent="flex-end">
                    <Grid item>
                        <Button color='warning' component={Link} to='login'> Login </Button>
                    </Grid>
                    <Grid item>
                        <Button color='warning' component={Link} to='register'> Register </Button>
                    </Grid>
                </Grid>
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