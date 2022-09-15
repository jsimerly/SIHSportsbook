import React, { useState, useEffect } from  "react";
import {
    useNavigate,
    Link,
    Navigate
} from "react-router-dom";

import { 
    Button, 
    Grid, 
    Typography, 
    FormControl,
    Input,
    InputLabel,
    Box
 } from '@mui/material';

export default function LoginPage(props){
    const [email, setEmail] = useState()
    const [password, setPassword] = useState()
    const [error, setError] = useState()    
    const navigate = useNavigate()

    useEffect(()=>{
        if (props.user.isLoggedIn == true){
            navigate('/')
        }
    },[props.user])

    function handleEmailChanged(e) {
        setEmail(e.target.value);
    }

    function handlePasswordChanged(e){
        setPassword(e.target.value)
    }

    function handleLogin(){
        console.log('herere')
        const requestOptions = {
            method: 'POST',
            headers: {
                'Content-Type' : 'application/json',
            },
            body: JSON.stringify({
                email: email,
                password: password
            })
        }

        fetch('/api/account/login/', requestOptions)
        .then((response) => {
            if (response.status===202) {
                response.json()
                .then((data) => {
                    props.handleLogin(data)
                    navigate('/')
                })                
            } else {
                setError(response.json())
            }
        })
    }

    return (
        <Box sx={{mt:5}}>
            <Grid container spacing={1}>
                <Grid item xs={12} align="center">
                    <Typography component='h4' variant='h4'>
                        Login
                    </Typography>
                </Grid>
                <Grid item xs={12} align="center">
                    <FormControl>
                        <InputLabel> e-mail </InputLabel>
                        <Input
                            name="email"
                            type="email"
                            autoComplete="email"
                            onChange={handleEmailChanged}
                        />
                    </FormControl>
                </Grid>
                <Grid item xs={12} align="center">
                    <FormControl>
                        <InputLabel> password </InputLabel>
                            <Input
                                name="password"
                                type="password"
                                autoComplete="password"
                                onChange={handlePasswordChanged}
                            />
                    </FormControl>
                </Grid>
                <Grid item xs={12} align="center">
                    <Button
                        variant="contained"
                        color="primary"
                        onClick={handleLogin}
                    >
                        Log-In
                    </Button>
                </Grid>
                <Grid item xs={12} align="center">
                    <a href='/register'> Register </a>
                </Grid>
            </Grid>
        </Box>
    )
}