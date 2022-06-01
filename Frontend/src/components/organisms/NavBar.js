import React, { useEffect, useState } from "react";
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
    const [user, setUser] = useState(props.user)

    useEffect(() => {
        console.log(props.user)
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
                })
            }
        });
    }

    function userCorner() {
        if (user.isLoggedIn) {
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
            {console.log('rerendered ' + user.isLoggedIn)}
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